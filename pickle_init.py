from main import  *
from save_load import *
from Network import *

dict_of_networks = {}
name = "Test 1A (Static 40 SIG 2 layers)"
proto = [[0,1,1],[1,5,2],[2,2,4]]
input = [1,4]
output = 0

net = Network(3)
net.prototypes = proto
net.input = input
net.output = output

net.name = name
net.datafile = 480


fname = "Network_1.pkl"
dict_of_networks[fname] = name
save(net, fname)
save(dict_of_networks, 'Network_List.pkl')