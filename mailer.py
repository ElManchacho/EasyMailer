import smtplib, ssl
import json

json_file = open("env.json")
variables = json.load(json_file)
json_file.close()

smtp_address = 'smtp.gmail.com'
smtp_port = 465

email_address = variables["sender"]
email_password = variables["password"]

email_receiver = variables["receiver"]

body = 'Madame, Monsieur, \n\n Je me permet de vous recontacter afin d\'obtenir des nouvelles quant a l\'envoi de nos notes sur l\'espace MyEfrei.\nEn attente de votre retour.\n\nCordialement,\n\nLEROY DUCARDONNOY Paul'

message = 'Subject: {}\n\n{}'.format("Informations notes", body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:

  server.login(email_address, email_password)

  server.sendmail(email_address, email_receiver, message)
