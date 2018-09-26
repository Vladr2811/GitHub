import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#Initial Data
	
user = input("Please enter your email: ")
password = input("Please enter your password: ")

def SendMail(to_mail,msgBody,Subject="Python Email"):

	fromaddr = user
	toaddr = to_mail
	body = msgBody
		
	#Creating the server
	
	server = smtplib.SMTP('smtp.gmail.com', 587)
	
    #Creating the mail
	
	#Splitting the msg in parts
	msg = MIMEMultipart()

	#Setting each part
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = Subject

	#Attaching the body to the msg
	msg.attach(MIMEText(body,'plain'))


	server.ehlo()
	server.starttls()
	server.ehlo()

	#Log in into server
	server.login(user,password)

	#Creating the text variable
	text = msg.as_string()


	#Sending the mail
	server.sendmail(fromaddr,toaddr,text)



sendText = input("Input the message: ")

try:
	sendSubject = input("Input the Subject (Optional): ")
	SendMail("redknife2811@gmail.com", sendText, sendSubject)
except:
	SendMail("redknife2811@gmail.com", sendText)

