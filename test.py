import numpy as np
from LVQ.Defines import *
from LVQ.input_data import *

# from LVQ.lqv_basic_functions import *
nb_epoques = 5
v_erreur = np.zeros(10)
data = readfile('data_train.csv', STATIC_40)
data = np.asmatrix(data)
x_matrix = data[:, 1:]

desired_values = np.asmatrix(data[:, 0])
w_matrix = x_matrix[0:10, :]
print(desired_values)
z=0
minimum_index = 0
alpha = 0.1
for t in range(nb_epoques):
    for row in x_matrix:
        temp_erreur_min = 9999
        for i in range(10):
            for j in proto
            v_erreur[i] = np.linalg.norm(row - w_matrix[i, :])
            print(row, w_matrix[i, :])

            if v_erreur.min().item(0) <= temp_erreur_min:
                temp_erreur_min = v_erreur.min().item(0)

                minimum_index = i

        print("reçu :", minimum_index, "désirée :", desired_values.item(z), "distance : ", temp_erreur_min)
        if minimum_index == desired_values.item(i):
            w_matrix[minimum_index, :] = w_matrix[minimum_index, :] + alpha*(row - w_matrix[minimum_index, :])
        else:
            w_matrix[minimum_index, :] = w_matrix[minimum_index, :] - alpha*(row - w_matrix[minimum_index, :])
        z = z + 1
        print(z, "/1340")

    data = readfile('data_train.csv', STATIC_40)
    data = np.asmatrix(data)
    x_matrix = data[:, 1:]
    alpha = alpha*0.5
    desired_values = np.asmatrix(data[:, 0])
    q = 0
    nb_hit = 0
    for row in x_matrix:
        temp_erreur_min = 9999
        for i in range(10):
            v_erreur[i] = np.linalg.norm(row - w_matrix[i, :])

            if v_erreur.min().item(0) <= temp_erreur_min:
                temp_erreur_min = v_erreur.min().item(0)

                minimum_index = i
        if minimum_index == desired_values[q]:
            nb_hit = nb_hit + 1

        q = q + 1
    print("percent_hit : ", nb_hit/1340)
    z = 0
    print("Époque", t+1, "Done")







