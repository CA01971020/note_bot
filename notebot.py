import requests

# =======================
# ここを自分の情報に書き換える
CHANNEL_ACCESS_TOKEN = ""
USER_ID = ""
# =======================

url = "https://api.line.me/v2/bot/message/push"
headers = {
    "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

print("ノートボット起動！")
print("メッセージを入力して Enter で送信。終了するには exit または quit を入力してね。\n")

while True:
    text = input("送信メッセージ: ")
    if text.lower() in ["exit", "quit"]:
        print("Bot を終了します。")
        break

    data = {
        "to": USER_ID,
        "messages": [
            {"type": "text", "text": text}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("送信成功 ✅")
    else:
        print("送信失敗 ❌", response.status_code, response.text)
