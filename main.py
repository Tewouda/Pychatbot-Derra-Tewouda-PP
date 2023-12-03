from Fonctions import *
print()
print(" Bonjour comment puis-je vous aider aujourdhui ?\n")
print("    1. Afficher la liste des mots les moins importants dans le corpus de documents. Un mot est dit non important, si son TD-IDF = 0 dans tous les fichiers.")
print("    2. Afficher le(s) mot(s) ayant le score TD-IDF le plus élevé")
print("    3. Indiquer le(s) mot(s) le(s) plus répété(s) par le président Chirac")
print("    4. Indiquer le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois")
print("    5. Indiquer le premier président à parler du climat et/ou de l’écologie")
print("    6. Hormis les mots dits « non importants », savoir le(s) mot(s) que tous les présidents ont évoqués.\n")
choix = int(input(" Entrez le nombre de votre choix : "))
while choix < 1 or choix > 6 :
    print("     Votre choix est invalide")
    choix = int(input(" Entrez le nombre de votre choix : "))

repertoire_speeches = "./speeches"
repertoire_cleaned = "./speeches"
idf = score_idf(repertoire_cleaned)

if choix == 1 :
    print()
    print(afficher_mot_moins_important(repertoire_cleaned,idf))

elif choix == 2 :
    print()
    print(afficher_mot_plus_important(repertoire_cleaned,idf))
elif choix == 3 :
    print()
    print(max_mot_chirac(repertoire_cleaned))
elif choix == 4 :
    print()
    print("Désolé pas eu le temps de developper cette fonctionalité mais sera fait pour la partie 2")
elif choix == 5 :
    print()
    print("Désolé pas eu le temps de developper cette fonctionalité mais sera fait pour la partie 2")
else:
    print()
    print("Désolé pas eu le temps de developper cette fonctionalité mais sera fait pour la partie 2")

