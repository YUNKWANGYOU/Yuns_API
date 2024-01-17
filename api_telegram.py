import telegram
from add_chat_id import DBHandler


token = '6865217637:AAFowKNL8VfhWt5OcCt-XrJQR-rjI712cxc'
yunsbot = telegram.Bot(token = token)
updates = yunsbot.getUpdates()
for u in updates :
    print(u.message.chat_id)

yunsbot.sendMessage(chat_id='6793912847',text="Hello,World!")