from Fonctions import *

'''print("hello pychatbot")
repertoire_speeches = "./speeches"
fichiers = liste_fichiers(repertoire_speeches,"txt")
print(fichiers)'''

repertoire_cleaned = "./cleaned"
#liste_noms_presi(fichiers)

#convertion_miniscule(repertoire_speeches, repertoire_cleaned)
#supp_ponctuation(repertoire_cleaned)


idf_scores = score_idf(repertoire_cleaned)
print(idf_scores)
