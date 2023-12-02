from Fonctions import *

print("hello pychatbot")
repertoire_speeches = "./speeches"
fichiers = liste_fichiers(repertoire_speeches,"txt")
print(fichiers)

repertoire_cleaned = "./cleaned"
liste_noms_presi(fichiers)

#convertion_miniscule(repertoire_speeches, repertoire_cleaned)
supp_ponctuation(repertoire_cleaned)


chaine_caractere = "Bryan est allé chez Bryan"
cpt = compter_mots(chaine_caractere)
print(cpt)
