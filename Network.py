
class Network(object):
    def __init__(self, number_of_proto, learning_rate=0.2):
        self.learning_rate = learning_rate
        self.number_of_proto = number_of_proto
        self.prototypes = []
        self.proto_selection_method = 1
        self.input = []
        self.output = []
        self.error_count = []
        self.datatype = 0
        self.epoch = 0
        self.closest_proto_from_input = None
        self.name = None
        self.vc_errors = 0

    def calculate_distance(self):
        last_closer = None
        best_euclidian_sum = None

        for i in self.prototypes:
            euclidian_sum = 0
            for j in range(len(i)-1):
                euclidian_sum += ((i[j+1]) - self.input[j]) * ((i[j+1]) - self.input[j])

            if best_euclidian_sum is None:
                best_euclidian_sum = euclidian_sum
                last_closer = i
            elif best_euclidian_sum > euclidian_sum:
                best_euclidian_sum = euclidian_sum
                last_closer = i

        self.closest_proto_from_input = last_closer

    def learn(self):
        index_of_closest = self.prototypes.index(self.closest_proto_from_input)
        if self.prototypes[index_of_closest][0] is self.output:
            for i in range(len(self.prototypes[index_of_closest]) - 1):
                delta = self.learning_rate * (self.input[i] - self.prototypes[index_of_closest][i+1])
                self.prototypes[index_of_closest][i+1] += delta
        else:
            for i in range(len(self.prototypes[index_of_closest]) - 1):
                delta = self.learning_rate * (self.input[i] - self.prototypes[index_of_closest][i+1])
                self.prototypes[index_of_closest][i+1] -= delta

        if self.epoch == 10:
            self.epoch = 0
            self.learning_rate = self.learning_rate * 0.8

