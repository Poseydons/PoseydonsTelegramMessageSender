#!/usr/bin/env python3
import os
os.system("./banner.sh")
while True:
	
	token = input("\nEnter the telegram bot token : ")
	chat_id = input("\nEnter chat id : ")
	msg = input("\nEnter the message  : ")
	code = str("sudo curl -X POST 'https://api.telegram.org/bot"+ token+"/sendMessage' -d 'chat_id="+chat_id+"&text="+msg+"'")
	os.system(code)

	end = int(input("\n\n<----------------------------------------------------------------------------->\n"
					"Do you want to terminate program (1 yes, 2 no) : "))
	if end == 1:
		os.system("clear")
		quit()

	else:
		continue
