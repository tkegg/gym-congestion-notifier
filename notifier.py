import requests
import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()
LINE_TOKEN = os.getenv("LINE_TOKEN")
LINE_USER_ID = os.getenv("LINE_USER_ID")

def send_line_message(count):
    # 送信するメッセージ
    message = f"🏋️ジムの混雑情報\n現在の人数：{count}人\nすいています！今がチャンスです💪"

    # LINE Messaging APIにリクエストを送る
    response = requests.post(
        "https://api.line.me/v2/bot/message/push",
        headers={
            "Authorization": f"Bearer {LINE_TOKEN}",
            "Content-Type": "application/json"
        },
        json={
            "to": LINE_USER_ID,
            "messages": [
                {
                    "type": "text",
                    "text": message
                }
            ]
        }
    )

    if response.status_code == 200:
        print("LINE通知を送信しました！")
    else:
        print(f"エラー：{response.status_code} {response.text}")