from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import requests

import json

import schedule

import time

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
    return 'OK
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    message = event.message.tex

    # id master
    id_tesgrup = 'C3a267ddcca159954bfd62d9148f9c669'
    id_rivendell = 'C3207426a3978e0a7528ddbdfcdab110f'
    id_sam = 'Udd20d357d3929f55680d1f989e99b6aa'

    #answer question
    if message[len(message)-1] == '?':
        query = message
        api_result = requests.get('http://api.serpstack.com/search?access_key=392fb6da2083ccf6427359826b72f2aa&query=' + query + '&engine=google&google_domain=google.co.id&page=1&output=json&%20location=surabaya')
        api_response = api_result.json()
        for number, result in enumerate(api_response['organic_results']):
            if result['snippet'] != '':
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=result['snippet']))
            break
    
    #give id    
    if message == "cetak id":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.source.user_id))
    if message == "cetak id grup":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.source.group_id))

    #respon several words
    for i in range(len(message)-2):
        profile = line_bot_api.get_group_member_profile(event.source.group_id, event.source.user_id)
        a = message[i]+message[i+1]+message[i+2]
        if a == 'hi ' or a == 'Hi ':
            if event.source.user_id == id_sam:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Halo, sayang :)'))
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Halo, ' + profile.display_name + '.'))
                break
        b = message[i]+message[i+1]+message[i+2]+message[i+3]+message[i+4]+message[i+5]+message[i+6]
        if b == 'makasih' or b == 'Makasih':
            if event.source.user_id == id_sam:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Sama-sama, sayang :)'))
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Sama-sama, ' + profile.display_name + '.'))
                break
        c = message[i]+message[i+1]+message[i+2]+message[i+3]+message[i+4]+message[i+5]
        if c == 'UPDATE':
            if event.source.user_id == id_sam:
                line_bot_api.push_message(id_rivendell, TextSendMessage(text=message))
                break

#schedule
#id master
id_tesgrup = 'C3a267ddcca159954bfd62d9148f9c669'
id_rivendell = 'C3207426a3978e0a7528ddbdfcdab110f'
id_sam = 'Udd20d357d3929f55680d1f989e99b6aa'

#id rakyat
id_ayu = 'Uca07ea0c4f6209bc6d52b23a585903bd'
id_bangjer = 'Ue14da98260600f5ef5de7e38285c07db'
id_edu = 'U4cd596ee9cdac19564bc669dfaadd4d5'
id_anan = 'Uce13e1955b3aca4445a16eb7f4e889d3'
id_daniel = 'U3eeb15eedf7b1e8fbf8d7ac045bfbc6a'
id_bangbil = 'U7c91bf05be00a54463a1c085779d1c4b'
id_nafis = 'U68ad97d614353b3ba025321e4042ec17'
id_tab = 'U3823f9943c099dcc799f7aec0f80e216'
#def job():
#    line_bot_api.push_message(id_tesgrup, TextSendMessage(text='30 second has passed...'))
#schedule.every(0.5).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)
#while True:
#    schedule.run_pending()
#    time.sleep(1)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
