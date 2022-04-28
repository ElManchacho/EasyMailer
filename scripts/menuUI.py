from tkinter import *
from checkLogsUI import checkLogsUI
from templatesUI import templatesUI
from sendMailsUI import sendMailsUI

def menuUi():

  fenetre = Tk(screenName="EasyMailer")

  appHeader = LabelFrame(fenetre, text="Menu", padx=20, pady=20)
  appHeader.pack(fill="both", expand="yes")
  mainTitle = Label(appHeader, text="Bienvenue sur EasyMailer !", font='bold').pack(side=TOP, padx=0, pady=0)

  # canvas = Canvas(appHeader, width=250, height=50, bg='ivory').pack(side='left', padx=5, pady=5)
  button1 = Button(appHeader, text ='Envoyer des mails', width=30,command=sendMailsUI).pack(side='top', padx=5, pady=5)
  button2 = Button(appHeader, text ='Visualiser les patrons enregistrés', width=30, command=templatesUI).pack(side='top', padx=5, pady=5)
  button2 = Button(appHeader, text ='Consulter les logs', width=30, command=checkLogsUI).pack(side='top', padx=5, pady=5)

  fenetre.mainloop()