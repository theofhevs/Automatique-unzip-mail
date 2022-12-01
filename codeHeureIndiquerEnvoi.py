from datetime import datetime
from threading import Timer


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


l = Timer(secs, "hello_world")#à LA PLACE DE HELLO_WORLD ON METTRA LA MéTHODE POUR ENVOYER MAIL
l.start()



