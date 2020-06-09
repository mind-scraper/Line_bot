from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi("BBYC9KC7q284mUq/bdvd4XusQaHbZTW9R4qVHz1nco0On3cuVSYhjqNlqp+wOapXmOq6zwTLUTVJiJv8tVaGU8GSxssPg/Rgbi5jMyW0AQs7NuoBN6Mz59K62TM5op41lJTLVK8Tegkzql5LN/qP1gdB04t89/1O/w1cDnyilFU=")
# Channel Secret
handler = WebhookHandler("83d434d9ffe175f89453670ca91674cc")

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text

# Simple echo
#    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))
	
# Replying with spesific message
    if message == "Hi":
        profile = line_bot_api.get_group_member_profile(event.source.group_id, event.source.user_id)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Halo, ' + profile.display_name))	
        
    if message == "cetak id":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.source.user_id))

    if message == "cetak id grup":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.source.group_id))

#    profile = line_bot_api.get_group_member_profile("C3a267ddcca159954bfd62d9148f9c669", "Udd20d357d3929f55680d1f989e99b6aa")

#    if message == "siapa saya?":
#        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=profile.display_name))

    for i in range(len(message)-1):
        a = message[i]+message[i+1]+message[i+2]+message[i+3]+message[i+4]+message[i+5]+message[i+6]
        if a == 'makasih' or a == 'Makasih':
            if event.source.user_id == 'Udd20d357d3929f55680d1f989e99b6aa':
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Sama-sama, sayang.')
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Sama-sama, ' + profile.display_name) + '.')
                break        
    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
