import os
import importlib

name = "menu"
description = "Hiển thị danh sách các lệnh hiện có theo danh mục."
cooldown = 10  
category = "Utility"  
isAdmin = False

def run(api, events):
   
    # Giả sử api.commands chứa các lệnh đã cấu hình
    commands = api.commands  
    
    # Tạo danh sách các lệnh theo danh mục
    categories = {}
    
    for command_name, command_info in commands.items():
        cmd_category = command_info.get('category', 'Không phân loại')
        if cmd_category not in categories:
            categories[cmd_category] = []
        categories[cmd_category].append(command_name)
        
    message = "Danh sách các lệnh hiện có:\n\n"
    
    for cat, cmds in categories.items():
        message += f"📁 {cat}\n"
        message += ", ".join(f"{cmd}" for cmd in cmds)  
        message += "\n\n"
    
    api.send_message(message, thread_id=events["thread_id"], message_id=events["message_id"])
