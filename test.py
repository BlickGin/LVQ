from Network import *

proto = [[0,1,1],[1,5,2],[2,2,4]]
input = [1,4]
output = 0

n = Network(proto)
n.input = input
n.output = output

n.calculate_distance()

print(n.closest_proto_from_input)

n.learn()

print(n.prototypes)