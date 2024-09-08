import json

name = "events"
description = "Hiển thị dữ liệu trong `events` dưới dạng JSON."
cooldown = 10  
category = "Utility"  

def run(api, events):
    events_json = json.dumps(events, indent=4)
    
    api.send_message(events_json, thread_id=events["thread_id"])
