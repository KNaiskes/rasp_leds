import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from keys import * # I keep my personal information in a separate file
from datetime import datetime 
import os.path
from os import remove

def sendNewMail():
	#define your personal information below or in a separate file as I did
	#user_email =""
	#passw = ""
	#sendTo = ""
	currentTime = datetime.now().time()
	currentTime = currentTime.replace(microsecond = 0)
	sub = "New alarm"
	image = "image.jpg"
	message = MIMEMultipart()
	message["Subject"] = sub
	message["From"] = user_email
	message["To"] = sendTo
	message.premble = "alert"
	message.attach(MIMEText("Alarm took place at: "+str(currentTime),"plain"))

	# If camera won't work for any reason, send email without the image
	if(os.path.isfile(image)):
		fp = open(image,"rb")
		image = MIMEImage(fp.read())
		fp.close()
		message.attach(image)


	sendIt = smtplib.SMTP("smtp.gmail.com",587)
	sendIt.ehlo()
	sendIt.starttls()
	sendIt.ehlo()
	sendIt.login(user_email,passw)
	sendIt.send_message(message)
	sendIt.quit()

	# remove image after sending it so it will not be send again if camera
	# cannot take a new screenshot

	try:
		remove("image.jpg")
	except OSError:
		pass
