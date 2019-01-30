from tkinter import *
import fenetreGestion
# Accueil

#MAIN
#LECTURE
# tbl = lectureCsv('webtarget.csv')
# #Supression doublons
# tbl = supprimerDoublon(tbl)
# #Verification Mail
# tblValide = []
# for row in tbl:
#     valeur = verificationMail(row)
#     if valeur != None:
#         tblValide.append(valeur[0])
# #SUPPRESSION
#    supprimerEmailInMailList(tblValide,email)
# #ECRITURE
# ecritureCsv('campagne.csv',tblValide)
#Verification URL
#tblUrl= []
#tblUrl.append(verificationUrl('tygyyt'))
#Recupération Domaine
#domaine = emailDomaine('nexon.sebastien@gmail.com')
#PING
#if domaine != None:
#    echec = pingDomaine(domaine)
#    print(echec)
#CRAWLER
# tblCrawler = crawlerUrl('http://univcergy.phpnet.org/python/mail.html')
# ecritureCsv('campagne.csv',tblCrawler)

fenetreAccueil = Tk()
fenetreAccueil.title("WebTarget")
lblNomCsv= Label(fenetreAccueil, text="nomCampagne")
lblNomCsv.pack()
entryCsv = Entry(fenetreAccueil, width=30)
entryCsv.pack()
#bouttonValider = Button(fenetreAccueil, text="Valider", command=lambda: lectureCsv(nomCsv.get()+'.csv')).pack()
bouttonValider = Button(fenetreAccueil, text="Valider", command=lambda: fenetreGestion.fenetreGestion(fenetreAccueil, entryCsv,0)).pack()
fenetreAccueil.mainloop()