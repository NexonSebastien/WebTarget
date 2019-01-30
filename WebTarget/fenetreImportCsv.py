from tkinter import *
import fonctionCommuneGestion
import fenetreGestion


def inportCsv(nomFichierLecture, nomFichier, fenetreImportCsv,maFenetreGestion):
    tbl = fonctionCommuneGestion.importNewCsv(nomFichierLecture)
    fonctionCommuneGestion.ecritureCsv(nomFichier, tbl)
    fenetreImportCsv.destroy()
    fenetreGestion.reload(maFenetreGestion, nomFichier)

def fenetreImportCsv(nomFichier,maFenetreGestion):
    fenetreImportCsv = Tk()
    fenetreImportCsv.title("Import CSV")
    lblImportCsv = Label(fenetreImportCsv, text="Import CSV").pack()
    entryCsv = Entry(fenetreImportCsv, width=30)
    entryCsv.pack()
    bouttonValider = Button(fenetreImportCsv, text="OK", command=lambda: inportCsv("data/"+entryCsv.get() + '.csv', nomFichier, fenetreImportCsv,maFenetreGestion)).pack()
    fenetreImportCsv.mainloop()