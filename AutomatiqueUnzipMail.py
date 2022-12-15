from datetime import datetime  # permet de travailler avec les dates sous forme d'objet
from threading import Timer # permet d'importer un timer pour executer une action après un temps donné
from email.message import EmailMessage  # classe pour customiser les parties d'un mail (adresses mail, objet, contenu)
from ftplib import FTP  # intègre les connections au serveur FTP
import datetime   # permet de travailler avec les dates sous forme d'objet
import json   # intègre le fichier.Json
import re   # permet de contrôler une chaîne de caractère
import smtplib  # module pour l'envoie du mail
import zipfile  # permet de créer, lire, éditer un fichier zip
import os   # pour de créer, supprimer et éditer un répertoire
import shutil   # permet d'effectuer plusieurs opérations sur un fichier


# ajoute les identifiants du fichier.JSON
def read_settings():
    settings_file = open("Settings.json")  # indique quel fichier json
    return json.load(settings_file)  # ouvre le fichier json


# se connecter au FTP
def connect_to_ftp_server(server, username, password):
    ftp_method = FTP(server)
    ftp_method.login(username, password)
    return ftp_method


# partie contrôle de la date
def test_date():
    # calcul du nombre de lignes
    nbr_lines = len(data)

    date_format = '%d.%m.%Y %H:%M'
    try:
        datetime.datetime.strptime(data[nbr_lines - 1], date_format)
        # si date valide
        return True
    # si date invalide
    except ValueError:
        return False


# création de la méthode pour mettre en majuscule
def transform_cap_upper(txt):
    return txt.upper()


# création de la methode pour remplacer des lettres
def remove_letter(txt, c):
    return txt.replace(c, "")


# création de la methode pour envoyer le mail
def send_auto_mail():
    # stock l'adresse mail valide
    to_address = address_to_verify
    # classe qui structure le mail
    msg = EmailMessage()
    # créer l'en-tête du mail
    header = {"From": settings["addressMail"], "To": to_address, "Subject": object}
    for title, value in header.items():
        msg[title] = value
    # créer le texte du mail
    msg.set_content(text_transform)
    # stocke les fichiers à mettre en pièce jointe
    files_paths = {r"FichierExtrait//CarteMere.pdf": "pdf",
                   r"FichierExtrait//Python.docx": "vnd.openxmlformats-officedocument.wordprocessingml.document"}
    # pour chaque fichier, lire et ajouter en pièce jointe
    for filePath, mimeType in files_paths.items():
        with open(filePath, 'rb') as file:
            msg.add_attachment(file.read(), maintype='application', subtype=mimeType, filename=file.name.split("//")[-1])
    # connection au serveur smtp de outlook, login et envoie du mail
    with smtplib.SMTP(host=settings["smtpHost"], port=settings["smtpPort"]) as smtpServer:
        smtpServer.starttls()
        smtpServer.login(settings["addressMail"], settings["password"])
        smtpServer.send_message(msg)


# supprimer un fichier souhaité
def delete_files():
    os.remove('Packet.zip')
    # supprimer dossier "FichierExtrait"
    shutil.rmtree('FichierExtrait')


# envoie le mail à l'heure indiquée
def send_mail_at_specific_time():
    with open("FichierExtrait\mail.txt", "r") as f:
        data = f.readlines()[-1]

    # trouver l'heure
    date_time = datetime.datetime.strptime(data, "%d.%m.%Y %H:%M")
    x = datetime.datetime.today()
    # heure et la date à laquelle on veut l'envoie du mail
    y = x.replace(year=date_time.year, month=date_time.month, day=date_time.day, hour=date_time.hour, minute=date_time.minute, second=0, microsecond=0)
    delta_t = y - x

    # variables pour envoyer le mail après une seconde et supprimer les fichiers 10 secondes plus tard
    secs = delta_t.seconds + 1
    secs1 = delta_t.seconds + 10
    # timer pour envoyer mail
    l = Timer(secs, send_auto_mail)

    # timer pour supprimer "FichierExtrait" et "Packet.zip" 10 secondes plus tard
    t = Timer(secs1, delete_files)
    t.start()
    l.start()
# Fin des méthodes


# creation de la variable pour les identifiant du fichier.JSON
settings = read_settings()


# connection au ftp
ftp = connect_to_ftp_server(settings["ftpHost"], settings["ftpUsername"], settings["ftpPassword"])
print("Connection réussie")


# téléchargement du fichier zip depuis le ftp
file_name = "Packet.zip"
file_location = "//6312_Python_2022//Proj6_Group11_Win//"
print("Téléchargement du fichier :" + file_name)
ftp.retrbinary("RETR " + file_location + file_name, open(file_name, 'wb').write)


# indique quel fichier doit être dézipper
target = file_name
# cette méthode dézippe le fichier target(notre fichier)
handle = zipfile.ZipFile(target)
# dans la parenthèse se trouve l'emplacement des fichiers extraits
handle.extractall('FichierExtrait')
handle.close()
data = []
print("fichier dezippé sur votre PC")
with open("FichierExtrait/mail.txt", "r") as f:
    # permet de lire les lignes du fichiers
    data = f.readlines()


# partie vérification mail
address_to_verify = data[0].removesuffix('\n')
object = data[1].removesuffix('\n')
# utilisation du regex suivant afin d'avoir le bon format pour les mails : "[_a-z0-9-]+(\.[_a-z0-9-]+)" format de caractère obligatoire pour le mail
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', address_to_verify)


if match is None:
    test_mail = False
    print("le fichier est déplacé dans Echec")
else:
    test_mail = True
    print("le fichier est déplacé dans Succès et envoyé par mail à l'heure indiqué sur le fichier texte")

# sélectionne le texte du fichier txt de la ligne 3 jusqu'à la fin du texte
text = ""
for i in range(3, data.__len__()):
    text += (data[i - 1])

if test_mail and test_date():
    # met le texte en majuscule
    text_transform = transform_cap_upper(txt=text)
    # enlève la lettre "e" dans le texte
    text_transform = remove_letter(text_transform, "E")
    # execute la fonction
    send_mail_at_specific_time()
    # chemin du ftp
    ftp.cwd("/6312_Python_2022/Proj6_Group11_Win")
    # permet de définir le fichier a déplacer
    print(ftp.sendcmd("RNFR Packet.zip"))
    # le chemin de destination avec le nom du fichier
    print(ftp.sendcmd("RNTO ./Succes/Packet.zip"))
    # supprimer fichier zip et "FichierExtrait"
else:
    # chemin du ftp
    ftp.cwd("/6312_Python_2022/Proj6_Group11_Win")
    # permet de définir le fichier a déplacer
    print(ftp.sendcmd("RNFR Packet.zip"))
    # le chemin de destination avec le nom du fichier
    print(ftp.sendcmd("RNTO ./Echec/Packet.zip"))
    # supprimer fichier zip et "FichierExtrait"
    delete_files()
