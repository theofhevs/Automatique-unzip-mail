import datetime

def test_date():
    data = []
    with open("test.txt", "r") as f:
        data = f.readlines()
        # calcul du nombre de lignes
        nbrLines = len(data)
        date = data[nbrLines-1]
        print(date)

    # source pour les formats: https://www.w3schools.com/python/python_datetime.asp
    date_format = '%d.%m.%Y %H:%M'

    try:
        valid_date = datetime.datetime.strptime(date, date_format)
    # si date invalide
    except ValueError:
        print("Invalid date")
        return -1
    return 0


# si date valide
if test_date()==0:
    print("Valid date")