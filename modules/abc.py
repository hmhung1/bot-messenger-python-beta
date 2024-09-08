name = ""
description = "abc"
cooldown = 5 
category = "Utility"
isAdmin = False

def run(api, events):
 
    api.send_message("Chưa nhập tên lệnh.", thread_id=events["thread_id"], message_id=events["message_id"])
