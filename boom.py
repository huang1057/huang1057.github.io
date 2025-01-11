import tkinter as tk
from tkinter import ttk
import requests
import subprocess
import os
import mysql.connector

# 数据库连接配置
db_config = {
    'user': 'huang1057',
    'password': '1057263',
    'host': 'localhost',
    'database': 'eebbkboomusers'
}

# 绘制浅蓝色背景
def draw_light_blue_background(canvas):
    canvas.configure(bg='lightblue')
    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill='lightblue')

# 验证用户信息
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
        print(f"Database error: {err}")
        return False

# 下载文件并显示进度
def download_file_with_progress(url, local_filename, canvas, progress_label):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    progress = 0

    for data in response.iter_content(block_size):
        progress += len(data)
        progress_percent = int((progress / total_size) * 100)
        progress_label.config(text=f"Downloading... {progress_percent}%")
        canvas.update()
        with open(local_filename, 'wb') as file:
            file.write(data)

# 下载并运行EXE文件
def download_and_run_exe(qq_number, serial_number, canvas, progress_label):
    if verify_info(qq_number, serial_number):
        download_directory = 'C:\\1057233'
        if not os.path.exists(download_directory):
            os.makedirs(download_directory)
        url = 'http://example.com/somefile.exe'
        local_filename = os.path.join(download_directory, 'downloaded_file.exe')
        
        download_file_with_progress(url, local_filename, canvas, progress_label)
        
        try:
            subprocess.run([local_filename], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to execute the file: {e}")
    else:
        print("Verification failed")

# 创建主窗口
root = tk.Tk()
root.title("步步高学习机XX解除软件安装限制工具VX.X")

# 设置窗口在屏幕中间
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (root.winfo_width()/2))
y_cordinate = int((screen_height/2) - (root.winfo_height()/2))

root.geometry(f"+{x_cordinate}+{y_cordinate}")

# 创建一个Canvas作为背景
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(fill=tk.BOTH, expand=True)

# 初始绘制浅蓝色背景
draw_light_blue_background(canvas)

# 创建输入框和标签
label_qq = tk.Label(root, text="QQ号", font=("Arial", 14))
label_qq.place(x=250, y=50)

entry_qq = tk.Entry(root, font=("Arial", 12), width=30)
entry_qq.place(x=350, y=50)

label_serial = tk.Label(root, text="序列号", font=("Arial", 14))
label_serial.place(x=250, y=100)

entry_serial = tk.Entry(root, font=("Arial", 12), width=30)
entry_serial.place(x=350, y=100)

# 创建进度标签
progress_label = tk.Label(root, text="准备下载...", font=("Arial", 12))
progress_label.place(x=250, y=150)

# 创建提交按钮
button_submit = tk.Button(root, text="提交", command=lambda: download_and_run_exe(entry_qq.get(), entry_serial.get(), canvas, progress_label), font=("Arial", 14))
button_submit.place(x=250, y=200)

# 运行主循环
root.mainloop()
