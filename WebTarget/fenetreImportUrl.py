from tkinter import *
import fonctionCommuneGestion
import fenetreGestion
from bs4 import BeautifulSoup
import requests

def crawlerUrl(url, nomFichier,maFenetreGestion):
    code = requests.get(url)
    plain = code.text
    s = BeautifulSoup(plain, "html.parser")
    tblEmail = []
    for row in s.findAll('a'):
        mailto = row.get('href')
        if mailto.__contains__('mailto'):
            email = mailto.split(':')[1]
            if fonctionCommuneGestion.verificationMail(email) != None:
                tblEmail.append(email)
    fonctionCommuneGestion.ecritureCsv(nomFichier, tblEmail)
    fenetreGestion.reload(maFenetreGestion, nomFichier)

def fenetreImportUrl(nomFichier,maFenetreGestion):
    fenetreImportUrl = Tk()
    fenetreImportUrl.title("Import URL")
    lblImportUrl = Label(fenetreImportUrl, text="Import URL").pack()
    entryUrl = Entry(fenetreImportUrl, width=30)
    entryUrl.pack()
    bouttonValider = Button(fenetreImportUrl, text="OK", command=lambda: crawlerUrl(entryUrl.get(), nomFichier,maFenetreGestion)).pack()
    fenetreImportUrl.mainloop()