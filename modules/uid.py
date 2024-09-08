name = "uid"
description = "Hiển thị ID của người gửi tin nhắn."
cooldown = 5  
category = "Utility"  
isAdmin = False

def run(api, events):
    """
    Hàm này sẽ được gọi khi lệnh `showid` được sử dụng.
    Nó sẽ gửi ID của người gửi tin nhắn.
    """

    sender_id = events.get("sender_id", "Không tìm thấy ID")

    message = f"{sender_id}"
    
    api.send_message(message, thread_id=events["thread_id"])
