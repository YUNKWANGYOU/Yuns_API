import telegram
from add_chat_id import DBHandler
import json
import os

admin_file = open('/home/svcapp_su/Yuns_API/ApplicationInfo.json')
admin_dict = json.load(admin_file)
telegram_dict = admin_dict['telegram']

token = telegram_dict['api_key']
yunsbot = telegram.Bot(token = token)
updates = yunsbot.getUpdates()
for u in updates :
    print(u.message.chat_id)

yunsbot.sendMessage(chat_id='6793912847',text="Hello,World!")