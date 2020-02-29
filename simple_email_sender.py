# send emails with python using simple message template protocol
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#create message object instance
msg = MIMEMultipart()
message = "Thank you"

#setup the the paramters of the message
password = "your_password"
msg['From'] = "your_address"
msg['To'] = "to_address"
msg['Subject'] = "Subscription"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

#create the server
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

#login credentials for sending the mail
server.login(msg['From'], password)

#send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print ("Successfully sent email")
# print "successfully sent email to %s:" % (msg['To])

