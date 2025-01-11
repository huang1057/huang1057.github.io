import tkinter as tk
from tkinter import messagebox, Toplevel, ttk
import requests
import subprocess
import os

# 数据库配置（示例）
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database'
}

def verify_info(qq_number, serial_number):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE qq_number=%s AND serial_number=%s", (qq_number, serial_number))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
    except mysql.connector.Error as err:
        messagebox.showerror("数据库错误", f"Failed to connect to MySQL: {err}")
        return False

def download_file_with_progress(url, local_filename):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    # 创建一个新窗口来显示进度条
    progress_window = tk.Toplevel(root)
    progress_window.title("下载进度")

    # 创建进度条
    progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=300, mode='determinate')
    progress_bar.pack(pady=20)

    # 下载文件并更新进度条
    with open(local_filename, 'wb') as file:
        for data in response.iter_content(block_size):
            file.write(data)
            progress_bar['value'] += (len(data) / total_size) * 100  # 更新进度条的值

    # 下载完成后关闭进度条窗口
    progress_window.destroy()

def download_and_run_exe(qq_number, serial_number):
    if verify_info(qq_number, serial_number):
        download_directory = 'C:\\1057233'
        if not os.path.exists(download_directory):
            os.makedirs(download_directory)
        url = 'http://example.com/somefile.exe'
        local_filename = os.path.join(download_directory, 'downloaded_file.exe')
        
        download_file_with_progress(url, local_filename)
        
        # 执行文件
        try:
            subprocess.run([local_filename], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("执行失败", f"Failed to execute the file: {e}")
    else:
        messagebox.showerror("验证失败", "QQ号或序列号不正确。")

# 创建主窗口
root = tk.Tk()
root.title("步步高学习机XX解除软件安装限制工具VX.X")

# 创建输入框和标签
label_qq = tk.Label(root, text="QQ号")
label_qq.pack()

entry_qq = tk.Entry(root)
entry_qq.pack()

label_serial = tk.Label(root, text="序列号")
label_serial.pack()

entry_serial = tk.Entry(root)
entry_serial.pack()

# 创建提交按钮
button_submit = tk.Button(root, text="提交", command=lambda: download_and_run_exe(entry_qq.get(), entry_serial.get()))
button_submit.pack(pady=20)

# 运行主循环
root.mainloop()
