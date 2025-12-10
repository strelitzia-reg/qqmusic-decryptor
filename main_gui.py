import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import frida
import os
import hashlib
import threading
import logging
import sys
from datetime import datetime

class QQMusicDecryptorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("QQ音乐解密工具 v1.0")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # 设置图标（如果有的话）
        try:
            self.root.iconbitmap("icon.ico")
        except:
            pass
        
        self.setup_ui()
        self.setup_logging()
        
        # 状态变量
        self.is_processing = False
        self.session = None
        self.script = None
        
    def setup_ui(self):
        # 主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 标题
        title_label = ttk.Label(main_frame, text="QQ音乐解密工具", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # 输入目录选择
        ttk.Label(main_frame, text="输入目录:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.input_path = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.input_path, width=50).grid(row=1, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        ttk.Button(main_frame, text="浏览", command=self.browse_input).grid(row=1, column=2, pady=5)
        
        # 输出目录选择
        ttk.Label(main_frame, text="输出目录:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.output_path = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.output_path, width=50).grid(row=2, column=1, padx=5, pady=5, sticky=(tk.W, tk.E))
        ttk.Button(main_frame, text="浏览", command=self.browse_output).grid(row=2, column=2, pady=5)
        
        # 控制按钮框架
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=3, pady=20)
        
        self.start_button = ttk.Button(button_frame, text="开始解密", command=self.start_decryption)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = ttk.Button(button_frame, text="停止", command=self.stop_decryption, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(button_frame, text="清空日志", command=self.clear_log).pack(side=tk.LEFT, padx=5)
        
        # 进度条
        self.progress = ttk.Progressbar(main_frame, mode='determinate')
        self.progress.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        # 状态标签
        self.status_label = ttk.Label(main_frame, text="准备就绪")
        self.status_label.grid(row=5, column=0, columnspan=3, pady=5)
        
        # 统计信息
        stats_frame = ttk.Frame(main_frame)
        stats_frame.grid(row=6, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))
        
        ttk.Label(stats_frame, text="统计信息:").grid(row=0, column=0, sticky=tk.W)
        self.stats_text = tk.StringVar(value="总文件: 0, 成功: 0, 失败: 0, 跳过: 0")
        ttk.Label(stats_frame, textvariable=self.stats_text).grid(row=0, column=1, sticky=tk.W, padx=10)
        
        # 日志区域
        ttk.Label(main_frame, text="操作日志:").grid(row=7, column=0, sticky=tk.W, pady=(10, 0))
        self.log_area = scrolledtext.ScrolledText(main_frame, width=80, height=20)
        self.log_area.grid(row=8, column=0, columnspan=3, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 署名
        ttk.Label(main_frame, text="工具由 Strelitzia 开发", font=("Arial", 8), foreground="gray").grid(
            row=9, column=2, sticky=tk.E, pady=(10, 0)
        )
        
        # 配置网格权重
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(8, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # 设置默认路径
        self.input_path.set("D:\\Music\\VipSongsDownload")
        self.output_path.set("D:\\DecryptedMusic")
    
    def setup_logging(self):
        # 创建自定义日志处理器
        class TextHandler(logging.Handler):
            def __init__(self, text_widget):
                super().__init__()
                self.text_widget = text_widget
                
            def emit(self, record):
                msg = self.format(record)
                self.text_widget.insert(tk.END, msg + '\n')
                self.text_widget.see(tk.END)
        
        # 配置日志
        self.log_handler = TextHandler(self.log_area)
        self.log_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(self.log_handler)
    
    def browse_input(self):
        path = filedialog.askdirectory(title="选择加密文件目录")
        if path:
            self.input_path.set(path)
    
    def browse_output(self):
        path = filedialog.askdirectory(title="选择输出目录")
        if path:
            self.output_path.set(path)
    
    def log(self, message, level=logging.INFO):
        self.logger.log(level, message)
    
    def clear_log(self):
        self.log_area.delete(1.0, tk.END)
    
    def update_status(self, message):
        self.status_label.config(text=message)
        self.root.update_idletasks()
    
    def update_stats(self, total, success, failed, skipped):
        self.stats_text.set(f"总文件: {total}, 成功: {success}, 失败: {failed}, 跳过: {skipped}")
    
    def start_decryption(self):
        if not self.input_path.get() or not self.output_path.get():
            messagebox.showerror("错误", "请选择输入和输出目录")
            return
        
        if not os.path.exists(self.input_path.get()):
            messagebox.showerror("错误", "输入目录不存在")
            return
        
        # 创建输出目录
        os.makedirs(self.output_path.get(), exist_ok=True)
        
        # 更新UI状态
        self.is_processing = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.progress['value'] = 0
        
        # 在新线程中运行解密
        thread = threading.Thread(target=self.run_decryption)
        thread.daemon = True
        thread.start()
    
    def stop_decryption(self):
        self.is_processing = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.update_status("解密已停止")
        
        # 断开Frida连接
        if self.session:
            try:
                self.session.detach()
            except:
                pass
    
    def run_decryption(self):
        try:
            input_dir = self.input_path.get()
            output_dir = self.output_path.get()
            
            self.log("正在连接到QQ音乐进程...")
            self.update_status("正在连接到QQ音乐...")
            
            # 连接到QQ音乐进程
            try:
                self.session = frida.attach("QQMusic.exe")
                self.log("✓ 成功连接到QQ音乐进程")
            except Exception as e:
                self.log(f"✗ 连接QQ音乐进程失败: {e}", logging.ERROR)
                self.log("请确保: 1) QQ音乐正在运行 2) frida-server已启动", logging.ERROR)
                self.stop_decryption()
                return
            
            # 加载解密脚本
            try:
                with open("hook_qq_music.js", "r", encoding="utf-8") as f:
                    script_code = f.read()
                self.script = self.session.create_script(script_code)
                self.script.load()
                self.log("✓ 解密脚本加载成功")
            except Exception as e:
                self.log(f"✗ 加载解密脚本失败: {e}", logging.ERROR)
                self.stop_decryption()
                return
            
            # 查找加密文件
            self.log("正在扫描加密文件...")
            self.update_status("正在扫描文件...")
            
            encrypted_files = []
            for root, dirs, files in os.walk(input_dir):
                for file in files:
                    file_ext = os.path.splitext(file)[-1].lower()
                    if file_ext in [".mflac", ".mgg"]:
                        encrypted_files.append(os.path.join(root, file))
            
            if not encrypted_files:
                self.log("未找到任何.mflac或.mgg文件", logging.WARNING)
                self.stop_decryption()
                return
            
            self.log(f"找到 {len(encrypted_files)} 个加密文件")
            self.update_status(f"开始解密 {len(encrypted_files)} 个文件...")
            
            # 统计变量
            total_files = len(encrypted_files)
            success_files = 0
            failed_files = 0
            skipped_files = 0
            
            # 处理每个文件
            for i, encrypted_file in enumerate(encrypted_files):
                if not self.is_processing:
                    break
                
                # 更新进度
                progress = (i / total_files) * 100
                self.progress['value'] = progress
                self.update_stats(total_files, success_files, failed_files, skipped_files)
                
                file_name = os.path.basename(encrypted_file)
                self.log(f"处理文件 {i+1}/{total_files}: {file_name}")
                
                # 构建输出文件名
                file_ext = os.path.splitext(file_name)[-1].lower()
                if file_ext == ".mflac":
                    output_ext = ".flac"
                else:  # .mgg
                    output_ext = ".ogg"
                
                output_file = os.path.splitext(file_name)[0] + output_ext
                output_file_path = os.path.join(output_dir, output_file)
                
                # 检查文件是否已存在
                if os.path.exists(output_file_path):
                    self.log(f"文件已存在，跳过: {output_file}")
                    skipped_files += 1
                    continue
                
                # 创建临时文件名
                temp_file_name = hashlib.md5(file_name.encode()).hexdigest() + output_ext
                temp_file_path = os.path.join(output_dir, temp_file_name)
                
                try:
                    # 调用解密函数
                    self.log(f"开始解密: {file_name}")
                    result = self.script.exports_sync.decrypt(encrypted_file, temp_file_path)
                    
                    if "Success" in result:
                        # 重命名临时文件
                        os.rename(temp_file_path, output_file_path)
                        success_files += 1
                        self.log(f"✓ 解密成功: {output_file}")
                    else:
                        failed_files += 1
                        self.log(f"✗ 解密失败: {file_name} - {result}", logging.ERROR)
                        # 清理临时文件
                        if os.path.exists(temp_file_path):
                            os.remove(temp_file_path)
                            
                except Exception as e:
                    failed_files += 1
                    self.log(f"✗ 处理文件时出错: {file_name} - {e}", logging.ERROR)
                    # 清理临时文件
                    if os.path.exists(temp_file_path):
                        os.remove(temp_file_path)
            
            # 完成处理
            self.progress['value'] = 100
            self.update_stats(total_files, success_files, failed_files, skipped_files)
            
            if self.is_processing:
                self.log("=" * 50)
                self.log("批量解密完成!")
                self.log(f"总文件数: {total_files}")
                self.log(f"成功: {success_files}")
                self.log(f"失败: {failed_files}")
                self.log(f"跳过: {skipped_files}")
                self.log(f"输出目录: {output_dir}")
                self.update_status("解密完成")
                
                if failed_files == 0:
                    messagebox.showinfo("完成", f"解密完成！成功处理 {success_files} 个文件。")
                else:
                    messagebox.showwarning("完成", 
                                         f"解密完成！\n成功: {success_files}\n失败: {failed_files}\n跳过: {skipped_files}")
            
        except Exception as e:
            self.log(f"解密过程发生错误: {e}", logging.ERROR)
            messagebox.showerror("错误", f"解密过程发生错误: {e}")
        
        finally:
            # 断开连接
            if self.session:
                try:
                    self.session.detach()
                except:
                    pass
            
            # 恢复UI状态
            self.is_processing = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    # 检查frida是否可用
    try:
        import frida
    except ImportError:
        print("错误: 未安装frida，请先运行: pip install -r requirements.txt")
        input("按回车键退出...")
        sys.exit(1)
    
    root = tk.Tk()
    app = QQMusicDecryptorGUI(root)
    root.mainloop()