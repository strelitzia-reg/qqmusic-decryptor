# QQMusic Decryptor 🎵

[![GitHub Release](https://img.shields.io/github/v/release/Strelitzia/qqmusic-decryptor)](https://github.com/Strelitzia/qqmusic-decryptor/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A powerful, user-friendly desktop tool for batch decrypting VIP songs downloaded from QQ Music (`.mflac`, `.mgg` formats). Built with Python and Frida, it features a clean graphical interface and robust decryption capabilities.

## ✨ Features

*   **Graphical User Interface (GUI)**: Intuitive and easy-to-use interface built with Tkinter—no command-line expertise required.
*   **Batch Processing**: Automatically decrypts all `.mflac` and `.mgg` files in a selected directory.
*   **Real-Time Progress**: Monitor the decryption process with a live progress bar, detailed logs, and file statistics.
*   **Intelligent File Management**: Automatically skips already decrypted files to save time.
*   **Safe & Reliable**: Implements chunked reading and retry mechanisms for stable decryption of large files.
*   **Cross-Format Support**: Converts `.mflac` to `.flac` and `.mgg` to `.ogg` seamlessly.

## 📸 Screenshot

*(Replace the placeholder below with an actual screenshot of your application, e.g., named `screenshot.png`)*
![QQMusic Decryptor GUI](screenshot.png)

## 🚀 Getting Started

### Prerequisites

Before using this tool, ensure you have the following installed and running:

1.  **Python 3.8 or higher**: [Download Python](https://www.python.org/downloads/)
2.  **QQ Music Client**: Latest version, logged in with a VIP account (for downloading songs).
3.  **Administrator Privileges** (Required to run `frida-server` on Windows).

### Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Strelitzia/qqmusic-decryptor.git
    cd qqmusic-decryptor
    ```

2.  **Install Python Dependencies**
    The tool's core requirements are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```
    > **Important Compatibility Note**: The specified `frida==16.7.10` requires **Python 3.8 or later**. If you are using Python 3.6 or 3.7, please upgrade your Python interpreter.

3.  **Start Frida-Server (CRITICAL STEP)**
    *   Download the **correct version** of `frida-server` (matching the `frida` Python package version `16.7.10`) from the [Frida releases page](https://github.com/frida/frida/releases) (look for `frida-server-16.7.10-windows-x86_64.exe.xz`).
    *   Extract the `.exe` file and run it **as Administrator** in a Command Prompt window. **Keep this window open** while using the decryptor.
    ```bash
    # Example: Navigate to your download folder and run
    frida-server.exe
    ```

### Usage

1.  **Launch QQ Music**: Ensure the official QQ Music client is running in the background.
2.  **Run the Decryptor**:
    ```bash
    python main_gui.py
    ```
    Or simply double-click `run.bat` on Windows.
3.  **Using the GUI**:
    *   **Input Directory**: Click "Browse" to select the folder containing your `.mflac`/`.mgg` files (e.g., `D:\Music\VipSongsDownload`).
    *   **Output Directory**: Select a folder where decrypted files will be saved (e.g., `D:\DecryptedMusic`).
    *   **Start**: Click the "Start Decryption" button. The progress bar and log window will show real-time status.
    *   **Stop**: You can pause the process at any time using the "Stop" button.

## 📖 FAQ (Frequently Asked Questions)

<details>
<summary><b>Decryption fails or the tool freezes.</b></summary>

*   **Verify Frida Connection**: Open a new terminal and run `frida-ps`. If it lists processes (including `QQMusic.exe`), the connection is good.
*   **Check Versions**: Ensure the `frida` Python package (`16.7.10`) and `frida-server` executable versions match exactly.
*   **Restart Services**: Close and restart both QQ Music and `frida-server` (as Administrator), then try again.
</details>

<details>
<summary><b>The output file is corrupted or won't play.</b></summary>

*   This usually indicates an incomplete read during decryption.
*   Ensure no other heavy applications are consuming excessive memory/CPU.
*   Try re-downloading the specific song in QQ Music and decrypt it again.
</details>

<details>
<summary><b>I get a "ModuleNotFoundError" for `frida`.</b></summary>

*   The dependencies did not install correctly. Please run:
    ```bash
    pip install -r requirements.txt
    ```
    Make sure your Python version is 3.8 or higher.
</details>

<details>
<summary><b>I get version errors when installing `frida`.</b></summary>

*   This project requires `frida==16.7.10`, which depends on **Python 3.8+**.
*   Please upgrade your Python interpreter to version 3.8 or later from the [official website](https://www.python.org/downloads/).
</details>

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1.  Fork the Project.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and development workflow.

## ⚖️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This tool is developed for **educational and research purposes only**. It is intended to allow users to exercise their fair use rights for music they have **legally purchased** through QQ Music's VIP service.

*   Users are solely responsible for ensuring they comply with their local copyright laws and QQ Music's terms of service.
*   The developers are **not responsible** for any misuse of this software.
*   Please support artists by purchasing their music through official channels.

---

**Tool developed by Strelitzia**