from loadInfos import loadInfos
from asyncio.windows_events import NULL


def dataIntoMails():

        mails = []

        infos = loadInfos()

        envVariables = infos[0]

        email_address = envVariables["sender"]
        email_password = envVariables["password"]

        for index,mail in infos[1].iterrows():
                
                email_receiver = mail["Destinataires"]

                message = 'Subject: {}\n\n{}'.format(mail["Sujets"], mail["Corps"])

                newMail = {
                "email_address": email_address,
                "email_password": email_password,
                "email_receiver": email_receiver,
                "message": message}

                mails.append(newMail)

        return mails
