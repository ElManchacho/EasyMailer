import datetime
from interval import intervalRandOrNot
from sendMail import sendMail

def sender(mails):

    dateStart = datetime.datetime.today()
    spaceTime = intervalRandOrNot()
    stop = ""

    while stop != "stop":

        diffTmstp = datetime.datetime.today().timestamp() - dateStart.timestamp()
        
        if (diffTmstp >= spaceTime["spaceTime"]):
            
            for mail in mails :
                
                sendPending = sendMail(mail)
                if sendPending != -1:
                    print("| Mail envoyé à "+ str(datetime.datetime.today())+", avec une différence approximative aléatoire de " + str(spaceTime["randomInterval"]) + " secondes.")
                    print("|_______________________________________________________________________________________________________________________________________________________")
                    dateStart = datetime.datetime.today()
                    spaceTime = intervalRandOrNot(spaceTime["interval"],spaceTime["approx"])