import datetime
import json
from interval import intervalRandOrNot
from sendMail import sendMail

def sender(mails,repet=1,interval=-1,approx=-1):
    repet = int(repet)
    dateStart = datetime.datetime.today()
    spaceTime = intervalRandOrNot(interval,approx)

    count = 0

    stop = False
    
    while stop != True :
        diffTmstp = datetime.datetime.today().timestamp() - dateStart.timestamp()
        
        if (diffTmstp >= spaceTime["spaceTime"]):

            mailToRemoveList = []


            for mail in mails :

                sendPending = sendMail(mail)
                logFile = '..\logs\log_' + str(datetime.datetime.today().timestamp())+ '.json'
                
                if sendPending["error"] != -1:

                    logContent = {
                        "mail" :{
                            "sendTime":str(datetime.datetime.today()),
                            "diffTime":str(spaceTime["randomInterval"]),
                            "sender":mail["email_address"],
                            "receiver": mail["email_receiver"]
                            }
                        }
                    dateStart = datetime.datetime.today()
                    spaceTime = intervalRandOrNot(spaceTime["interval"],spaceTime["approx"])
               
                else :
                    
                    logContent = {
                        "error" : {
                            "errorTime":str(datetime.datetime.today()),
                            "errorMsg":str(sendPending["errorText"]),
                            "sender":mail["email_address"],
                            "receiver": mail["email_receiver"]
                        }
                    }
                    mailToRemoveList.append(mail)

                f = open(logFile, 'w')
                json.dump(logContent,f)
                f.close()

            for mailToRemove in mailToRemoveList:

                mails.remove(mailToRemove)

                if len(mails)<1:
                    return None
            count += 1
            if count == repet:
                stop = True