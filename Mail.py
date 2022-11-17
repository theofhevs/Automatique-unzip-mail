import smtplib
from datetime import datetime
from threading import Timer
from email.message import EmailMessage

def sendAutoMail():
    fromAddress = "ssmmttpplib@outlook.com"
    password = input("Password: ")
    toAddress = ""

    #Element du mail
    msg = EmailMessage()
    msg["From"] = fromAddress
    msg["To"] = toAddress
    msg["Subject"] = "Sujet mail"
    msg.set_content("Texte du mail")
    filesPaths = [] #Les chemins d'accès de fichier exemple   r"C:/.../monImg.jpeg"

    #Pour chaque fichier, lire et ajouter au piece jointe
    for filePath in filesPaths:
        with open(filePath, 'rb') as file:
            msg.add_attachment(file.read(), maintype='image', subtype='jpeg')  #seulement jpeg

    #Connecter au smtp de outlook et login et envoie
    with smtplib.SMTP(host="smtp-mail.outlook.com", port=587) as smtpServer:
        smtpServer.starttls()
        smtpServer.login(fromAddress, password)
        smtpServer.send_message(msg, fromAddress, toAddress)

#Execute la fonction à l'heure
x = datetime.today()
y = x.replace(day=x.day + 0, hour=1, minute=1, second=0, microsecond=00)
delta_t = y - x
secs = delta_t.seconds + 1
t = Timer(secs, sendAutoMail)
t.start()

