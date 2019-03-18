import numpy as np

def calcul_Distance(list_X, list_W):
    Dist = np.linalg.norm(subtract(list_X,list_W))
return Dist

def min_Classe(list_D):
    Min_Classe = list_D.index(min(list_D))
return Min_Classe

if x.classe = Min_Class :
    Mat_W[Min_Classe] = np.add(Mat_W[Min_Classe],n*(np.subtract(x.vecteur_x,Mat_W[Min_Classe])))
else
    Mat_W[Min_Classe] = np.subtract(Mat_W[Min_Classe],n*(np.subtract(x.vecteur_x,Mat_W[Min_Classe])))
