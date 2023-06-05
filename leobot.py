import time
from pyrogram import Client, filters

api_id = 'your_api_id'
api_hash = 'your_api_hash'

app = Client("bot", api_id = api_id, api_hash = api_hash)

names = ['names that bot WILL like']
description = ['words that bot WILL NOT like']
fid = 'id of a chat to forward liked profiles'

@app.on_message(filters.chat(-1001758400648))
def sorting(client, message):
	timing=time.localtime(time.time())
	if timing.tm_hour > 8:
		if timing.tm_hour < 23:
			mid = message.chat.id
			ms = message.id
			source_text = message.caption
			if source_text:
				text1 = source_text.lower().split(',',1)
				text2 = source_text.lower().split('–', 1)
				if text1[0] in names:
					try:
						if any(i in text2[1] for i in description):
							app.send_message(mid, '👎')
						else:
							app.send_message(mid, '👍')
							app.forward_messages(fid, -1001758400648, ms)
					except IndexError:
						app.send_message(mid, '👎' )
				else:
					app.send_message(mid, '👎' )
			elif message.text:
			 	app.send_message(mid, 'Продолжить просмотр анкет')
app.run()


