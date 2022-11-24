from datetime import datetime
from email.message import EmailMessage
import zipfile
import datetime
import shutil
import re
import smtplib
from ftplib import FTP


def connect_to_FTP_server(server, username, password):
    # domain name or server ip:
    ftp = FTP(server)
    ftp.login(username, password)
    return ftp

# partie contrôle date
def test_date():
    # calcul du nombre de lignes
    nbrLines = len(data)
    # print(data[nbrLines - 1])

    # source pour les formats: https://www.w3schools.com/python/python_datetime.asp
    date_format = '%d.%m.%Y %H:%M'
    try:
        valid_date = datetime.datetime.strptime(data[nbrLines - 1], date_format)
        # date valide
        return 0
    # si date invalide
    except ValueError:
        return -1


def transformCap(txt):  # création de la méthode pour mettre en majuscule
    return txt.upper()


def removeLetter(txt, c):  # création de la méthode pour remplacer des lettres
    return txt.replace(c, "")

def sendAutoMail():
    fromAddress = "ssmmttpplib@outlook.com"
    password = "MailAuto465"
    toAddress = addressToVerify
    # Element du mail
    msg = EmailMessage()
    msg["From"] = fromAddress
    msg["To"] = toAddress
    msg["Subject"] = objet
    msg.set_content(textTransformer)
    filesPaths = {r"C:\Users\loren\PycharmProjects\Automatique-unzip-mail\FichierExtrait\nice.pdf": "pdf"}
    # Pour chaque fichier, lire et ajouter au piece jointe
    for filePath, mimeType in filesPaths.items():
        with open(filePath, 'rb') as file:
            msg.add_attachment(file.read(), maintype='application', subtype=mimeType)
    # Connecter au smtp de outlook et login et envoie
    with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as smtpServer:
        smtpServer.starttls()
        smtpServer.login(fromAddress, password)
        smtpServer.send_message(msg, fromAddress, toAddress)


#Lire le ftp
ftp_server = connect_to_FTP_server('d73kw.ftp.infomaniak.com', 'd73kw_proj6_group11_win', 'UvmZdaW975a8' )
ftp_server.cwd("/6312_Python_2022/Proj6_Group11_Win")
print(ftp_server.dir())

# partie dézipper
target = 'Packet.zip' #indique quel fichier doit être dézipper
handle = zipfile.ZipFile(target) #cette méthode dézippe le fichier target(notre fichier)
handle.extractall('FichierExtrait') #dans la parenthèse se trouve l'emplacement des fichiers extraits
handle.close()

data = []
with open("FichierExtrait\mail.txt", "r") as f:
    data = f.readlines()  # permet de lire les lignes du fichiers

# print(data[0])

# partie vérifier mail
addressToVerify = data[0].removesuffix('\n') #lorenzodeieso@gmail.com
objet = data[1].removesuffix('\n') #object
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

if match == None:
    testMail = -1
else:
    testMail = 0

test_date()

# decode bse64


# sélectionne le texte du fichier depuis le server ftp
text = ""
for i in range(3, data.__len__()):  # de la ligne 2 jusqu'à le total du texte
    text += (data[i - 1])


if testMail != 0 or test_date() != 0:
    # Déplacer un fichier du répertoire rep1 vers rep2
    shutil.move("Packet.zip", "Echec")
    shutil.rmtree('FichierExtrait')

else:
    textTransformer = transformCap(txt=text)#transforme le texte selectionner
    textTransformer = removeLetter(textTransformer, "E")
    # Execute la fonction
    sendAutoMail()
