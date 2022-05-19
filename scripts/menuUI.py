from tkinter import *
from checkLogsUI import *
from templatesUI import *
from sendMailsUI import *

def menuUi():

  fenetre = Tk()
  fenetre.title("EasyMailer")

  appHeader = LabelFrame(fenetre, text="Menu", padx=20, pady=20)
  appHeader.pack(fill="both", expand="yes")
  mainTitle = Label(appHeader, text="Bienvenue sur EasyMailer !", font='bold').pack(side=TOP, padx=0, pady=0)
  
  def callPage(page):

    page = page.main()
    
  button1 = Button(appHeader, text ='Envoyer des mails', width=30,command=lambda:callPage(sendMailsUIClass)).pack(side='top', padx=5, pady=5)
  button2 = Button(appHeader, text ='Visualiser les patrons enregistrés', width=30, command=lambda:callPage(templatesUIClass)).pack(side='top', padx=5, pady=5)
  button3 = Button(appHeader, text ='Consulter les logs', width=30, command=lambda:callPage(checkLogsUIClass)).pack(side='top', padx=5, pady=5)

  fenetre.mainloop()