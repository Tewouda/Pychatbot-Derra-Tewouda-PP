import os
import math


# Fonction pour l'extraction des fichiers dans le dossier speeches
def liste_fichiers(repertoire,extension):  # Fonction prenant en paramètre le chemin du dit dossier et l'extension des fichiers à extraire
    fichiers = []
    for elem in os.listdir(repertoire):
        if elem.endswith(extension):
            fichiers.append(elem[:-4])  # Création d'une liste contenant le nom des fichiers du dossier
    return fichiers


# Fonction affichant la liste des présidents en faisant attention aux doublons
def liste_noms_presi(liste):
    Set = set()
    for elem in liste:
        mot = ""
        for chr in elem:
            if ord(chr) < ord("0") or ord(chr) > ord("9"):  # Elimination des caractères numeriques
                mot += chr
        Set.add(mot)  # Ajout des elements sans caractères numeriques dans un set afin d'eliminer les doublouns
    print(list(Set))  # castage en liste du set et affichage


# Fonction convertissant le contenu des fichiers en miniscules et stockage dans un autre fichier
def convertion_miniscule(repertoire1, repertoire2):
    for fichier in os.listdir(repertoire1):  # Parcours des fichiers du repertoire 1

        file_path = os.path.join(repertoire1, fichier)  # Recuperation du chemin d'acces de chaque fichiers

        with open(file_path, "r") as f:  # Lecture du fichier en entier
            ligne = f.read()

        nv_ligne = ""
        for i in ligne:  # Parcours du contenu du ficher elements par elements
            if ord(i) >= 65 and ord(i) <= 90:
                i = chr(ord(i) + 32)  # convertion en minuscule
            nv_ligne += i  # Recuperation du contenu convertis

        nv_fichier = fichier[:-4] + "_cleaned.txt"  # Nommination du nouveau fichier

        with open(repertoire2 + "/" + nv_fichier, "w") as f:  # Creation du nouveau fichier dans le nouveau repertoire
            f.write(nv_ligne)


# Fonction supprimant la ponctuation
def supp_ponctuation(repertoire):
    ponct = "-,?;:/!+'"

    for files in os.listdir(repertoire):
        files_path = os.path.join(repertoire, files)
        with open(files_path, "r") as f:  # Lectures du fichiers
            lignes = f.readlines()

        with open(files_path, "w") as f:  # Reecriture du fichier
            for ligne in lignes:  # Parcours des lignes du fichiers
                nv_ligne = ""
                for i in ligne:  # Parcours des caractères dans les lignes
                    if i in ponct:
                        nv_ligne += " "
                    else:
                        nv_ligne += i
                f.write(nv_ligne)  # Ecriture de la ligne


def compter_mots(chaine):
    mots = chaine.split()  # Séparer la chaîne en mots
    compteur_mots = {}  # Initialiser un dictionnaire vide pour compter les mots

    for mot in mots:
        # Vérifier si le mot est déjà dans le dictionnaire, sinon initialiser à 0
        compteur_mots[mot] = compteur_mots.get(mot, 0) + 1

    return compteur_mots

def score_tf_term(terme, repertoire, document):
    path = repertoire + "/" + document + ".txt"
    occ = 0

    with open(path, "r", encoding='utf-8') as f:
        content = f.read()
        words = content.split()
        for word in words:
            if word == terme:
                occ += 1
        return occ / len(words)


def score_tf(repertoire):
    files = liste_fichiers(repertoire, "txt")
    word_set = set()
    for file in files:
        with open(repertoire + "/" + file + ".txt", "r", encoding="utf-8") as f:
            content = f.read().split()
            for word in content:
                word_set.add(word)
    print(word_set)

    d_tf = {}
    for word in word_set:
        if word not in d_tf.keys():
            d_tf[word] = []
        for file in files:
            d_tf[word].append(score_tf_term(word, repertoire, file))
    return d_tf


def score_idf(repertoire):
    nombre_documents = 0
    mots_par_document = {}
    idf_scores = {}

    # Parcourir les fichiers du répertoire
    for files in os.listdir(repertoire):
        file_path = os.path.join(repertoire, files)
        if os.path.isfile(file_path) and files.endswith('.txt'):
            nombre_documents += 1
            mots_du_document = set()

            # Lire le contenu du fichier
            with open(file_path, 'r', encoding='utf-8') as f:
                contenu = f.read().split()
                for mot in contenu:
                    mots_du_document.add(mot)  # Stocker les mots uniques du document

            # Mettre à jour le dictionnaire mots_par_document avec les mots du document actuel
            for mot in mots_du_document:
                #mots_par_document[mot] = mots_par_document.get(mot, 0) + 1
                if mot not in mots_par_document.keys():
                    mots_par_document[mot] = 1
                else:
                    mots_par_document[mot] += 1

    # Calculer IDF pour chaque mot
    for mot, occurrences in mots_par_document.items():
        score = round(math.log10(nombre_documents / occurrences), 2)
        idf_scores[mot] = score

    return idf_scores


def tfidf_matrix(repertoire):
    files = [file[:-4] for file in os.listdir(repertoire) if file.endswith('.txt')]
    words = set()
    for file in files:
        with open(os.path.join(repertoire, file + ".txt"), "r", encoding="utf-8") as f:
            content = f.read().split()
            words.update(content)

    tf_scores = {}
    for word in words:
        tf_scores[word] = [score_tf_term(word, repertoire, file) for file in files]

    idf_scores = score_idf(repertoire)

    matrix = [0] * len(words)
    for i in range(len(words)) :
        matrix[i] = [0]*len(files)


    for i, word in enumerate(words):
        for j, file in enumerate(files):
            tf_value = tf_scores[word][j]
            idf_value = idf_scores.get(word,0)
            matrix[i][j] = tf_value * idf_value

    return matrix


def afficher_mot_moins_important( idf, tf) :
    L = {}
    for mot in tf:
        for j in range(len(tf[mot])):
            L[mot] = tf[mot][j] * idf.get(mot,0)
    res = ""
    for i in L:
        if L[i] == 0.0 :
            res += i + " "
    M = res.split()
    return M


def afficher_mot_plus_important(tf, idf):
    L = {}
    for mot in tf:
        for j in range(len(tf[mot])):
            L[mot] = tf[mot][j] * idf.get(mot, 0)
    res = ""
    for i in L:
        if (L[i] > 0.0):
            res += i + " "
    M = res.split()
    return M


def max_mot_chirac(repertoire):
    contenu = ""
    for file in os.listdir(repertoire):
        i = 1
        while i <= 2:
            file_path = os.path.join(repertoire, file)
            with open(file_path, "r", encoding='utf-8') as f:
                contenu += f.read()
            i += 1
    tf = compter_mots(contenu)
    max = 0
    res = ""
    for mot in tf:
        if tf[mot] >= max:
            max = tf[mot]
            res = mot
    print("Le mot le plus repeter par le président Chirac est", res)
    print()

def print_mat(mat):
    for row in mat:
        print(row)

