import smtplib
from sqlite3 import Date
import ssl
import sys

def sendMail(mail):

    smtp_address = 'smtp.gmail.com'
    smtp_port = 465
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:

        server.login(mail["email_address"], mail["email_password"])

        while True:

            try:

                server.sendmail(mail["email_address"], mail["email_receiver"], mail["message"])
                break
            except:
                print("Email \"" + mail["email_receiver"] + "\" non valide", sys.exc_info()[0])
                return -1
            

        print(" _______________________________________________________________________________________________________________________________________________________")
        print("| Expéditeur : "+mail["email_address"] + " - Destinataire : "+ mail["email_receiver"])
