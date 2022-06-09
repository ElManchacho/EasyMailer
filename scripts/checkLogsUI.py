import json
from tkinter import *
from os import listdir
from os.path import isfile, join

class checkLogsUIClass:
    def main():

        def strigyfyElems(elements):
            strigified = ""
            for element in elements:
                strigified += element + " : " + elements[element] + " "
            # virer le dernier espace
            return strigified

        logsPath = '../logs/'

        fenetre = Tk()

        fenetre.title("EasyMailer")

        mainTitle = Label(fenetre, text="Logs d'activité EasyMailer", font='bold').grid(row=0,column=1)

        listLogs = Listbox(fenetre)

        fileslist = [f for f in listdir(logsPath) if isfile(join(logsPath, f))]

        for file in fileslist:
            json_file = open(logsPath + file)
            variables = json.load(json_file)["mail"]
            json_file.close()
            listLogs.insert("end",strigyfyElems(variables))

        listLogs.grid(row=2,column=1)

        def closeBeforeOpen():
                fenetre.destroy()
