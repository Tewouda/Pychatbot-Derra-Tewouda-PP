from Fonctions import *

print("hello pychatbot")
repertoire = "./speeches"
files_names = list_of_files(repertoire,"txt")
print(files_names)

chaine_caractere = "Bryan est allé chez Bryan"
cpt = compter_mots(chaine_caractere)
print(cpt)
