# QQ音乐解密工具

一个用于批量解密QQ音乐VIP下载歌曲的图形化工具。

## 功能特点

- 批量解密QQ音乐下载的 `.mflac` 和 `.mgg` 文件
- 用户友好的图形界面
- 实时显示解密进度和日志
- 支持暂停和继续操作
- 自动跳过已解密的文件

## 支持格式

- 输入: `.mflac`, `.mgg`
- 输出: `.flac`, `.ogg`

## 系统要求

- Windows 10/11
- Python 3.6+
- QQ音乐客户端（最新版本）
- 管理员权限（用于运行frida-server）

## 使用方法

### 1. 环境准备

1. 安装Python 3.6或更高版本
2. 运行 `run.bat` 或手动安装依赖：
   ```bash
   pip install -r requirements.txt