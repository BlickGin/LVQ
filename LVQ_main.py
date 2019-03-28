from LVQ.neural_net import *
NB_EPOQUES = 10
T_DONNEES = ALL_60
NB_PROTO = 20
x = np.zeros(NB_EPOQUES)
vc = np.zeros(NB_EPOQUES)
test = np.zeros(NB_EPOQUES)
n = neural_net(NB_PROTO, T_DONNEES, 0.1)
n.setup()

for i in range(NB_EPOQUES):
    n.learning_rate = 0.2 - (0.2/NB_EPOQUES)*i
    n.train()
    x[i] = n.test_train()
    vc[i] = n.vc_test()
    test[i] = n.test()

print('Train results : ', x)
print('VC_results : ', vc)
print('Test_results : ', test)