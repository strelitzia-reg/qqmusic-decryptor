@echo off
chcp 65001 >nul
title QQ音乐解密工具

echo ========================================
echo        QQ音乐解密工具 v1.0
echo ========================================
echo.

echo 检查Python环境...
python --version >nul 2>&1
if errorlevel 1 (
    echo 错误: 未找到Python，请先安装Python 3.6+
    pause
    exit /b 1
)

echo 检查依赖包...
pip show frida >nul 2>&1
if errorlevel 1 (
    echo 安装依赖包...
    pip install -r requirements.txt
)

echo 启动图形界面...
python main_gui.py

pause