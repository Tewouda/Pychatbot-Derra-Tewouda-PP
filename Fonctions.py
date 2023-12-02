import os
import math
def list_of_files(a,b):
    files_names = []
    for elem in os.listdir(a):
        if elem.endswith(b):
            files_names.append(elem[11:-4])
    return files_names

def pres_noms(l) :
    dic = {}
    for elem in l :
        dic[elem] = elem[11:]


def compter_mots(chaine) :
    mots = chaine.split()   # Séparer la chaîne en mots
    compteur_mots = {}     # Initialiser un dictionnaire vide pour compter les mots

    for mot in mots :
        # Vérifier si le mot est déjà dans le dictionnaire, sinon initialiser à 0
        compteur_mots[mot] = compteur_mots.get(mot, 0) + 1
    return compteur_mots


def score_idf(repertoire) :
    mots_par_documents = {}
    idf_scores = {}
    nombre_documents = 0
    # Parcourir les fichiers du répertoire
    for files in os.listdir(repertoire) :
        files_path = os.path.join(repertoire, files)
        if os.path.isfile(files_path) and files.endswith('.txt'):
            nombre_documents += 1
            mots_du_document = set()
        with open(files_path, "r") as f :
            ligne = f.read().split()
            for mot in ligne :
                mots_du_document.add(mot)  # Stocker les mots uniques du document

        for mot in mots_du_document :
            # Mettre à jour le dictionnaire mots_par_document avec les mots du document actuel
            mots_par_documents[mot] = mots_par_documents.get(mot, 0) + 1

    # Calculer l'IDF pour chaque mot
    for mot, occurrences in mots_par_documents.items() :
        idf_score = math.log10(nombre_documents / occurrences)
        idf_scores[mot] = idf_score

    return idf_scores


