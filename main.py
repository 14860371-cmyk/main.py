import requests
from bs4 import BeautifulSoup

# Telegram 資訊
BOT_TOKEN = "8955243724:AAGBTVZTwif1deDCdz0mqN_UDdkhjq_oiyu"
CHAT_ID = "8977904332"

# 股票代號
stock_id = "2330"

# Yahoo 股市網址
url = f"https://tw.stock.yahoo.com/quote/{stock_id}"

# 發送請求
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

# 解析 HTML
soup = BeautifulSoup(response.text, "html.parser")

# 抓股價
price = soup.find("span", class_="Fz(32px)").text

# 訊息內容
message = f"台積電({stock_id}) 即時股價：{price}"

# Telegram API
telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

payload = {
    "chat_id": CHAT_ID,
    "text": message
}

# 發送 Telegram 通知
requests.post(telegram_url, data=payload)

print("通知已發送")
