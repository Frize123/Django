import requests

def send_msg(msg):
    token="5475871685:AAHldVylXC8xXEgkn7f_I1FdlEgJdyjSXLY"
    url = "https://api.telegram.org/bot"
    channel_id="-742389096"
    url += token
    method = url + "/sendMessage"

    print(msg)
    print(method)

    r = requests.post(method, data={
        "chat_id": channel_id,
        "text": msg
    })
