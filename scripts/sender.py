import datetime
from interval import intervalRandOrNot
from sendMail import sendMail

def sender(mails,repet=1,interval=-1,approx=-1):

    dateStart = datetime.datetime.today()
    spaceTime = intervalRandOrNot(interval,approx)

    count = 0
    
    while count != repet:
        print(count)
        print(repet)
        print(count != repet)
        count += 1
        diffTmstp = datetime.datetime.today().timestamp() - dateStart.timestamp()
        
        if (diffTmstp >= spaceTime["spaceTime"]):

            mailToRemoveList = []


            for mail in mails :

                sendPending = sendMail(mail)
                logFile = '..\logs\log_' + str(datetime.datetime.today().timestamp())+ '.txt'
                
                if sendPending["error"] != -1:

                    logContent = "Mail envoye a "+ str(datetime.datetime.today())+", avec une difference approximative aleatoire de " + str(spaceTime["randomInterval"]) + " secondes."
                    logContent += "\nExpediteur : "+mail["email_address"] + " - Destinataire : "+ mail["email_receiver"]
                    dateStart = datetime.datetime.today()
                    spaceTime = intervalRandOrNot(spaceTime["interval"],spaceTime["approx"])
               
                else :
                    logContent = "Echec d'envoi de mail a "+ str(datetime.datetime.today()) + " secondes au destinataire \""+mail["email_receiver"]+"\".\nErreur : " + str(sendPending["errorText"])
                    mailToRemoveList.append(mail)

                with open(logFile, 'w') as f:
                        
                        f.write(logContent)
                        f.close()

            for mailToRemove in mailToRemoveList:

                mails.remove(mailToRemove)

                if len(mails)<1:
                    return None