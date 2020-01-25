import time 
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
import xlrd
address_book = []
birthday_list = []
birthdayname_list =[]
birthday_Name = ""
birthday_mail = ""
#PPath for the Birthday List
#Consists of 1st Column : DOB
#2nd Column : Name ;3rd Column : Mail ID
birthdayFile = '/BirthdayMail/BirthdayList.xlsx'
fileName = open(birthdayFile, 'r')
#Date Format
today = time.strftime('%m%d') 
flag = 0

book = xlrd.open_workbook(birthdayFile , 'r')
first_sheet = book.sheet_by_index(0)
cols = first_sheet.ncols
rows = first_sheet.nrows


n = 0
while (n < rows):
    
    Content = first_sheet.cell(n,0).value
    #print(Content)
    #Comparing Today's date with DOB
    if today in Content:
        flag =1
        birthday_Name = first_sheet.cell(n,1).value
        birthday_mail = first_sheet.cell(n,2).value
        #print(birthday_mail)
        #Appending the list of mails and names to list
        birthday_list.append(birthday_mail)
        birthday_list.append("PortalTeam@domain.com")
        birthdayname_list.append(birthday_Name)

    n +=1

             
if flag == 0:
    os.system('notify-send "No Birthdays Today!"') 


#print(birthday_list)
#print(birthday_list[0])
address_book = birthday_list
print(';'.join(address_book))
birthday_names = ','.join(birthdayname_list)
print(birthday_names)
msg = MIMEMultipart()    
sender = 'sender@domain.com'
subject = "Happy Birthday"
msg['From'] = sender
#if we want to send a mail to more than one person then we need do add ";"
msg['To'] = ';'.join(address_book)
msg['Subject'] = subject
body = MIMEText(""" <p>Dear """  + birthday_names + """ <br><p style = "font-family:"Comic Sans MS";color:blue"><blink>Happy Birthday!!!<br><br>Wishing you a wonderful year of good health,happiness and success!!</br></blink></p><br><img src = "C:/Users/1206439/Desktop/birthday.jpg" alt= "Birthday" width="350"></img></p><p>Best Regards<br>Indigo Team""", _subtype='html')
msg.attach(body)
text=msg.as_string()
s = smtplib.SMTP('mail.domain.com')
s.sendmail(sender,address_book, text)
s.quit() 

