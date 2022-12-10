from datetime import datetime
from threading import Timer
from email.message import EmailMessage
from ftplib import FTP
import datetime
import json
import re
import smtplib
import zipfile
import os
import shutil

def read_settings():
    settings_file = open("Settings.json")  # indique quel fichier json
    return json.load(settings_file)  # ouvre le fichier json


def connect_to_ftp_server(server, username, password):  # se connecter au FTP
    # domain name or server ip:
    _ftp = FTP(server)
    _ftp.login(username, password)
    return _ftp


# partie contrôle date
def test_date():
    # calcul du nombre de lignes
    nbr_lines = len(data)
    # print(data[nbrLines - 1])

    # source pour les formats: https://www.w3schools.com/python/python_datetime.asp
    date_format = '%d.%m.%Y %H:%M'
    try:
        datetime.datetime.strptime(data[nbr_lines - 1], date_format)
        # date valide
        return True
    # si date invalide
    except ValueError:
        return False


def transform_cap(txt):  # création de la méthode pour mettre en majuscule
    return txt.upper()


def remove_letter(txt, c):  # création de la méthode pour remplacer des lettres
    return txt.replace(c, "")


def send_auto_mail():
    to_address = addressToVerify
    # Elements du mail
    msg = EmailMessage()
    header = {"From": settings["addressMail"], "To": to_address, "Subject": objet}
    for title, value in header.items():
        msg[title] = value
    msg.set_content(textTransformer)
    files_paths = {r"FichierExtrait//CarteMere.pdf": "pdf",
                   r"FichierExtrait//Python.docx": "vnd.openxmlformats-officedocument.wordprocessingml.document"}
    # Pour chaque fichier, lire et ajouter en pièce jointe
    for filePath, mimeType in files_paths.items():
        with open(filePath, 'rb') as file:
            msg.add_attachment(file.read(), maintype='application', subtype=mimeType, filename=file.name.split("//")[-1])
        # Connection au serveur smtp de outlook, login et envoie du mail
    with smtplib.SMTP(host=settings["smtpHost"], port=settings["smtpPort"]) as smtpServer:
        smtpServer.starttls()
        smtpServer.login(settings["addressMail"], settings["password"])
        smtpServer.send_message(msg, settings["addressMail"], to_address)

def supprime():
    os.remove('Packet.zip')
    # supprimer dossier "FichierExtrait"
    shutil.rmtree('FichierExtrait')

def envoieMailHeureIndiquee():
    with open("FichierExtrait\mail.txt", "r") as f:
        data = f.readlines()[-1]
    #29.01.2022 10:00
    # *****************************************************
    # début pour trouver heure
    N = 2
    count = 0
    res = ""
    for ele in data:
        if ele == ' ':
            count = count + 1
            if count == N:
                break
            res = ""
        else:
            res = res + ele

    N = 1
    count = 0
    hour = ""
    for ele in res:
        if ele == ':':
            count = count + 1
            if count == N:
                break
            hour = ""
        else:
            hour = hour + ele

    # Conversion de string en entier
    int_hour = int(hour)
    # fin pour trouver heure

    # début pour trouver minute
    N = 2
    count = 0
    min = ""
    for ele in data:
        if ele == ':':
            count = count + 1
            if count == N:
                break
            min = ""
        else:
            min = min + ele

    # Conversion de string en entier
    int_min = int(min)
    # fin pour trouver min
    # ****************************************************


    # ****************************************************
    # début pour trouver annee
    N = 1
    count = 0
    res = ""
    for ele in data:
        if ele == ' ':
            count = count + 1
            if count == N:
                break
            res = ""
        else:
            res = res + ele

    N = 3
    count = 0
    annee = ""
    for ele in res:
        if ele == '.':
            count = count + 1
            if count == N:
                break
            annee = ""
        else:
            annee = annee + ele

    # Conversion de string en entier
    int_annee = int(annee)
    # fin pour trouver annee

    # début pour trouver mois
    N = 1
    count = 0
    res = ""
    for ele in data:
        if ele == ' ':
            count = count + 1
            if count == N:
                break
            res = ""
        else:
            res = res + ele

    N = 2
    count = 0
    mois = ""
    for ele in res:
        if ele == '.':
            count = count + 1
            if count == N:
                break
            mois = ""
        else:
            mois = mois + ele

    int_mois = int(mois)
    # fin pour trouver

    # début pour trouver jour
    N = 1
    count = 0
    jour = ""
    for ele in data:
        if ele == '.':
            count = count + 1
            if count == N:
                break
            jour = ""
        else:
            jour = jour + ele

    int_jour = int(jour)
# fin pour trouver jour
# **************************************************


    x = datetime.datetime.today()  # ici on met l'heure à laquelle on veut que ça print
    y = x.replace(year=int_annee, month=int_mois, day=int_jour, hour=int_hour, minute=int_min, second=0, microsecond=0)
    delta_t = y - x

    secs = delta_t.seconds + 1
    secs1 = delta_t.seconds + 10


    l = Timer(secs, send_auto_mail)#à LA PLACE DE HELLO_WORLD ON METTRA LA MéTHODE POUR ENVOYER MAIL
    t = Timer(secs1,supprime)#supprime FichierExtrait et Packet.zip 10 secondes plus tard
    t.start()
    l.start()


settings = read_settings()


# connecte sur le ftp
ftp = connect_to_ftp_server(settings["ftpHost"], settings["ftpUsername"], settings["ftpPassword"])

# télécharge fichier zip depuis un ftp

fileName = "Packet.zip"
fileLocation = "//6312_Python_2022//Proj6_Group11_Win//"
print("Téléchargement du fichier :" + fileName)
ftp.retrbinary("RETR " + fileLocation + fileName, open(fileName, 'wb').write)

# partie dézipper
target = fileName  # indique quel fichier doit être dézipper
handle = zipfile.ZipFile(target)  # cette méthode dézippe le fichier target(notre fichier)
handle.extractall('FichierExtrait')  # dans la parenthèse se trouve l'emplacement des fichiers extraits
handle.close()

data = []
with open("FichierExtrait/mail.txt", "r") as f:
    data = f.readlines()  # permet de lire les lignes du fichiers

# print(data[0])

# partie vérifier mail
addressToVerify = data[0].removesuffix('\n')  # lorenzodeieso@gmail.com
objet = data[1].removesuffix('\n')  # object
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

if match is None:
    testMail = False
else:
    testMail = True

# sélectionne le texte du fichier txt
text = ""
for i in range(3, data.__len__()):  # de la ligne 2 jusqu'à le total du texte
    text += (data[i - 1])

if testMail and test_date():
    textTransformer = transform_cap(txt=text)  # transforme le texte selectionner
    textTransformer = remove_letter(textTransformer, "E")
    # Execute la fonction
    envoieMailHeureIndiquee()

    ftp.cwd("/6312_Python_2022/Proj6_Group11_Win")  # chemin du ftp
    print(ftp.sendcmd("RNFR Packet.zip"))  # Permet de définir le fichier a déplacer
    print(ftp.sendcmd("RNTO ./Succes/Packet.zip"))  # le chemin de destination avec le nom du fichier

else:
    ftp.cwd("/6312_Python_2022/Proj6_Group11_Win")  # chemin du ftp
    print(ftp.sendcmd("RNFR Packet.zip"))  # Permet de définir le fichier a déplacer
    print(ftp.sendcmd("RNTO ./Echec/Packet.zip"))  # le chemin de destination avec le nom du fichier
    #supprimer fichier zip
    supprime()
