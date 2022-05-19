import imp
from tkinter import *
from tkinter import ttk
from loadInfos import loadInfos
from sender import sender

class sendMailsUIClass:
    def main():

        fenetre = Tk()
        fenetre.title("EasyMailer")

        hr1 = ttk.Separator(fenetre,orient="vertical").grid(row=1,column=1, padx=10, rowspan=5,sticky="ns")
        hr2 = ttk.Separator(fenetre,orient="vertical").grid(row=1,column=3, padx=10, rowspan=5,sticky="ns")

        mainTitle = Label(fenetre, text="Envoyer des mails", font='bold').grid(row=0,column=0)

        dest = Entry(fenetre, textvariable=str, width=30)
        listDest = Listbox(fenetre)

        def addDest():

            newDesti = dest.get()

            if newDesti!='':
                listDest.insert("end",newDesti)
                dest.delete(0,"end")

        def delDest():
            if listDest.curselection():
                listDest.delete(listDest.curselection())
        
        addDestTitle = Label(fenetre, text="Ajout de destinataire", pady=10).grid(row=1,column=0)
        button1 = Button(fenetre, text ='Ajouter',command= lambda: addDest()).grid(row=3,column=0)
        dest.grid(row=2,column=0)
        destTitle = Label(fenetre, text="Destinataires", pady=10).grid(row=1,column=2)
        listDest.grid(row=3,column=2, rowspan=1,sticky="ns")
        button1 = Button(fenetre, text ='Supprimer un destinataire',command= lambda: delDest()).grid(row=4,column=2)

        
        subjectTitle = Label(fenetre, text="Objet").grid(row=1,column=4)
        subject = Entry(fenetre, textvariable=str, width=30)
        message = Text(fenetre,bg="light grey",font=("black",10),height=20,width=100,padx=20,pady=20)

        repetTitle = Label(fenetre, text="Nombre de répétitions").grid(row=7,column=0)
        repet = Entry(fenetre, textvariable=str, width=30)   

        intervalTitle = Label(fenetre, text="Intervalle").grid(row=7,column=2)
        interval = Entry(fenetre, textvariable=str, width=30)

        approxTitle = Label(fenetre, text="Pourcentage d\'approximation").grid(row=7,column=4)
        approx = Entry(fenetre, textvariable=str, width=30)

        def warningPopUp():
            popUp = Tk()
            popUp.title("Warning !")
            popUpLabel = Label(popUp, text="Saisissez au moins un Destinataire, un Objet de mail et un message", pady=10).grid(row=1,column=0, columnspan=3)
            popUpButton1 = Button(popUp, text ='Ok',command= lambda: popUp.destroy())
            return popUpButton1.grid(row=2,column=1)

        def sendNewMail():
            emailList = []
            arrayDist = listDest.get('@1,0', 'end')
            if arrayDist == ():
                return warningPopUp()
            infos = loadInfos()[0]
            objet = subject.get()
            if objet == "":
                return warningPopUp()
            objet = objet.replace('é','e')
            objet = objet.replace('è','e')
            objet = objet.replace('ê','e')
            
            corpsMail = message.get("1.0","end")
            if corpsMail == "":
                return warningPopUp()
            corpsMail = corpsMail.replace('é','e')
            corpsMail = corpsMail.replace('è','e')
            corpsMail = corpsMail.replace('ê','e')
            for destinataire in arrayDist:
                email = {
                                "email_address": infos["sender"],
                                "email_password": infos["password"],
                                "email_receiver": destinataire,
                                "message": 'Subject: {}\n\n{}'.format(objet,corpsMail)}
                emailList.append(email)
            sender(emailList, repet.get(), int(interval.get()),int(approx.get()))
            fenetre.destroy()
        subject.grid(row=1,column=5)
        message.grid(row=2,column=4,columnspan=2, rowspan=3)
        repet.grid(row=7,column=1)
        interval.grid(row=7,column=3)
        approx.grid(row=7,column=5)
        hr3 = ttk.Separator(fenetre,orient="horizontal").grid(pady=10, row=6,column=0, columnspan=6,sticky="ws")
        
        sendButton = Button(fenetre, text ='Envoyer mail',command= lambda: sendNewMail(),width=50).grid(row=8,column=3,columnspan=2)
