from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def SendMsg(message,user,password,to,subject):
 
	# create message object instance
	msg = MIMEMultipart()
 
	# setup the parameters of the message
	
	msg['From'] = user
	msg['To'] = to
	msg['Subject'] = subject
 
	# add in the message body
	msg.attach(MIMEText(message, 'plain'))
 
	#create server
	server = smtplib.SMTP('smtp.gmail.com: 587')
 
	server.starttls()
 
	# Login Credentials for sending the mail
	server.login(msg['From'], password)
 
 
	# send the message via the server.
	server.sendmail(msg['From'], msg['To'], msg.as_string())
 
	server.quit()
 

def SendIp(): 
	from urllib2 import urlopen
	my_ip = urlopen('http://ip.42.pl/raw').read()
	SendMsg(("Ip RPI: " + my_ip),"vladgoia2811@gmail.com","kernelpanic1999","vladgoia2811@yahoo.com","IP RPI")
