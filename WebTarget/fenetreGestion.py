from tkinter import *
import fonctionCommuneGestion
import fenetreImportCsv
import fenetreImportUrl
import fenetreMail

def reload(maFenetre,nomFichier):
    maFenetre.destroy()
    fenetreGestion(0, 0, nomFichier)

def fenetreGestion(fenetreAccueil,entryCsv,nomFichier):
    def supprimerAdresse(num,label,b,nomFichier):
        tbl.pop(num)
        fonctionCommuneGestion.reecritureCsv(nomFichier,tbl)
        reload(fenetreGestion, nomFichier)

    def supprimerDoublon(tbl, nomFichier):
        tbl = list(set(tbl))
        fonctionCommuneGestion.reecritureCsv(nomFichier, tbl)
        reload(fenetreGestion, nomFichier)

    fenetreGestion = Tk()
    fenetreGestion.title("Gestion")
    if entryCsv != 0:
        nomFichier = "data/"+entryCsv.get() + ".csv"
    if fenetreAccueil != 0:
        fenetreAccueil.destroy()
    tbl = fonctionCommuneGestion.lectureCsv(nomFichier)

    listBoxMail = Listbox(fenetreGestion)
    #Boutons
    #tbl = supprimerDoublon(tbl)
    bouttonDedoublonage = Button(fenetreGestion, text="Dedoublonner", command=lambda: supprimerDoublon(fonctionCommuneGestion.lectureCsv(nomFichier),nomFichier)).grid(row=0, column=1)
    bouttonVerification = Button(fenetreGestion, text="Verification",command=lambda: fonctionCommuneGestion.verificationListeMail(tbl,fenetreGestion)).grid(row=1, column=1)
    bouttonImportCsv = Button(fenetreGestion, text="Import CSV", command=lambda: fenetreImportCsv.fenetreImportCsv(nomFichier,fenetreGestion)).grid(row=2, column=1)
    bouttonImportUrl = Button(fenetreGestion, text="Import URL", command=lambda: fenetreImportUrl.fenetreImportUrl(nomFichier,fenetreGestion)).grid(row=3, column=1)
    #bouttonSupprimerAdresse = Button(fenetreGestion, text="X", command=lambda: fonctionCommuneGestion.supprimerAdresse(vars)).pack()

    #Lecture CSV
    i = 0
    for row in tbl:
        #listBoxMail.insert(END, row)
        monLabel = Label(fenetreGestion, text=row).grid(row=i+4, column=1)
        bouttonSupprimerAdresse = Button(fenetreGestion, text="X")
        bouttonSupprimerAdresse['command'] = lambda b=bouttonSupprimerAdresse, label=monLabel, num=i: supprimerAdresse(num,label,b,nomFichier)
        bouttonSupprimerAdresse.grid(row=i+4, column=2)
        #bouttonSupprimerAdresse = Button(fenetreGestion, text="X", command=lambda num=i: fonctionCommuneGestion.supprimerAdresse(tbl,num,fenetreGestion)).grid(row=i+4, column=2)
        i+=1
    #listBoxMail.grid(row=0, column=1)
    bouttonValider = Button(fenetreGestion, text="OK", command=lambda: fenetreMail.fenetreMail(tbl)).grid(row=i+4, column=1)
    fenetreGestion.mainloop()