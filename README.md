![BOOKOO Hydration Preview](preview.jpeg)

# 💧 BOOKOO Hydration

**BOOKOO Hydration** is a high-aesthetic smart hydration monitoring system. It connects to your digital scale via Bluetooth to automatically recognize your drinking behavior, record daily intake, and generate health trend charts.

No manual recording is required—simply pick up the cup, drink, and place it back to automatically log the data.

---

## ✨ Key Features

*   **Smart Sensing**: Automatically distinguishes between "drinking", "refilling", and "accidental touch" actions.
*   **Ghost UI**: When the cup is lifted, the value remains unchanged (grayed out) to provide visual continuity; the difference is automatically calculated and settled when placed back.
*   **Data Visualization**:
    *   **Daily Dashboard**: Real-time display of milliliters (mL) and goal progress bar.
    *   **Weekly Trends**: Automatic bar chart statistics of hydration achievements over the past 7 days.
    *   **History Timeline**: Detailed record of the time and amount of each water intake.
*   **Data Persistence**: Records are saved in the browser's local storage, ensuring no data loss upon page refresh or computer restart.
*   **Multi-language Support**: One-click toggle between Chinese (zh) and English (en).
*   **Cross-Platform Adaptation**: Uses a responsive layout, perfectly supporting both large desktop screens and mobile devices.

---

## 🚀 Quick Start

### 1. Environment Preparation
Ensure your computer has Python 3.7+ installed. Open a terminal and install the necessary dependency libraries:
```bash
pip install fastapi uvicorn bleak
```

### 2. Start Service
Run the backend bridge program in the project directory:
```bash
python server_bridge.py
```

The service is ready when the terminal displays `Uvicorn running on http://0.0.0.0:8000` and prompts `✅ Bluetooth Connected`.

### 3. Open Application
*   **Desktop**: Directly double-click to open the `BOOKOO_hydration.html` file.
*   **Mobile (Recommended)**:
    *   Ensure your phone and computer are connected to the same Wi-Fi network.
    *   Open a new terminal in the project directory and run the following command to host the files:
        ```bash
        python -m http.server 8080
        ```
    *   Visit on your mobile browser: `http://<Computer-LAN-IP>:8080/BOOKOO_hydration.html`.

### ⚙️ User Guide (First Time Calibration)
To ensure data accuracy, please click the ⚙️ icon in the top right corner to enter the settings panel for initial calibration:
*   **HW Tare**: Remove all items from the scale and click the button to ensure the weight returns to zero.
*   **Set Empty**: Place your empty cup on the scale and click `∅ Empty`.
*   **Set Full**: Fill the cup with water, place it on the scale, and click `💧 Full` (used to calculate water level percentage).
*   **Set Goal**: Input your planned daily total water intake (default is 2000mL).

### 🛠️ Common Operations
*   **Pause Recording**: Click `⏸ Pause` in settings. You can now use the scale for other weighing tasks without interfering with the hydration logic.
*   **Undo**: If a misrecord occurs, click `↺ Undo Last` in settings to delete the most recent record and revert progress.
*   **Clear Data**: Click `Clear All` to reset all local historical records.

### 📱 Full Screen Experience on Mobile
In the iOS Safari browser, tap the **Share button -> Add to Home Screen** at the bottom to get a native app-like full-screen immersive experience.

---
---

# 💧 BOOKOO Hydration

**BOOKOO Hydration** 是一款高颜值的智能饮水监测系统。它通过蓝牙连接你的电子秤，自动识别你的喝水行为，记录每日摄入量，并生成健康趋势图表。

无需手动记录，拿起杯子喝水，放回即自动记账。

---

## ✨ 核心功能

* **智能感应**：自动区分“喝水”、“注水”和“误触”动作。
* **幽灵模式 (Ghost UI)**：拿起杯子时数值保持不变（变灰），提供视觉延续感；放回后自动结算差值。
* **数据可视化**：
    * **今日看板**：实时显示毫升数 (mL) 和目标进度条。
    * **本周趋势**：自动统计过去 7 天的饮水达成情况柱状图。
    * **历史时间轴**：详细记录每一次饮水的时间和水量。
* **数据持久化**：记录保存在浏览器本地，刷新网页或重启电脑数据不丢失。
* **多语言支持**：一键切换 中文 (zh) / English (en)。
* **跨平台适配**：采用自适应布局，完美支持电脑大屏和手机移动端。

---

## 🚀 快速开始

### 1. 环境准备
确保电脑已安装 Python 3.7+。打开终端安装必要的依赖库：
```bash
pip install fastapi uvicorn bleak
```

### 2. 启动服务
在项目目录下运行后端桥接程序（建议重命名为 server_bridge.py）：
```bash
python server_bridge.py
```

当终端显示 `Uvicorn running on http://0.0.0.0:8000` 且提示 `✅ 蓝牙已连接` 时，说明服务已就绪。

### 3. 打开应用
* **电脑端**：直接双击打开 `BOOKOO_hydration.html` 文件。
* **手机端（推荐）**：
    * 确保手机和电脑连接在同一个 Wi-Fi 下。
    * 在项目目录新开一个终端运行以下命令以托管文件：
      ```bash
      python -m http.server 8080
      ```
    * 在手机浏览器访问：`http://<电脑局域网IP地址>:8080/BOOKOO_hydration.html`。

### ⚙️ 使用指南 (首次校准)
为了保证数据准确，初次使用请点击右上角 ⚙️ 进入设置面板进行校准：
* **硬件去皮 (HW Tare)**：移走秤上所有物品，点击按钮，确保重量回零。
* **设定空杯 (Empty)**：放上你的空杯子，点击 `∅ Empty`。
* **设定满杯 (Full)**：把杯子加满水放上去，点击 `💧 Full`（用于计算杯内水位百分比）。
* **设定目标**：输入你每日计划的饮水总量（默认 2000mL）。

### 🛠️ 常见操作
* **暂停记录**：在设置中点击 `⏸ Pause`，此时你可以使用秤进行其他称重操作而不受饮水逻辑干扰。
* **撤销误判**：如果发生误记录，点击设置里的 `↺ Undo Last` 即可删除最近一条记录并回退进度。
* **清空数据**：点击 `Clear All` 将重置本地所有历史记录。

### 📱 手机全屏体验
在 iOS Safari 浏览器中，点击底部 **分享按钮 -> 添加到主屏幕**，即可获得类似原生 App 的全屏沉浸体验。
