import tkinter as tk
from tkinter import ttk
import requests
import subprocess
import os
import mysql.connector

def draw_gradient(canvas, width, height):
    for y in range(height):
        ratio = y / height
        color = f'#{int(255 * (1 - ratio)):02x}{int(255 * ratio):02x}FF'  # 从蓝色渐变到白色
        canvas.create_rectangle(0, y, width, y + 1, fill=color)

def verify_info(qq_number, serial_number):
    try:
        conn = mysql.connector.connect(
            user='root',
            password='yuelove233',
            host='localhost',
            database='users'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE qq_number=%s AND serial_number=%s", (qq_number, serial_number))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
    except mysql.connector.Error as err:
        print(f"数据库错误: {err}")
        return False

def download_file_with_progress(url, local_filename, canvas):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte

    progress = 0
    for data in response.iter_content(block_size):
        progress += len(data)
        progress_percent = int((progress / total_size) * 100)
        draw_gradient(canvas, 400, 300)  # 重新绘制渐变背景
        canvas.create_text(200, 150, text=f"正在下载... {progress_percent}%", fill="white", font=("Arial", 14))
        canvas.update()
        with open(local_filename, 'wb') as file:
            file.write(data)

def download_and_run_exe(qq_number, serial_number, canvas):
    if verify_info(qq_number, serial_number):
        download_directory = 'C:\\1057233'
        if not os.path.exists(download_directory):
            os.makedirs(download_directory)
        url = 'http://example.com/somefile.exe'
        local_filename = os.path.join(download_directory, '下载的文件.exe')
        
        download_file_with_progress(url, local_filename, canvas)
        
        # 执行文件
        try:
            subprocess.run([local_filename], check=True)
        except subprocess.CalledProcessError as e:
            print(f"执行文件失败: {e}")
    else:
        print("验证失败")

# 创建主窗口
root = tk.Tk()
root.title("步步高学习机XX解除软件安装限制工具VX.X")

# 创建一个Canvas作为背景
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill=tk.BOTH, expand=True)

# 初始绘制渐变
draw_gradient(canvas, 400, 300)

# 创建输入框和标签
label_qq = tk.Label(root, text="QQ号")
label_qq.place(x=150, y=50)

entry_qq = tk.Entry(root)
entry_qq.place(x=150, y=80)

label_serial = tk.Label(root, text="序列号")
label_serial.place(x=150, y=120)

entry_serial = tk.Entry(root)
entry_serial.place(x=150, y=150)

# 创建提交按钮
button_submit = tk.Button(root, text="提交", command=lambda: download_and_run_exe(entry_qq.get(), entry_serial.get(), canvas))
button_submit.place(x=150, y=180)

# 运行主循环
root.mainloop()
