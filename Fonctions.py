import os

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

