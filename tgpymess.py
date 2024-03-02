from requests import get
class BOT:
	def send_message(BotToken,chat_id,message):
		api = f"https://api.telegram.org/bot{BotToken}/sendMessage?chat_id={chat_id}&text={message}"
		requested = get(
		api
		)
		if requested.status_code == 200:
			print(
			"Message has been sent"
			)
		else:pass
	def getme(BotToken):
		api = f"https://api.telegram.org/bot{BotToken}/getMe"
		req_u = get(
		api
		).text
		print(
		req_u
		)