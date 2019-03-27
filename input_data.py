
import random
from Defines import *

nb2output = {0.0: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             1.0: [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             2.0: [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             3.0: [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
             4.0: [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             5.0: [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             6.0: [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
             7.0: [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             8.0: [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
             9.0: [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]}


def readfile(filename, choix):

    data = []

    for line in open(filename):
        csv_row = line.split(";")
        for column, item in enumerate(csv_row):
            csv_row[column] = float(item)
        csv_data_row = organise_tableau_lab3(csv_row, choix)
        data.append(csv_data_row)

    random.shuffle(data)
    return data


def organise_tableau_lab3(row_data, choix):

    # choix/ 1240: statiques/40 ; 1250: statiques/50 ; 1260: statiques/60 ; 2640: tous/40; 2650: tous/50; 2660: tous/60;
    filtered_row_data = []
    filtered_row_data.append(row_data[0])
    if choix == STATIC_40:
        row_data = row_data[:(1 + 40 * 26)]
        row_data = row_data[1:]
        while len(row_data) != 0:
            for index in range(12):
                filtered_row_data.append(row_data[index])
            row_data = row_data[26:]
    elif choix == STATIC_50:
        row_data = row_data[:(1 + 50 * 26)]
        row_data = row_data[1:]
        while len(row_data) != 0:
            for index in range(12):
                filtered_row_data.append(row_data[index])
            row_data = row_data[26:]
    elif choix == STATIC_60:
        row_data = row_data[1:]
        while len(row_data) != 0:
            for index in range(12):
                filtered_row_data.append(row_data[index])
            row_data = row_data[26:]
    elif choix == ALL_40:
        filtered_row_data = row_data[:(1 + 40 * 26)]
    elif choix == ALL_50:
        filtered_row_data = row_data[:(1 + 50 * 26)]
    elif choix == ALL_60:
        filtered_row_data = row_data
    else:
        print("Erreur: config mal choisie")

#    filtered_row_data[0] = nb2output[filtered_row_data[0]]
    filtered_row_data[0] = int(filtered_row_data[0])
    return filtered_row_data


def choose_prototype(filtered_data, k, method):
    prototypes = []
    k_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in filtered_data:
        if i[0] == 0.0 and k_counter[0] < k:
            prototypes.append(i)
            k_counter[0] += 1
        if i[0] == 1.0 and k_counter[1] < k:
            prototypes.append(i)
            k_counter[1] += 1
        if i[0] == 2.0 and k_counter[2] < k:
            prototypes.append(i)
            k_counter[2] += 1
        if i[0] == 3.0 and k_counter[3] < k:
            prototypes.append(i)
            k_counter[3] += 1
        if i[0] == 4.0 and k_counter[4] < k:
            prototypes.append(i)
            k_counter[4] += 1
        if i[0] == 5.0 and k_counter[5] < k:
            prototypes.append(i)
            k_counter[5] += 1
        if i[0] == 6.0 and k_counter[6] < k:
            prototypes.append(i)
            k_counter[6] += 1
        if i[0] == 7.0 and k_counter[7] < k:
            prototypes.append(i)
            k_counter[7] += 1
        if i[0] == 8.0 and k_counter[8] < k:
            prototypes.append(i)
            k_counter[8] += 1
        if i[0] == 9.0 and k_counter[9] < k:
            prototypes.append(i)
            k_counter[9] += 1

    return prototypes

# data = readfile('data_train.csv', STATIC_40)
# prot = choose_prototype(data, int(input("k= ")))
# print(prot)


# k_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in prot:
#     if i == 0.0:
#         k_counter[0] += 1
#     if i == 1.0:
#         k_counter[1] += 1
#     if i == 2.0:
#         k_counter[2] += 1
#     if i == 3.0:
#         k_counter[3] += 1
#     if i == 4.0:
#         k_counter[4] += 1
#     if i == 5.0:
#         k_counter[5] += 1
#     if i == 6.0:
#         k_counter[6] += 1
#     if i == 7.0:
#         k_counter[7] += 1
#     if i == 8.0:
#         k_counter[8] += 1
#     if i == 9.0:
#         k_counter[9] += 1
# print(k_counter)
# start = time.time()
# data = readfile('data_test.csv', 1240)
# data2 = readfile('data_test.csv', 1250)
# data3 = readfile('data_test.csv', 1260)
# data4 = readfile('data_test.csv', 2640)
# data5 = readfile('data_test.csv', 2650)
# data6 = readfile('data_test.csv', 2660)
#
# print("len1240:")
# print((len(data[0])-1)/40, len(data))
# print("len1250:")
# print((len(data2[0])-1)/50, len(data2))
# print("len1260:")
# print((len(data3[0])-1)/60, len(data3))
# print("len2640:")
# print((len(data4[0])-1)/40, len(data4))
# print("len2650:")
# print((len(data5[0])-1)/50, len(data5))
# print("len2660:")
# print((len(data6[0])-1)/60, len(data6))
#
#
# end = time.time()
#
# data_ges = []
# data_ges.append(data[0])
# data_ges.append(data2[0])
# data_ges.append(data3[0])
# data_ges.append(data4[0])
# data_ges.append(data5[0])
# data_ges.append(data6[0])
#
#
# print(data_ges[0][:26])
# print(data_ges[1][:26])
# print(data_ges[2][:26])
#
# print(data_ges[3][:26])
# print(data_ges[4][:26])
# print(data_ges[5][:26])
#
