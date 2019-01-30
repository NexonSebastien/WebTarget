from tkinter import *
import fonctionCommuneGestion

def fenetreEnvoie(fenetreMail, expediteur,objet,message,tbl):
    fenetreMail.destroy()
    fenetreEnvoie = Tk()
    fenetreEnvoie.title("Fenetre Envoie")
    lblEmail = Label(fenetreEnvoie, text="Email :").pack()
    entryEmail = Entry(fenetreEnvoie, width=30)
    entryEmail.pack()
    bouton = Button(fenetreEnvoie, text="Envoi", command=lambda: fonctionCommuneGestion.envoieMail(entryEmail.get(), expediteur, objet, message)).pack()
    boutonAll = Button(fenetreEnvoie, text="Envoi à toute la liste", command=lambda: fonctionCommuneGestion.envoieMailList(fenetreEnvoie, tbl, expediteur, objet, message)).pack()