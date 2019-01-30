from tkinter import *
import fenetreEnvoie
def fenetreMail(tbl):
    fenetreMail = Tk()
    fenetreMail.title("Mail")
    lblExpediteur = Label(fenetreMail, text="Expediteur").pack()
    entryExpediteur = Entry(fenetreMail, width=30)
    entryExpediteur.pack()
    lblObjet = Label(fenetreMail, text="Objet").pack()
    entryObjet = Entry(fenetreMail, width=30)
    entryObjet.pack()
    lblMessage = Label(fenetreMail, text="Message").pack()
    entryMessage = Entry(fenetreMail, width=90)
    entryMessage.pack()
    bouttonValider = Button(fenetreMail, text="OK",command=lambda: fenetreEnvoie.fenetreEnvoie(fenetreMail, entryExpediteur.get(),entryObjet.get(),entryMessage.get(),tbl)).pack()
    fenetreMail.mainloop()