from tkinter import *

def sendMailsUI():

    fenetre = Tk(screenName="EasyMailer")

    appHeader = LabelFrame(fenetre, text="Mails", padx=20, pady=20)
    appHeader.pack(fill="both", expand="yes")

    mainTitle = Label(appHeader, text="Envoyer des mails", font='bold').pack(side=TOP, padx=0, pady=0)

    destTitle = Label(appHeader, text="Destinataires").pack(side='top', padx=2, pady=8)
    dest = Entry(appHeader, textvariable=str, width=30)
    
    listDest = Listbox(appHeader)

    listOfCompanies = [[1, ''], [2, '-'], [3, '@ASK TRAINING PTE. LTD.'], [4, 'AAIS'], [5, 'Ademco'], [6, 'Anacle']]

    def addDest():
        listDest.insert("end",dest.get())
        dest.delete(0,"end")

    button1 = Button(appHeader, text ='Ajouter un destinataire', width=30,command= lambda: addDest()).pack(side='top', padx=5, pady=5)
    listDest.pack(side='top', padx=0, pady=2)
    dest.pack(side='top',padx=2, pady=7)
    subjectTitle = Label(appHeader, text="Objet").pack(side='top', padx=2, pady=8)
    subject = Entry(appHeader, textvariable=str, width=30).pack(side='top',padx=2, pady=7)
    message = Text(appHeader,bg="light grey",font=("black",10),height=20,width=100,padx=20,pady=20).pack(side='bottom',padx=2, pady=10)
