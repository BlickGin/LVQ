from LVQ.neural_net import *
x = np.zeros(40)
vc = np.zeros(40)
test = np.zeros(40)
n = neural_net(20, ALL_60, 0.1)
n.setup(ALL_60)

for i in range(40):
    n.learning_rate = 0.1 -0.0025*i
    n.train(ALL_60)
    x[i] = n.test_train()
    vc[i] = n.vc_test()
    test[i] = n.test()

    print('Train results : ', x)
    print('VC_results : ', vc)
    print('Test_results : ', test)