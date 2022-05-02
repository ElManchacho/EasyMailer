import imp
from tkinter import *
from tkinter import ttk
from loadInfos import loadInfos
from sender import sender

def sendMailsUI():

    fenetre = Tk(screenName="EasyMailer")

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

    addDestTitle = Label(fenetre, text="Ajout de destinataire", pady=10).grid(row=1,column=0)
    button1 = Button(fenetre, text ='Ajouter',command= lambda: addDest()).grid(row=3,column=0)
    dest.grid(row=2,column=0)
    destTitle = Label(fenetre, text="Destinataires", pady=10).grid(row=1,column=2)
    listDest.grid(row=3,column=2, rowspan=1,sticky="ns")


    
    subjectTitle = Label(fenetre, text="Objet").grid(row=1,column=4)
    subject = Entry(fenetre, textvariable=str, width=30).grid(row=1,column=5)
    message = Text(fenetre,bg="light grey",font=("black",10),height=20,width=100,padx=20,pady=20)

    def sendNewMail():
        emailList= []
        infos = loadInfos()[0]
        for destinataire in listDest.get('@1,0', 'end'):
            email = {
                            "email_address": infos["sender"],
                            "email_password": infos["password"],
                            "email_receiver": destinataire,
                            "message": message.get("1.0","end")}
            emailList.append(email)
        sender(emailList)

    message.grid(row=2,column=4,columnspan=2, rowspan=3)

    sendButton = Button(fenetre, text ='Envoyer mail',command= lambda: sendNewMail(),width=30).grid(row=6,column=2,rowspan=2)
