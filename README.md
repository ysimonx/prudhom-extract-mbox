# prudhom-extract-mbox

Ce script exporte des données d'un fichier "test.mbox" que l'on obtient, notamment avec la procédure "take away" de Google Drive ou d'Outlook
afin d'en extraire les données des emails envoyés et/ou reçus à savoir :
- l'expéditeur
- la date et l'heure
- le sujet
- la liste des destinataires 
- la liste des destinataires en copie

le fichier en sortie peut etre récupéré via excel, c'est un fichier texte au format UTF-8, caractère séparateur '£'
avec la commande 

python3 prudhom-mbox.py > resultat.txt


