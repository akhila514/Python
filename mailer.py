import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

address_book = ['abc@domain.com', 'bcd@domain.com']
# domain= your internal mailer system
msg = MIMEMultipart()    
sender = 'name@domain.com'
subject = "My subject"
body = "This is my email body"

msg['From'] = sender
msg['To'] = ','.join(address_book)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))
text=msg.as_string()
#print text
# Send the message via our SMTP server
s = smtplib.SMTP('mail.domain.com')
s.sendmail(sender,address_book, text)
s.quit()   
