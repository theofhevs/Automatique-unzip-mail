import zipfile

target = 'my_files.zip' #indique quel fichier doit être dézipper

handle = zipfile.ZipFile(target) #cette méthode dézippe le fichier target(notre fichier)

handle.extractall('exemple') #dans la parenthèse se trouve l'emplacement des fichiers extraits

handle.close()