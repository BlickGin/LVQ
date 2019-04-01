import numpy as np
try:
    from input_data import *
except:
    from LVQ.input_data import *

# -------------------- Class Neural_net -----------------------------------------------------------------
#
#          Class du réseau de neuronnes, s'initialise avec le nb_prototypes, la caractérstique des
#          données d'entrées et le taux d'apprentissage (Optionel)
#
#               L'objet agit comme conteneur pour la matrice de poids, les données d'entrainement
#               de validation croisé et de test. Ces méthodes sont l'ensemble de traitement qui
#               seront effectués sur ces donnés.
#
#               L'objet Neural_net possede les fonctions suivantes :
#                           1. Setup(init_poids)
#                           2. Train()
#                           3. test_train()
#                           4. vc_test()
#                           5. Test()
#                           6. add_x(x_list)
#                           7. add_vc(vc_list)
#                           8. add_test(test_list)
# -------------------------------------------------------------------------------------------------------
class neural_net():
    def __init__(self, nb_proto, input_car, base_learning_rate=0.1):

        self.nb_epoques = 0
        self.input_matrix = []
        self.input_caracteristics = input_car

        self.input_car_text = "STATIC_40"
        self.nb_of_prototypes = nb_proto
        self.v_erreur = np.zeros(int(nb_proto))

        self.learning_rate = base_learning_rate
        self.name = "Empty"
        self.train_status = 0

        self.best_performance = 0
        self.x = []
        self.vc = []
        self.test = []
        # initialisation des matrices en fonction de l'entrée
        if input_car == STATIC_40:

            self.training_data = np.asmatrix([1340, 12 * 40])
            self.vc_data = np.asmatrix([120, 12 * 40])
            self.test_data = np.asmatrix([1340, 12 * 40])
            self.w_matrix = np.asmatrix(np.random.rand(self.nb_of_prototypes * 10, 12 * 40))

        elif input_car == STATIC_50:

            self.training_data = np.asmatrix([1340, 12 * 50])
            self.w_matrix = np.asmatrix(np.random.rand(self.nb_of_prototypes * 10, 12 * 50))
            self.vc_data = np.asmatrix([120, 12 * 40])
            self.test_data = np.asmatrix([1340, 12 * 50])

        elif input_car == STATIC_60:

            self.training_data = np.asmatrix([1340, 12 * 60])
            self.w_matrix = np.asmatrix(np.random.rand(self.nb_of_prototypes * 10, 12 * 60))
            self.vc_data = np.asmatrix([120, 12 * 60])
            self.test_data = np.asmatrix([1340, 12 * 60])
        elif input_car == ALL_40:

            self.training_data = np.asmatrix([1340, 26 * 40])
            self.w_matrix = np.asmatrix(np.random.rand(self.nb_of_prototypes * 10, 26 * 40))
            self.vc_data = np.asmatrix([120, 26 * 40])
            self.test_data = np.asmatrix([1340, 26 * 40])

        elif input_car == ALL_50:

            self.training_data = np.asmatrix([1340, 26 * 50])
            self.w_matrix = np.asmatrix(np.random.rand(self.nb_of_prototypes * 10, 26 * 50))
            self.vc_data = np.asmatrix([120, 26 * 50])
            self.test_data = np.asmatrix([1340, 26 * 50])

        elif input_car == ALL_60:

            self.training_data = np.asmatrix([1340, 26 * 60])
            self.w_matrix = np.asmatrix(np.random.rand(self.nb_of_prototypes*10, 26 * 60))
            self.vc_data = np.asmatrix([120, 26 * 60])
            self.test_data = np.asmatrix([1340, 26 * 60])

        self.best_w_matrix = self.w_matrix
    # -------------------- setup ---------------------------------------------------------------
    #
    #          initialise les poids si le type d'initialisation est différent de Random
    #
    # -------------------------------------------------------------------------------------------
    def setup(self, selected_proto_sel):
        # l'objet ouvre les 3 fichiers pour les garder dans la mémoire vive de l'ordinateur
        data = readfile('data_train.csv', self.input_caracteristics)
        vc_data = readfile('data_vc.csv', self.input_caracteristics)
        test_data = readfile('data_test.csv', self.input_caracteristics)


        if selected_proto_sel < 3:
            self.w_matrix = np.asmatrix(choose_prototype(data, self.nb_of_prototypes, selected_proto_sel))
        test_data = np.asmatrix(test_data)

        self.training_data = np.asmatrix(data)
        self.vc_data = np.asmatrix(vc_data)
        self.test_data = np.asmatrix(test_data)


    # -------------------- train ---------------------------------------------------------------
    #
    #          on entraine le réseau en comparant les données d'apprentissage avec les proto.
    #
    # -------------------------------------------------------------------------------------------
    def train(self):

        z = 0
        minimum_index = 0
        minimum_index_j = 0

        alpha = self.learning_rate

        np.random.shuffle(self.training_data)
        desired_values = np.asarray(self.training_data[:, 0])
        data = self.training_data[:, 1:]
        # Pour chaque donnée d'entrée on trouve le prototype le plus proche.
        # Si le prototype est dans la bonne classe on diminue la distance entre
        # la donnée et le prototype, sinon on éloigne le prototype de la donnée.
        # la valeur de i représente la classe tandis que la valeur de j
        # est l'index du prototype dans la classe.
        for row in data:
            temp_erreur_min = 9999
            temp_erreur_min_j = 9999
            for i in range(10):
                for j in range(self.nb_of_prototypes):
                    self.v_erreur[j] = np.linalg.norm(row - self.w_matrix[self.nb_of_prototypes * i + j, :])
                    if self.v_erreur[j] <= temp_erreur_min_j:
                        temp_erreur_min_j = self.v_erreur[j]
                        minimum_index_j = j
                if self.v_erreur.min() <= temp_erreur_min:
                    temp_erreur_min = self.v_erreur.min()

                    minimum_index = i

            print("reçu :", minimum_index, "désirée :", int(desired_values.item(z)), "distance : ", temp_erreur_min)
            k = self.nb_of_prototypes
            print(np.linalg.norm(row - self.w_matrix[self.nb_of_prototypes * minimum_index + minimum_index_j, :]))

            # Ajustement des poids du prototype j de la classe i
            if minimum_index == int(desired_values.item(z)):
                self.w_matrix[minimum_index * k + minimum_index_j, :] = \
                    self.w_matrix[minimum_index * k + minimum_index_j,:] + \
                    alpha * (row - self.w_matrix[minimum_index * k + minimum_index_j,:])
            else:
                self.w_matrix[minimum_index * k + minimum_index_j, :] = \
                    self.w_matrix[minimum_index * k + minimum_index_j,:] - \
                    alpha * (row - self.w_matrix[minimum_index * k + minimum_index_j,:])


            print(np.linalg.norm(row - self.w_matrix[self.nb_of_prototypes * minimum_index + minimum_index_j, :]))
            z = z + 1
            print(z, "/1340")
    # -------------------- test_train ------------------------------------------------------------
    #
    #          Retourne le % de réussite sur les données d'entrainement
    #
    # -------------------------------------------------------------------------------------------
    def test_train(self):
        np.random.shuffle(self.training_data)
        x_matrix = np.asmatrix(self.training_data)
        desired_values = np.asarray(x_matrix[:, 0])
        x_matrix = x_matrix[:, 1:]
        nb_hit = 0
        q = 0
        minimum_index = 0
        for row in x_matrix:
            temp_erreur_min = 9999
            for i in range(10):
                for j in range(self.nb_of_prototypes):
                    self.v_erreur[j] = np.linalg.norm(row - self.w_matrix[self.nb_of_prototypes * i + j, :])
                if self.v_erreur.min() <= temp_erreur_min:
                    temp_erreur_min = self.v_erreur.min()

                    minimum_index = i
            if minimum_index == int(desired_values.item(q)):
                nb_hit = nb_hit + 1
            q = q + 1
        print("percent_hit (Train): ", nb_hit / 1340 * 100)
        return nb_hit / 1340 * 100



    # -------------------- vc_test --------------------------------------------------------------
    #
    #          Retourne le % de réussite sur les données de validation croisée
    #
    # -------------------------------------------------------------------------------------------
    def vc_test(self):
        np.random.shuffle(self.vc_data)
        x_matrix = np.asmatrix(self.vc_data)
        desired_values = np.asarray(x_matrix[:, 0])
        x_matrix = x_matrix[:, 1:]
        nb_hit = 0
        q = 0
        minimum_index = 0
        for row in x_matrix:
            temp_erreur_min = 9999
            for i in range(10):
                for j in range(self.nb_of_prototypes):
                    self.v_erreur[j] = np.linalg.norm(row - self.w_matrix[self.nb_of_prototypes * i + j, :])
                if self.v_erreur.min() <= temp_erreur_min:
                    temp_erreur_min = self.v_erreur.min()

                    minimum_index = i
            if minimum_index == int(desired_values.item(q)):
                nb_hit = nb_hit + 1
            q = q + 1
        print("percent_hit (VC): ", nb_hit / 120 * 100)
        return nb_hit / 120 * 100

    # -------------------- Test ------------------------------------------------------------
    #
    #          Retourne le % de réussite sur les données de test
    #
    # -------------------------------------------------------------------------------------------
    def Test(self):
        np.random.shuffle(self.test_data)
        x_matrix = np.asmatrix(self.test_data)
        desired_values = np.asarray(x_matrix[:, 0])
        x_matrix = x_matrix[:, 1:]
        nb_hit = 0
        q = 0
        minimum_index = 0
        for row in x_matrix:
            temp_erreur_min = 9999
            for i in range(10):
                for j in range(self.nb_of_prototypes):
                    self.v_erreur[j] = np.linalg.norm(row - self.w_matrix[self.nb_of_prototypes * i + j, :])
                if self.v_erreur.min() <= temp_erreur_min:
                    temp_erreur_min = self.v_erreur.min()

                    minimum_index = i
            if minimum_index == int(desired_values.item(q)):
                nb_hit = nb_hit + 1
            q = q + 1
        print("percent_hit (test): ", nb_hit / 780 * 100)
        return nb_hit / 780 * 100
    # -------------------- add ------------------------------------------------------------
    #
    #          Ajoute a un array dans l'objet pour la construction du graphique
    #
    # -------------------------------------------------------------------------------------
    def add_x(self, x):
        self.x = self.x + x
    def add_vc(self, vc):
        self.vc = self.vc + vc
    def add_test(self,test):
        self.test = self.test + test
