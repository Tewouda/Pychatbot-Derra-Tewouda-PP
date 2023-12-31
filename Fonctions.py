import os
import math
# Fonction pour l'extraction des fichiers dans le dossier speeches
def liste_fichiers(repertoire,extension): # Fonction prenant en paramètre le chemin du dit dossier et l'extension des fichiers à extraire
    fichiers = []
    for elem in os.listdir(repertoire):
        if elem.endswith(extension):
            fichiers.append(elem[11:-4]) # Création d'une liste contenant le nom des fichiers du dossier
    return fichiers

# Fonction affichant la liste des présidents en faisant attention aux doublons
def liste_noms_presi(liste) :
    Set = set()
    for elem in liste :
        mot = ""
        for chr in elem :
            if ord(chr) < ord("0") or ord(chr) >ord("9") : # Elimination des caractères numeriques
                mot+= chr
        Set.add(mot) # Ajout des elements sans caractères numeriques dans un set afin d'eliminer les doublouns
    print(list(Set)) # castage en liste du set et affichage


# Fonction convertissant le contenu des fichiers en miniscules et stockage dans un autre fichier
def convertion_miniscule(repertoire1,repertoire2) :
    for fichier in os.listdir(repertoire1) : # Parcours des fichiers du repertoire 1

        file_path = os.path.join(repertoire1,fichier) # Recuperation du chemin d'acces de chaque fichiers

        with open(file_path,"r") as f : # Lecture du fichier en entier
            ligne = f.read()


        nv_ligne =""
        for i in ligne : # Parcours du contenu du ficher elements par elements
            if ord(i) >= 65 and ord(i) <= 90 :
                i = chr(ord(i) + 32) # convertion en minuscule
            nv_ligne += i # Recuperation du contenu convertis

        nv_fichier = fichier[:-4] + "_cleaned.txt" # Nommination du nouveau fichier

        with open(repertoire2 +"/"+nv_fichier,"w") as f : # Creation du nouveau fichier dans le nouveau repertoire
            f.write(nv_ligne)


# Fonction supprimant la ponctuation
def supp_ponctuation(repertoire):

    for files in os.listdir(repertoire) :
        files_path = os.path.join(repertoire,files)
        with open(files_path,"r") as f : # Lectures du fichiers
            lignes = f.readlines()

        with open(files_path, "w") as f: # Reecriture du fichier
            for ligne in lignes : # Parcours des lignes du fichiers
                nv_ligne = ""
                for i in ligne : # Parcours des caractères dans les lignes
                    if (i == "'" or i == "-") or i == " " : # Remplacement de certains caractères par un espace
                        i = " "
                    elif (ord(i) < 97 or ord(i) > 122) and (i not in ["é","è","ç","à","ù"]) : # Suppression de certains caractères
                        i = ""
                    nv_ligne += i # Recuperation de tous les caractères de la ligne
                f.write(nv_ligne) # Ecriture de la ligne


def compter_mots(chaine):
    mots = chaine.split()  # Séparer la chaîne en mots
    compteur_mots = {}  # Initialiser un dictionnaire vide pour compter les mots

    for mot in mots:
        # Vérifier si le mot est déjà dans le dictionnaire, sinon initialiser à 0
        compteur_mots[mot] = compteur_mots.get(mot, 0) + 1

    return compteur_mots

def score_idf(repertoire):
    nombre_documents = 0
    mots_par_document = {}
    idf_scores = {}

    # Parcourir les fichiers du répertoire
    for files in os.listdir(repertoire):
        file_path = os.path.join(repertoire, files )
        if os.path.isfile(file_path) and files.endswith('.txt'):
            nombre_documents += 1
            mots_du_document = set()

            # Lire le contenu du fichier
            with open(file_path, 'r') as f:
                contenu = f.read().split()
                for mot in contenu:
                    mots_du_document.add(mot)  # Stocker les mots uniques du document

            # Mettre à jour le dictionnaire mots_par_document avec les mots du document actuel
            for mot in mots_du_document:
                mots_par_document[mot] = mots_par_document.get(mot, 0) + 1

    # Calculer IDF pour chaque mot
    for mot, occurrences in mots_par_document.items():
        score = math.log10(nombre_documents / occurrences)
        idf_scores[mot] = score

    return idf_scores

def matrice_tf_idf (repertoire,idf) :
    cpt_col = 0
    contenu = ""
    for file in os.listdir(repertoire) :
        cpt_col +=1
        file_path = os.path.join(repertoire,file)
        with open(file_path,"r") as f :
            contenu += f.read()

    tf = compter_mots(contenu)
    cpt_lig = 0
    for mot in tf :
        cpt_lig +=1

    M = [0]*cpt_lig
    for i in range(cpt_lig) :
        M[i] = [0]*cpt_col

    j = 0
    for file in os.listdir(repertoire) :
        i = 0
        for mot in tf :
            M[i][j] = idf[mot]* tf[mot]
            i += 1
        j +=1
    return M

def afficher_mot_moins_important (repertoire,idf) :
    contenu = ""
    for file in os.listdir(repertoire):
        file_path = os.path.join(repertoire, file)
        with open(file_path, "r") as f:
            contenu += f.read()
    tf = compter_mots(contenu)

    L = {}
    for mot in tf :
        L[mot] = tf[mot] * idf[mot]
    min = 10
    res = ""
    for i in L :
        if L[i] <= min :
            min = L[i]
            res = i
    print(res, "est le mot le moins important")
    print()

def afficher_mot_plus_important(repertoire,idf) :
    contenu = ""
    for file in os.listdir(repertoire):
        file_path = os.path.join(repertoire, file)
        with open(file_path, "r") as f:
            contenu += f.read()
    tf = compter_mots(contenu)

    L = {}
    for mot in tf:
        L[mot] = tf[mot] * idf[mot]
    max = 0
    res = ""
    for i in L:
        if L[i] >= max:
            max = L[i]
            res = i
    print(res, "est le mot le plus important")
    print()

def max_mot_chirac(repertoire) :
    contenu = ""
    for file in os.listdir(repertoire):
        i = 1
        while i <= 2 :
            file_path = os.path.join(repertoire, file)
            with open(file_path, "r") as f:
                contenu += f.read()
            i += 1
    tf = compter_mots(contenu)
    max = 0
    res = ""
    for mot in tf :
        if tf[mot] >= max :
            max = tf[mot]
            res = mot
    print("Le mot le plus repeter par le président Chirac est" , res)
    print()