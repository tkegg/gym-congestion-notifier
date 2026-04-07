from scraper import get_congestion
from notifier import send_line_message
from datetime import datetime, timezone, timedelta

# 日本時間に変換
JST = timezone(timedelta(hours=9))

def main():
    now = datetime.now(JST)
    hour = now.hour

    print(f"現在時刻（日本時間）：{now.strftime('%Y-%m-%d %H:%M')}")

    # 時間帯ごとの設定
    if 8 <= hour < 17:
        threshold = 3
    elif 17 <= hour or hour < 1:
        threshold = 4
    else:
        print(f"現在{hour}時。通知時間帯外のため終了します")
        return

    # 現在の人数を取得
    count = get_congestion()

    if count is None:
        print("人数の取得に失敗しました")
        return

    # 閾値以下なら通知
    if count <= threshold:
        send_line_message(count)
    else:
        print(f"現在{count}人。閾値({threshold}人)を超えています。通知しません。")

main()