import asyncio
import json
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket
from bleak import BleakClient, BleakScanner
from starlette.websockets import WebSocketState

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

SERVICE_UUID = "00000ffe-0000-1000-8000-00805f9b34fb"
DATA_CHAR_UUID = "0000ff11-0000-1000-8000-00805f9b34fb"
CMD_CHAR_UUID = "0000ff12-0000-1000-8000-00805f9b34fb"

COMMANDS = {
    "TARE": bytearray([0x03, 0x0A, 0x01, 0x00, 0x00, 0x08]),
    "START": bytearray([0x03, 0x0A, 0x04, 0x00, 0x00, 0x0A]),
    "STOP": bytearray([0x03, 0x0A, 0x05, 0x00, 0x00, 0x0D]),
    "RESET": bytearray([0x03, 0x0A, 0x06, 0x00, 0x00, 0x0C]),
}

connected_clients = set()
current_ble_client = None

async def broadcast_status():
    """定期向前端同步电子秤的连接状态"""
    while True:
        is_connected = current_ble_client is not None and current_ble_client.is_connected
        status_payload = json.dumps({"type": "status", "connected": is_connected})
        for ws in list(connected_clients):
            if ws.client_state == WebSocketState.CONNECTED:
                try:
                    await ws.send_text(status_payload)
                except: pass
        await asyncio.sleep(1)

async def ble_data_bridge():
    global current_ble_client
    while True:
        device = await BleakScanner.find_device_by_filter(
            lambda d, ad: SERVICE_UUID.lower() in [s.lower() for s in ad.service_uuids]
        )
        if not device:
            current_ble_client = None
            await asyncio.sleep(3)
            continue
        try:
            async with BleakClient(device) as client:
                current_ble_client = client
                logging.info(f"✅ 蓝牙已连接: {device.address}")

                def callback(sender, data):
                    if len(data) < 20: return
                    checksum = 0
                    for i in range(19): checksum ^= data[i]
                    if checksum != data[19]: return

                    # 解析重量与流速
                    weight_sign = -1 if data[6] == 45 else 1 
                    raw_weight = (data[7] << 16) | (data[8] << 8) | data[9]
                    weight = (raw_weight / 100.0) * weight_sign

                    flow_sign = -1 if data[10] == 45 else 1
                    raw_flow = (data[11] << 8) | data[12]
                    flow = (raw_flow / 100.0) * flow_sign

                    payload = json.dumps({
                        "type": "real",
                        "weight": round(weight, 2),
                        "flow": round(flow, 2),
                        "time": (data[2] << 16) | (data[3] << 8) | data[4],
                        "battery": data[13]
                    })
                    
                    for ws in list(connected_clients):
                        if ws.client_state == WebSocketState.CONNECTED:
                            asyncio.create_task(ws.send_text(payload))

                await client.start_notify(DATA_CHAR_UUID, callback)
                while client.is_connected:
                    await asyncio.sleep(1)
        except Exception as e:
            logging.error(f"蓝牙连接断开: {e}")
            current_ble_client = None
            await asyncio.sleep(2)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动蓝牙桥接和状态广播任务
    asyncio.create_task(ble_data_bridge())
    asyncio.create_task(broadcast_status())
    yield

app = FastAPI(lifespan=lifespan)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            msg = await websocket.receive_json()
            if current_ble_client and current_ble_client.is_connected:
                for action in msg.get("actions", []):
                    if action in COMMANDS:
                        await current_ble_client.write_gatt_char(CMD_CHAR_UUID, COMMANDS[action])
                        await asyncio.sleep(0.05)
    except: pass
    finally:
        connected_clients.remove(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)