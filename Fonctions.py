import os

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
