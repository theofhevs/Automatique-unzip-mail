from zipfile import ZipFile


with ZipFile("C:/Users/theof/OneDrive/Bureau/Test python/final.zip","r") as zipObject:

    listOfFileNames = zipObject.namelist()
    for fileName in listOfFileNames:
        zipObject.extract(fileName, 'C:/Users/theof/OneDrive/Bureau')






