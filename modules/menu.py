import os
import importlib

name = "menu"
description = "Hiển thị danh sách các lệnh hiện có theo danh mục."
cooldown = 10  # Thời gian chờ (giây) giữa các lần sử dụng lệnh
category = "Utility"  # Danh mục của lệnh
isAdmin = False

def run(api, events):
    """
    Hàm này sẽ được gọi khi lệnh `menu` được sử dụng.
    Nó sẽ gửi danh sách các lệnh hiện có theo danh mục, với các lệnh trong cùng một danh mục phân cách bằng dấu ','.
    """
    # Giả sử api.commands chứa các lệnh đã cấu hình
    commands = api.commands  
    
    # Tạo danh sách các lệnh theo danh mục
    categories = {}
    
    for command_name, command_info in commands.items():
        cmd_category = command_info.get('category', 'Không phân loại')
        if cmd_category not in categories:
            categories[cmd_category] = []
        categories[cmd_category].append(command_name)
    
    # Xây dựng thông điệp từ danh sách các lệnh theo danh mục
    message = "Danh sách các lệnh hiện có:\n\n"
    
    for cat, cmds in categories.items():
        message += f"📁 {cat}\n"
        message += ", ".join(f"{cmd}" for cmd in cmds)  # Kết hợp các lệnh bằng dấu ',' và thêm dấu '/' trước tên lệnh
        message += "\n\n"
    
    api.send_message(message, thread_id=events["thread_id"], message_id=events["message_id"])
