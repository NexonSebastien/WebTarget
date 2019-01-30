import csv
from os import system
from tkinter import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from tkinter import messagebox


def lectureCsv(nomFichier):
    tbl = []
    try:
        with open(nomFichier, 'r') as csvfile:
            lignes = csv.reader(csvfile, delimiter=';')
            for ligne in lignes:
                tbl.append(ligne[0])
    except IOError:
        #a = messagebox.askyesno("Warning", "Le fichier n'existe pas voulez vous le creer ?")
        #if a == True:
        with open(nomFichier, 'a+') as csvfile:
            lignes = csv.reader(csvfile, delimiter=';')
            for ligne in lignes:
                tbl.append(ligne[0])
        #else:
        #    sys.exit()

    return tbl


def importNewCsv(nomFichier):
    tbl = []
    try:
        with open(nomFichier, 'r') as csvfile:
            lignes = csv.reader(csvfile, delimiter=';')
            for ligne in lignes:
                tbl.append(ligne[0])
        return tbl
    except IOError:
        messagebox.showwarning("Warning", "Le fichier n'existe pas !!!")
        return tbl

def ecritureCsv(nomFichier,tbl):
    with open(nomFichier,'a+', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for row in tbl:
            writer.writerow([row])
def reecritureCsv(nomFichier,tbl):
    with open(nomFichier,'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for row in tbl:
            writer.writerow([row])

def verificationMail(adresseVerif):
    verif = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', adresseVerif)
    return verif

def verificationListeMail(listeAdresse,fenetreGestion):
    i = 4
    for adresse in listeAdresse:
        if verificationMail(adresse) != None:
            domaine = emailDomaine(adresse)
            if pingDomaine(domaine) != True:
                monLabel = Label(fenetreGestion, text="OK").grid(row=i, column=3)
            else:
                monLabel = Label(fenetreGestion, text="NOK").grid(row=i, column=3)
        else:
            monLabel = Label(fenetreGestion, text="NOK").grid(row=i, column=3)
        i+=1

def verificationUrl(adresseUrl):
    verif = re.match('^http://.*$|https://.*$',adresseUrl)
    return verif

def emailDomaine(email):
    if verificationMail(email) != None:
        email = email.split('@')
        email = email[1]
    else:
        email = None
    return email

def pingDomaine(domaine):
    #False Ping réussi True ping raté
    valeur = system('ping' + ' -n 1 ' + domaine)
    return (bool(valeur))

def supprimerEmailInMailList(tbl,email):
    tbl.remove(email)

def envoieMailList(fenetreEnvoie, destinataire,expediteur,objet,message):
    fenetreEnvoie.destroy()
    for row in destinataire:
        envoieMail(row,expediteur,objet,message)

def envoieMail(destinataire,expediteur,objet,message):
    expediteur = "snexonNoReply@gmail.com"
    adresseDestinaire = destinataire
    msg = MIMEMultipart()
    msg['From'] = expediteur
    msg['To'] = adresseDestinaire
    msg['Subject'] = objet
    body = message
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(expediteur, "snexon123")
    text = msg.as_string()
    server.sendmail(expediteur, adresseDestinaire, text)
    server.quit()


