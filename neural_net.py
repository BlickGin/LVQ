import numpy as np
from LVQ.Defines import *
from LVQ.input_data import *

class neural_net():
    def __init__(self, nb_proto, input_car, base_learning_rate=0.1):
        self.nb_epoques = 0
        self.input_matrix = []
        self.input_caracteristics = input_car
        self.nb_of_prototypes = nb_proto
        self.v_erreur = np.zeros(nb_proto)
        self.learning_rate = base_learning_rate


        if input_car == STATIC_40:
            self.training_data = np.asmatrix([1340, 12 * 40])
            self.w_matrix = np.asmatrix([nb_proto * 10,12 * 40])
        elif input_car == STATIC_50:
            self.training_data = np.asmatrix([1340, 12 * 50])
            self.w_matrix = np.asmatrix([nb_proto * 10, 12 * 50])
        elif input_car == STATIC_60:
            self.training_data = np.asmatrix([1340, 12 * 60])
            self.w_matrix = np.asmatrix([nb_proto * 10, 12 * 60])
        elif input_car == ALL_40:
            self.training_data = np.asmatrix([1340, 26 * 40])
            self.w_matrix = np.asmatrix([nb_proto * 10, 26 * 40])
        elif input_car == ALL_50:
            self.training_data = np.asmatrix([1340, 26 * 50])
            self.w_matrix = np.asmatrix([nb_proto * 10, 26 * 50])
        elif input_car == ALL_60:
            self.training_data = np.asmatrix([1340, 26 * 60])
            self.w_matrix = np.asmatrix([nb_proto * 10, 26 * 60])

    def setup(self, data_type):
        data = readfile('data_test.csv', data_type)
        data = np.asmatrix(data)
        self.w_matrix = data[0:10 * self.nb_of_prototypes, 1:]


    def train(self, data_type = STATIC_40):
        z = 0
        minimum_index = 0
        minimum_index_j = 0
        alpha = self.learning_rate

        data = readfile('data_train.csv', data_type)
        data = np.asmatrix(data)
        desired_values = np.asarray(data[:, 0])
        self.training_data = data[:,1:]
        for row in self.training_data:
            temp_erreur_min = 9999
            for i in range(10):
                temp_erreur_min_j = 9999
                for j in range(self.nb_of_prototypes):
                    self.v_erreur[j] = np.linalg.norm(row - self.w_matrix[self.nb_of_prototypes*i + j, :])
                    if self.v_erreur[j] <= temp_erreur_min_j:
                        temp_erreur_min_j = self.v_erreur[j]
                        minimum_index_j = j
                if self.v_erreur.min() <= temp_erreur_min:
                    temp_erreur_min = self.v_erreur.min()

                    minimum_index = i

            print("reçu :", minimum_index, "désirée :", int(desired_values.item(z)), "distance : ", temp_erreur_min)
            k = self.nb_of_prototypes
            print(temp_erreur_min)
            if minimum_index == int(desired_values.item(z)):
                self.w_matrix[minimum_index * k + minimum_index_j, :] = self.w_matrix[minimum_index * k +minimum_index_j, :] + alpha * (row - self.w_matrix[minimum_index * k + minimum_index_j, :])

            else:
                self.w_matrix[minimum_index * k + minimum_index_j, :] = self.w_matrix[minimum_index * k + minimum_index_j, :] - alpha * (row - self.w_matrix[minimum_index * k + minimum_index_j, :])
            print(np.linalg.norm(row - self.w_matrix[self.nb_of_prototypes*minimum_index + minimum_index_j, :]))
            z = z + 1
            print(z, "/1340")

    def test(self):
        data = readfile('data_train.csv', self.input_caracteristics)
        data = np.asmatrix(data)
        x_matrix = data[:, 1:]
        desired_values = np.asarray(data[:, 0])
        nb_hit = 0
        q = 0
        for row in x_matrix:
            temp_erreur_min = 9999
            for i in range(10):
                for j in range(self.nb_of_prototypes):
                    self.v_erreur[j] = np.linalg.norm(row - self.w_matrix[self.nb_of_prototypes*i + j, :])
                if self.v_erreur.min() <= temp_erreur_min:
                    temp_erreur_min = self.v_erreur.min()

                    minimum_index = i
            if minimum_index == int(desired_values.item(q)):
                nb_hit = nb_hit + 1
            q = q +1
        print("percent_hit : ", nb_hit / 1340)
        print("Époque", "Done")
        return nb_hit/1340
