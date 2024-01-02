from Fonctions import *

repertoire_speeches = "./test-corpus"
repertoire_cleaned = "./test-corpus-cleaned"
convertion_miniscule(repertoire_speeches,repertoire_cleaned)
supp_ponctuation(repertoire_cleaned)

tf = score_tf_affichage(repertoire_cleaned)
print(tf)

'''files = liste_fichiers(repertoire_cleaned, "txt")
word_set = set()
for file in files:
    with open(repertoire_cleaned + "/" + file + ".txt" , "r", encoding="utf-8") as f:
        content = f.read().split()
        for word in content:
            word_set.add(word)
print(word_set)

d_tf = {}
for word in word_set:
    if word not in d_tf.keys():
        d_tf[word] = []
    for file in files:
        d_tf[word].append(score_tf_term(word, repertoire_cleaned, file))
print(d_tf)'''