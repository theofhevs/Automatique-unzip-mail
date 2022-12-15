# Automatique-unzip-mail


Objectif du script :

Le but de ce script est de pouvoir dans un premier temps télécharger un fichier ZIP depuis un FTP et le dézipper sur votre PC. Ensuite le script contrôlera la structure de l’adresse mail et de la date écrite à l’intérieur du fichier.txt.
Dans le cas d’erreur le fichier ZIP sera déplacé dans le fichier « Echec » sur le FTP et dans le cas contraire il sera déplacé dans le fichier « Succès ».
Le texte à l’intérieur du fichier.txt ainsi que les documents annexes seront envoyés par mail à l’adresse et l’heure figurant dans le fichier txt.
Les fichiers extraits seront pour les deux cas supprimés à la fin du processus.


Warning #1: Afin de pouvoir rajouter votre adresse mail et changer la date, il faudra : 
  1. Vous connecter au FTP
  2. Vous récuperez le fichier "Packet.zip" à la racine du dossier "/6312_Python_2022/Proj6_Group11_Win"
  3. Vous devez dézipper le fichier "Packet.zip" afin de pouvoir modifier le fichier "mail.txt" contenu à l'intérieur de celui-ci 
  4. Ensuite il faut ouvrir le fichier "mail.txt" dans un éditeur de texte et modifier les lignes suivantes par exemple :
```text
VotreEmail@subdomain.domain <- Saisir votre e-mail
Automatique unzip mail
Ci-joint vous retrouverez 
un document Word ainsi qu'un PDF.
Meilleurs salutations, le groupe 6 Windows
15.12.2022 19:39 <- Saisir la date d'envoi de l'e-mail
```
Vous devez modifier les deux lignes suivantes : l'e-mail et la date d'envoi

  5. Maintenant vous devez zipper le dossier "Packet"
  6. Ensuite vous devez remplacer le fichier "Packet.zip" sur le FTP

Ne pas oublier de redéplacer le fichier "Packet.zip" au même emplacement que les deux dossiers "Echec" et "Success"
après chaque utilisation sinon le programme ne trouvera pas son emplacement.

Warning #2 : Ne pas oublier de télécharger le fichier JSON "Settings" afin d'avoir les accès au serveur FTP ainsi qu'à l'adresse mail.

Warning #3 : Pour toute modification concernant le texte, l'adresse mail ou encore la date d'envoi, il faudra directement modifier
ces éléments dans le fichier.txt.

Warning #4 : Afin que la mail soit envoyé à une date précise, n'oubliez pas de laisser le script ouvert jusqu'à ce que le programme ait terminé.


Commit :

L'ensemble des commit concerne le projet réparti en petit bout de code. 
L'assemblage de toute les parties à directement été réalisé par tous les membres du groupe grâce à la fonctionnalité "code with me"
disponible depuis l'éditeur "Pycharm". Ceci explique pourquoi nous n'avons pas un nombre important de commit.
