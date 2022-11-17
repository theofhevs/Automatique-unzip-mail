#code qui permet de selectionner les lignes du txt
data = []
with open("reger.txt", "r") as f:
    data = f.readlines()  # permet de lire les lignes du fichiers
print(data[1])
text = ""
for i in range(2, data.__len__()):  # de la ligne 2 jusqu'à le total du texte
    text += (data[i])

print(text)

