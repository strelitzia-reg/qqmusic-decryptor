# qqmusic-decryptor
A GUI tool for batch decrypting QQ Music VIP songs
File structure程序结构
QQMusicDecryptor/
├── main_gui.py              # 主程序（图形界面）
├── hook_qq_music.js         # 解密脚本
├── requirements.txt         # 依赖包
├── run.bat                 # Windows运行脚本
└── README.md               # 说明文档
2. 启动服务
以管理员身份运行命令提示符
启动frida-server：
-frida-server.exe
保持此窗口开启
3.运行解密工具
启动QQ音乐并登录VIP账号
运行 run.bat 或直接运行：
-python main_gui.py
在界面中选择输入和输出目录
点击"开始解密"

注意事项
请确保QQ音乐正在运行
请确保frida-server已以管理员权限启动
本工具仅用于个人学习和研究
请确保您拥有歌曲的合法使用权

常见问题
连接失败
检查QQ音乐是否正在运行
检查frida-server是否已启动
尝试以管理员权限运行所有程序
解密失败
确保文件是通过VIP账号下载的
尝试重新下载有问题的歌曲
检查QQ音乐版本是否兼容

确保已启动：
QQ音乐客户端（登录VIP账号）
frida-server（以管理员权限运行）
在图形界面中选择输入输出目录，点击开始解密

✨ 功能特点
直观的图形界面：无需命令行操作
实时进度显示：进度条和详细日志
批量处理：自动处理目录下所有加密文件
错误处理：单个文件失败不影响其他文件
智能跳过：已解密的文件自动跳过
可中断操作：支持中途停止解密过程
