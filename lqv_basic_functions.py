import numpy as np


def calcul_distance(list_x, list_w):
    dist = np.linalg.norm(np.subtract(list_x,list_w))
    return dist

def min_classe(list_d):
    minimum = list_d.index(min(list_d))
    return minimum

if x.classe = Min_Class :
    Mat_W[Min_Classe] = np.add(Mat_W[Min_Classe],n*(np.subtract(x.vecteur_x,Mat_W[Min_Classe])))
else
    Mat_W[Min_Classe] = np.subtract(Mat_W[Min_Classe],n*(np.subtract(x.vecteur_x,Mat_W[Min_Classe])))
