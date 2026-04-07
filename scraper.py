from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

# .envファイルを読み込む
load_dotenv()
URL = os.getenv("GYM_URL")

def get_congestion():
    with sync_playwright() as p:
        # ブラウザを起動（headless=Falseにすると画面が見える）
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # ページを開く
        page.goto(URL)
        
        # JavaScriptの読み込みを待つ
        page.wait_for_selector("#cong-list dd.info_cong span")
        
        # 人数を取得
        span = page.query_selector("#cong-list dd.info_cong span")
        count = int(span.inner_text().strip())
        
        print(f"現在の人数：{count}人")
        
        browser.close()
        return count

get_congestion()