def transformCap(txt): #création de la méthode pour mettre en majuscule
    return txt.upper()


def removeLetter(txt, c): # création de la méthode pour remplacer des lettres
    return txt.replace(c, "")


resultat = transformCap(txt="theo falcinelli")

print(resultat)

resultat = removeLetter(resultat, "E")

print(resultat)
