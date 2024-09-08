import os
import importlib
import json
from fbapy import Client, API
from threading import Thread
import time

with open('config.json', 'r') as f:
    config = json.load(f)

client = Client()

with open('fbstate.txt', 'r') as file:
    appstate = file.read().strip()

api = client.login(
    appstate=appstate,
    options={
        "user_agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
    },
)

def load_modules():
    commands = {}
    for filename in os.listdir("modules"):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            spec = importlib.util.spec_from_file_location(module_name, os.path.join("modules", filename))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, "name") and hasattr(module, "description") and hasattr(module, "cooldown") and hasattr(module, "run") and hasattr(module, "category"):
                commands[module.name] = {
                    "description": module.description,
                    "cooldown": module.cooldown,
                    "category": module.category,
                    "run": module.run,
                    "last_used": 0  
                }
            else:
                print(f"Module {module_name} bị thiếu thuộc tính bắt buộc và sẽ không được nạp.")
    return commands

commands = load_modules()
api.commands = commands
api.config = config  

def callback(events, api: API):
    if events["type"] == "message":
        message_body = events["body"].strip()
        
        if message_body.startswith(api.config['prefix']):
            command_name = message_body[len(api.config['prefix']):].split(" ")[0]
            
            if command_name in commands:
                command = commands[command_name]
                
                current_time = time.time()
                if current_time - command["last_used"] >= command["cooldown"]:
                    Thread(target=command["run"], args=(api, events)).start()
                    command["last_used"] = current_time
                else:
                    api.send_message(f"Vui lòng chờ {int(command['cooldown'] - (current_time - command['last_used']))} giây nữa trước khi sử dụng lại lệnh này.", thread_id=events["thread_id"])

api.listen_mqtt(callback)
