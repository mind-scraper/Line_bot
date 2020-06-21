from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from apscheduler.schedulers.background import BackgroundScheduler

import requests

import json

import random
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

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    message = event.message.text
    profile = line_bot_api.get_group_member_profile(event.source.group_id, event.source.user_id)

    #answer question
    if message[len(message)-1] == '?':
        query = message
        api_result = requests.get('http://api.serpstack.com/search?access_key=392fb6da2083ccf6427359826b72f2aa&query=' + query + '&engine=google&google_domain=google.co.id&page=1&output=json&%20location=surabaya&safe=1')
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

    keyword0 = ["UPDATE!!!"]
    keyword1 = ["hi ", "hi,", "Hi ", "Hi,", "Hallo", "hallo", "Halo", "halo", "Selamat","selamat","Salam","salam"]
    respond1 = ["Semoga harimu menyenangkan.", "Sudah mandi belum?", "Jangan lupa makan ya.", "Semangat ya." , "Andai waktu itu Newton duduk di bawah pohon kelapa...", "Ilmuan yang belajar fisika disebut fisikawan.", "Cahaya dari bumi hanya butuh 1,255 detik untuk mencapai bulan, selama kamu membaca tulisan ini.", "Physics is, hopefully, simple. Physicists are not. -Edward Teller-", "Curiosity adalah robot penjelajah Mars milik NASA. Tak heran tidak ada kucing di Mars.", "It doesn't matter how beautiful your theory is, it doesn't matter how smart you are. If it doesn't agree with experiment, it's wrong. In that simple statement is the key to science.-Richard Feynman-","It's Okay to say I don't know! There's no shame in that! The only shame is to pretend that we know everything.-Richard Feynman-","Be yourself; everyone else is already taken.-Oscar Wilde-","It would be better for the true physics if there were no mathematicians on earth. -Daniel Bernoulli-", "Nature doesn't really care about your beliefs.-Richard Feynman-", "Membacalah setiap hari.", "Jangan berhenti belajar.", "Bertanyalah.", "Tidak apa-apa melakukan kesalahan baru.", "Fisikawan tidak suka mencari-cari masalah. Masalah mereka sudah cukup banyak.", "All science is either physics or stamp collecting.-Ernest Rutherford-", "Hukum gravitasi tidak berlaku terhadap orang yang sedang jatuh cinta.-Albert Einstein-" ]
    keyword2 = ["Terima kasih", "terima kasih", "thank", "Thank", "Mksh", "mksh", "Thx", "makasih", "Arigato", "arigato"]
    respond2 = ["Sama-sama, ", "You're welcome, ", "No problem, ", "Halah santai, ", "It's my pleasure, ", "I know you'd do the same for me, ", "Don't mention it, ", "Anytime, ", "Sure, ", "It was nothing, ", "I'm happy to help, ", "Senang bisa membantumu, ", "Langsung transfer aja, ", "아니에요, ", "どういたしまして, ", "Sami-sami, "]

    #give specific response
    for i in range(len(keyword0)):
        if keyword0[i] in message:
            if event.source.user_id == id_sam:
                line_bot_api.push_message(id_rivendell, TextSendMessage(text=message))
            break

    for i in range(len(keyword1)):
        if keyword1[i] in message:
            if event.source.user_id == id_sam:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Halo, sayang :) " + respond1[random.randrange(len(respond1))]))
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Halo, " + profile.display_name + ". " + respond1[random.randrange(len(respond1))]))
            break

    for i in range(len(keyword2)):
        if keyword2[i] in message:
            if event.source.user_id == id_sam:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=respond2[random.randrange(len(respond2))] + "sayang :)"))
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text=respond2[random.randrange(len(respond2))] + profile.display_name + '.'))
            break
    
#schedule
def nama(id):
    profile = line_bot_api.get_group_member_profile(id_rivendell, id)
    return profile.display_name

piket_senin = nama(id_bangjer) + ", " + nama(id_edu) + "."
piket_selasa = nama(id_anan) + "."
piket_rabu = nama(id_nafis) + "."
piket_kamis = nama(id_daniel) + ", " + nama(id_ayu) + "."
piket_jumat = nama(id_bangbil) + ", " + nama(id_tab) + "."

sched = BackgroundScheduler()

@sched.scheduled_job('cron', day_of_week='mon', hour=15)
def scheduled_job():
    line_bot_api.push_message(id_rivendell, TextSendMessage(text="Selamat malam, Rivendellian. Petugas piket besok adalah " + piket_selasa + "Kalian segera tidur biar bisa bangun pagi ya... :)"))
    scheduler.resume()

@sched.scheduled_job('cron', day_of_week='tue', hour=15)
def scheduled_job():
    line_bot_api.push_message(id_rivendell, TextSendMessage(text="Selamat malam, Rivendellian. Petugas piket besok adalah " + piket_rabu + "Kalian segera tidur biar bisa bangun pagi ya... :)"))
    scheduler.resume()

@sched.scheduled_job('cron', day_of_week='wed', hour=15)
def scheduled_job():
    line_bot_api.push_message(id_rivendell, TextSendMessage(text="Selamat malam, Rivendellian. Petugas piket besok adalah " + piket_kamis + "Kalian segera tidur biar bisa bangun pagi ya... :)"))
    scheduler.resume()

@sched.scheduled_job('cron', day_of_week='thu', hour=15)
def scheduled_job():
    line_bot_api.push_message(id_rivendell, TextSendMessage(text="Selamat malam, Rivendellian. Petugas piket besok adalah " + piket_jumat + "Kalian segera tidur biar bisa bangun pagi ya... :)"))
    scheduler.resume()

@sched.scheduled_job('cron', day_of_week='fri', hour=15)
def scheduled_job():
    line_bot_api.push_message(id_rivendell, TextSendMessage(text="Selamat malam, Rivendellian. Besok tidak ada piket. Kalian bisa begadang sampai pagi."))
    scheduler.resume()

@sched.scheduled_job('cron', day_of_week='sat', hour=15)
def scheduled_job():
    line_bot_api.push_message(id_rivendell, TextSendMessage(text="Selamat malam, Rivendellian. Besok tidak ada piket. Kalian bisa begadang sampai pagi."))
    scheduler.resume()

@sched.scheduled_job('cron', day_of_week='sun', hour=15)
def scheduled_job():
    line_bot_api.push_message(id_rivendell, TextSendMessage(text="Selamat malam, Rivendellian. Petugas piket besok adalah " + piket_senin + "Kalian segera tidur biar bisa bangun pagi ya... :)"))
    scheduler.resume()

sched.start()

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
