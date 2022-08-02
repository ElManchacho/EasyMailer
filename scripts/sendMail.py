import smtplib
from sqlite3 import Date
import ssl
import sys
from loadInfos import loadInfos
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendMail(mail):
    smtp_address = 'smtp.gmail.com'
    smtp_port = 465
    context = ssl.create_default_context()
    

    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
        
        server.login(mail["email_address"], mail["email_password"])

        while True:

            try:
                print(mail["email_address"], mail["email_receiver"], mail["message"])
                server.sendmail(mail["email_address"], mail["email_receiver"], mail["message"])
                break

            except:
                errorData = {"error":-1,"errorText":sys.exc_info()}
                print(errorData)
                return errorData
        
    return {"error":0,"errorText":"none"}