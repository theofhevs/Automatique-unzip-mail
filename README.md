# Automatique-unzip-mail


Objectif du script :

Le but de ce script est de pouvoir dans un premier temps télécharger un fichier ZIP depuis un FTP et le dézipper sur votre PC. Ensuite le script contrôlera la structure de l’adresse mail et de la date écrite à l’intérieur du fichier.txt.
Dans le cas d’erreur le fichier ZIP sera déplacé dans le fichier « Echec » sur le FTP et dans le cas contraire il sera déplacé dans le fichier « Succès ».
Le texte à l’intérieur du fichier.txt ainsi que les documents annexes seront envoyés par mail à l’adresse et l’heure figurant dans le fichier txt.
Les fichiers extraits seront pour les deux cas supprimés à la fin du processus.


Warning #1: Ne pas oublier de redéplacer le fichier "Packet.zip" au même emplacement que les deux dossiers "Echec" et "Success"
après chaque utilisation sinon le programme ne trouvera pas son emplacement.

Warning #2 : Ne pas oublier de télécharger le fichier JSON "Settings" afin d'avoir les accès au serveur FTP ainsi qu'à l'adresse mail.

Warning #3 : Pour toute modification concernant le texte, l'adresse mail ou encore la date d'envoie, il faudra directement modifier
ces éléments dans le fichier.txt.

Warning #4 : Afin que la mail soit envoyé à une date précise, n'oubliez pas de laissé le script ouvert jusqu'à ce que le programme ait terminé.


Commit :

L'ensemble des commit concerne le projet réparti en petit bout de code. 
L'assemblage de toute les parties à directement était réalisé par tous les membres du groupe grâce à la fonctionnalité "code with me"
disponible depuis l'éditeur "Pycharm". Ceci explique pourquoi nous n'avons pas beaucoup utilisé les commandes proposées par Git.
