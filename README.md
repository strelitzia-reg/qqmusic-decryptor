# QQMusic Decryptor 🎵

[![GitHub Release](https://img.shields.io/github/v/release/Strelitzia/qqmusic-decryptor?include_prereleases)](https://github.com/Strelitzia/qqmusic-decryptor/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Strelitzia/qqmusic-decryptor/blob/main/CONTRIBUTING.md)

A powerful and user-friendly desktop application for batch decrypting VIP songs downloaded from QQ Music. This tool seamlessly converts encrypted `.mflac` and `.mgg` files into standard `.flac` and `.ogg` formats for offline playback.

## ✨ Features

- **Graphical User Interface (GUI)**: Intuitive interface built with Tkinter – no command-line skills required.
- **Batch Processing**: Automatically decrypts all `.mflac` and `.mgg` files in a selected folder.
- **Real-Time Monitoring**: Live progress bar, detailed operation logs, and file statistics.
- **Pause & Resume**: Stop the decryption process at any time.
- **Smart Skipping**: Automatically skips already decrypted files to save time.
- **Safe Operation**: Implements chunked reading to handle large files reliably.

## 🖼️ Screenshots

*(Placeholder: You can add a screenshot of your GUI here later)*
> *Example: `![Main Interface](screenshot.png)`*

## 🚀 Quick Start

### Prerequisites

Ensure you have the following ready on your Windows system:
1.  **Python 3.6 or higher** ([Download](https://www.python.org/downloads/))
2.  **QQ Music Client** (Latest version, logged in with a VIP account).
3.  **Administrator Privileges** (Required to run `frida-server`).

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/Strelitzia/qqmusic-decryptor.git
    cd qqmusic-decryptor
    ```

2.  **Install Python dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Decryptor

1.  **Start the required services**:
    - Launch the **QQ Music** client and keep it running.
    - Run **`frida-server.exe` as Administrator** (Download matching version from [Frida releases](https://github.com/frida/frida/releases)). Keep its window open.

2.  **Launch the GUI tool**:
    - **Option A**: Execute the main script.
      ```bash
      python main_gui.py
      ```
    - **Option B** (Windows): Simply double-click the `run.bat` file.

3.  **Use the interface**:
    - Click **"Browse..."** to select the folder containing your `.mflac`/`.mgg` files (Input).
    - Click **"Browse..."** to select an output folder for the decrypted files.
    - Click the **"Start Decryption"** button. Monitor progress via the bar and log window.

## 📖 Detailed Usage Guide

### Step 1: Preparing Frida-Server
This is the most critical step for the tool to work.
1.  Check your installed Frida version: `pip show frida | findstr Version`
2.  Download the `frida-server` archive with the **exact same version number** for Windows from the official releases page.
3.  Extract `frida-server.exe` and run it in a Command Prompt **opened as Administrator**. A blinking cursor indicates it's running correctly.

### Step 2: Downloading Music
- Use the QQ Music client to download the VIP songs you wish to decrypt. The encrypted files are typically stored in your designated download directory (e.g., `D:\Music\VipSongsDownload`).

### Step 3: Decryption Process
- The tool will scan, decrypt, and convert files one by one. Successful files will be saved as `.flac` or `.ogg`.
- If the process is interrupted, you can restart it. The tool will skip files already present in the output folder.

## ❓ Frequently Asked Questions (FAQ)

<details>
<summary><b>Decryption fails or the tool freezes.</b></summary>

- **Verify Frida Connection**: Open a new terminal and run `frida-ps`. If it lists processes, the connection is good.
- **Check Versions**: Ensure the `frida` Python package and `frida-server` executable versions match exactly.
- **Restart Services**: Close and restart both QQ Music and `frida-server`, then try again.
</details>

<details>
<summary><b>The output file is corrupted or won't play.</b></summary>

- This usually indicates an incomplete read during decryption. Ensure no other heavy applications are consuming memory. Try re-downloading the specific song in QQ Music and decrypt it again.
</details>

<details>
<summary><b>I get a "ModuleNotFoundError" for frida.</b></summary>

- The dependencies did not install correctly. Run: `pip install frida==16.7.10`
</details>

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

Please read [CONTRIBUTING.md](https://github.com/Strelitzia/qqmusic-decryptor/blob/main/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## ⚖️ License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Strelitzia/qqmusic-decryptor/blob/main/LICENSE) file for details.

## ⚠️ Disclaimer

This tool is developed for **educational and research purposes only**. It is intended to allow users to exercise their fair use rights for music they have legally purchased. The developers are not responsible for any misuse of this software. Please support artists by purchasing their music legally.

---

**Tool developed by Strelitzia**