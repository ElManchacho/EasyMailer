from tkinter import *

def sendMailsUI():

    fenetre = Tk(screenName="EasyMailer")

    mainTitle = Label(fenetre, text="Envoyer des mails", font='bold').grid(row=0,column=1)

    dest = Entry(fenetre, textvariable=str, width=30)
    listDest = Listbox(fenetre)

    def addDest():
        newDesti = dest.get()
        if newDesti!='':
            listDest.insert("end",newDesti)
            dest.delete(0,"end")

    button1 = Button(fenetre, text ='Ajouter un destinataire',command= lambda: addDest()).grid(row=4,column=1)
    dest.grid(row=5,column=1)
    destTitle = Label(fenetre, text="Destinataires").grid(row=3,column=3)
    listDest.grid(row=5,column=3)
    
    subjectTitle = Label(fenetre, text="Objet").grid(row=5,column=4)
    subject = Entry(fenetre, textvariable=str, width=30).grid(row=6,column=4)
    message = Text(fenetre,bg="light grey",font=("black",10),height=20,width=100,padx=20,pady=20).grid(row=7,column=4)
