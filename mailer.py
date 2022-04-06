from datetime import date
import smtplib, ssl
from sqlite3 import Date
import json, datetime, random

json_file = open("env.json")
variables = json.load(json_file)
json_file.close()

smtp_address = 'smtp.gmail.com'
smtp_port = 465

email_address = variables["sender"]
email_password = variables["password"]

email_receiver = variables["receiver"]

def sendMail():
  with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:

    server.login(email_address, email_password)

    server.sendmail(email_address, email_receiver, message)

dateStart = datetime.datetime.today()

interval = int(input("Veuillez saisir l\'intervalle de temps entre chaque envoi en minutes : \n")) # en minutes

approx = input("Si vous souhaitez que cette intervalle soit approximative (pour plus de crédibilité),\nveuillez renseigner un pourcentage d'approximation (sinon, appuyer sur Entrer) : \n")

body = 'Madame, Monsieur, \n\n Je me permet de vous recontacter afin d\'obtenir des nouvelles quant a l\'envoi de nos notes sur l\'espace MyEfrei.\nEn attente de votre retour.\n\nCordialement,\n\nLEROY DUCARDONNOY Paul'

message = 'Subject: {}\n\n{}'.format("Informations notes", body)

context = ssl.create_default_context()

stop = ""

spaceTime = 0

def intervalRandOrNot(approx):
  if approx == '':
    spaceTime = (interval * 60)
  else :
    approx = int(approx)/100
    spaceTime = (interval * 60) + (random.randint(-round(interval*approx),round(interval*approx))*60) + (random.randint(0,60))
  return spaceTime

while stop != "stop":
  spaceTime = intervalRandOrNot(approx)
  diffTmstp = datetime.datetime.today().timestamp() - dateStart.timestamp()
  if (diffTmstp >= spaceTime):
    sendMail()
    print("Mail envoyé à "+ str(datetime.datetime.today()) )
    dateStart = datetime.datetime.today()