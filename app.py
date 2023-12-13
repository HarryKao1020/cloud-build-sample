import os

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from web_crawler import simple_web_crawler, headless_web_crawler, beautifulsoup_web_crawler


app = Flask(__name__)


# 替換成你的 Channel Access Token 和 Channel Secret
# CHANNEL_ACCESS_TOKEN='gIS4eSAOyETZv18tiyNcT4ZZ6274L9UuhLjSowpDjuqYf4dFCNB37+saXJfI1FSr85uiKqqrhteAxVCD3Yjalx/4zC3rshDGfm1/xZXIZmf4pFY2HYnRLs3LqbNiJAmBXAIOwCqSEZTqqnzNa8mfkwdB04t89/1O/w1cDnyilFU='
# CHANNEL_SECRET='04279870980e7421fbf1b27cc03165c2'

# for local test
# line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
# handler = WebhookHandler(CHANNEL_SECRET)

# for cloud run test
line_bot_api = LineBotApi(os.environ.get('CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.environ.get('CHANNEL_SECRET'))


# 在應用程式啟動時主動發送歡迎訊息給所有已關注的使用者
# def push_welcome_message_to_all_users():
#     try:
#         # 主動發送歡迎訊息
#         line_bot_api.broadcast(
#             TextSendMessage(text="哈囉！歡迎使用 Line Bot！")
#         )
#     except LineBotApiError as e:
#         print(f"推送歡迎訊息失敗，錯誤訊息：{e}")

# # 在應用程式啟動時執行初始化推送
# push_welcome_message_to_all_users()


line_bot_api.push_message('U2032ae75254e026706d91546f58b9af1', TextSendMessage(text='你可以開始了'))
# 綁定 Line Bot 的 Webhook URL


@app.route("/hello")
def sayhi():
    return "Hello world"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_text = event.message.text
    reply_text = f'你說的是：{user_text}'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, port=port, host='0.0.0.0')
    simple_web_crawler()  # 執行基本爬蟲程式
    headless_web_crawler()  # 執行 headless 爬蟲程式
    beautifulsoup_web_crawler()  # 執行 BeautifulSoup 爬蟲程式




