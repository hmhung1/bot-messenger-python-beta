import os
import time
import psutil
from datetime import timedelta

start_time = time.time()

name = "uptime"
description = "Hiển thị thời gian hoạt động và thông tin hệ thống."
cooldown = 10 
category = "Utility" 
isAdmin = False

def get_uptime():
    """
    Hàm này tính toán thời gian hoạt động từ thời điểm bot khởi động.
    """
    elapsed_time = time.time() - start_time
    return str(timedelta(seconds=int(elapsed_time)))

def run(api, events):
    """
    Hàm này sẽ được gọi khi lệnh `uptime` được sử dụng.
    Nó sẽ gửi thời gian hoạt động và thông tin hệ thống.
    """
    uptime = get_uptime()
    
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_used = memory_info.used / (1024 * 1024)  # MB
    memory_total = memory_info.total / (1024 * 1024)  # MB
    memory_free = memory_info.available / (1024 * 1024)  # MB
   
    message = (
        f"⏱️ Thời gian hoạt động: {uptime}\n"
        f"💻 Sử dụng CPU: {cpu_usage}%\n"
        f"🤖 Ram đã sử dụng: {memory_used:.2f}/{memory_total:.2f} MB\n"
    )
    
    api.send_message(message, thread_id=events["thread_id"], message_id=events["message_id"])
