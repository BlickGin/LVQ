# ELE767 Lab 2

from LVQ.input_data import *


import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use("TkAgg")
import tkinter as tk
from tkinter import messagebox

import numpy as np
import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import figure
from matplotlib import axes
import pygubu
import pickle
from LVQ.save_load import *
from LVQ.input_data import *
from LVQ.Network import *
from LVQ.neural_net import *


class Dialog:
    def __init__(self, master, text, variable):
        top = self.top = tk.Toplevel(master)
        self.variable = None

        tk.Label(top, text=text).pack()

        self.e = tk.Entry(top)
        self.e.pack(padx=5)

        b = tk.Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        self.variable = self.e.get()
        self.top.destroy()


def draw_graph(frame, error_values):
    fig = plt.figure(1)
    plt.ion()
    t = list(range(len(error_values)))
    s = error_values
    fig.clear()
    plt.plot(t, s)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    plot_widget = canvas.get_tk_widget()

    plot_widget.grid(row=0, column=0)


class Application:
    def __init__(self, master):
        self.nb_of_networks = 0
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('main.ui')

        self.builder2 = builder2 = pygubu.Builder()
        self.builder2.add_from_file('main.ui')
        self.frame_3 = None

        self.mainwindow = builder.get_object('Toplevel_2', master)
        builder.connect_callbacks(self)
        master.protocol("WM_DELETE_WINDOW", self.on_close_window)

        self.selected_network_filename = ""
        self.selected_network = None
        self.selected_nb_entry = STATIC_40
        self.selected_proto_sel = 0

        # Gère la sélection d'un item dans la liste
        def curselect(event):
            widget = event.widget
            selection = widget.curselection()
            picked = widget.get(selection[0])
            net = load(picked)
            self.selected_network_filename = picked
            self.selected_network = net
            txt = "Nom : " + net.name + "\n\r" \
                                        "Nombre de prototype : " + str(net.nb_of_prototypes)

            self.netinfos_label.config(text=txt)
            #percent_hit = net.vc_test()
            # draw_graph(frame_13, 1)

        self.networks_listbox = net_lbox = builder.get_object('Network_list')
        self.networks_listbox.bind('<<ListboxSelect>>', curselect)

        self.netinfos_label = net_infos = builder.get_object('Network_Infos')

        # self.graph_win = graph_win = builder.get_object('Graphics')
        # graph_win.pack()

        self.frame_13 = frame_13 = builder.get_object('Frame_13')

        self.list_of_networks = {}
        self.list_of_networks_name = 'Network_List.pkl'
        builder.connect_callbacks(self)

        self.list_of_networks = load(self.list_of_networks_name)
        self.nb_of_networks = len(self.list_of_networks)

        net_lbox.select_clear(tk.END)
        for i in self.list_of_networks:
            text = i
            net_lbox.insert(tk.END, text)
        net_lbox.see(tk.END)
        net_lbox.selection_set(tk.END)

    def on_close_window(self, event=None):
        print("closed")
        self.mainwindow.master.destroy()
        exit()

    def on_new_network_click(self):
        self.builder2 = builder2 = pygubu.Builder()
        self.builder2.add_from_file('main.ui')
        top3 = tk.Toplevel(self.mainwindow)
        self.selected_acti_type = None
        self.selected_nb_entry = None

        self.frame_3 = self.builder2.get_object('New_Network_Window', top3)
        self.builder2.connect_callbacks(self)

    def on_ok_click(self):
        good_data = False

        name_input = 0
        number_of_prototypes = 0
        nb_input = 0

        name_input_entry = self.builder2.get_object('Network_Name_Entry')
        Number_Of_Prototypes_Entry = self.builder2.get_object('Number_Of_Prototypes_Entry')
        # data_path_entry = self.builder2.get_object('Data_File_Input')

        name_input = name_input_entry.get()
        number_of_prototypes = Number_Of_Prototypes_Entry.get()
        nb_input = self.selected_nb_entry
        method = self.selected_proto_sel
        # data_path = data_path_entry.cget('path')

        try:
            number_of_prototypes = int(number_of_prototypes)
            try:
                nb_input = int(nb_input)
                good_data = True
            except ValueError:
                messagebox.showwarning("Wrong Type Entry", "Please enter an integer for the number of inputs")
        except ValueError:
            messagebox.showwarning("Wrong Type Entry", "Please enter an integer for the number of prototypes")

        if good_data is True:
            if name_input is "":
                messagebox.showwarning("Wrong Type Entry", "Please enter a name")
            else:
                print(name_input)
                print(number_of_prototypes)
                print(nb_input)
                net = neural_net(number_of_prototypes,nb_input) #Network(number_of_prototypes)
                net.name = name_input
                net.setup()
                #net.proto_selection_method = method

                self.nb_of_networks += 1
                fname = "Network_" + str(self.nb_of_networks) + ".pkl"
                self.list_of_networks[fname] = name_input
                save(net, fname)
                save(self.list_of_networks, self.list_of_networks_name)

                self.networks_listbox.delete(0, tk.END)
                self.networks_listbox.select_clear(tk.END)



                for i in self.list_of_networks:
                    text = i
                    self.networks_listbox.insert(tk.END, text)
                self.networks_listbox.see(tk.END)
                self.networks_listbox.selection_set(tk.END)

                self.frame_3.master.destroy()

    def on_selected_entry(self, selection):
        if selection == 'Input_Type_1':
            self.selected_nb_entry = STATIC_40
        elif selection == 'Input_Type_2':
            self.selected_nb_entry = STATIC_50
        elif selection == 'Input_Type_3':
            self.selected_nb_entry = STATIC_60
        elif selection == 'Input_Type_4':
            self.selected_nb_entry = ALL_40
        elif selection == 'Input_Type_5':
            self.selected_nb_entry = ALL_50
        elif selection == 'Input_Type_6':
            self.selected_nb_entry = ALL_60

    def on_selected_method(self, selection):
        if selection == 'method_1':
            self.selected_proto_sel = FIRST_K
        elif selection == 'method_2':
            self.selected_proto_sel = ARITH_MEAN
        elif selection == 'method_3':
            self.selected_proto_sel = RANDOM_K_PICK

    def on_click_learn_button(self):
        NB_EPOQUES = 10

        n = self.selected_network
        x = np.zeros(NB_EPOQUES)
        vc = np.zeros(NB_EPOQUES)
        test = np.zeros(NB_EPOQUES)


        for i in range(NB_EPOQUES):
            n.learning_rate = 0.2 - (0.2 / NB_EPOQUES) * i
            n.train()
            x[i] = n.test_train()
            vc[i] = n.vc_test()
            test[i] = n.test()
            draw_graph(self.frame_13, x)

        print('Train results : ', x)
        print('VC_results : ', vc)
        print('Test_results : ', test)

        fname = self.selected_network_filename
        self.list_of_networks[fname] = n.name
        save(n, fname)

        self.networks_listbox.delete(0, tk.END)
        self.networks_listbox.select_clear(tk.END)
        for i in self.list_of_networks:
            text = i
            self.networks_listbox.insert(tk.END, text)
        self.networks_listbox.see(tk.END)
        self.networks_listbox.selection_set(tk.END)

    def on_click_test_button(self):
        n = self.selected_network
        dataset = 0

        if n.datatype == 480:
            dataset = STATIC_40
        elif n.datatype == 600:
            dataset = STATIC_50
        elif n.datatype == 720:
            dataset = STATIC_60
        elif n.datatype == 1040:
            dataset = ALL_40
        elif n.datatype == 1300:
            dataset = ALL_50
        elif n.datatype == 1560:
            dataset = ALL_60

        shuffled_input_test = readfile('data_train.csv', dataset)

        test_erreur_count = 0
        test_erreur = []

        for j in shuffled_input_test:
            n.input = j[1:]
            n.output = j[0]
            n.calculate_distance()

            out = n.closest_proto_from_input[0]

            if out is not n.output:
                test_erreur_count += 1

        # text = ""
        # for i in test_erreur:
        #     text = text + str(i) + "\n\r"

        messagebox.showinfo("Rapport d'erreurs", "Nombre d'erreurs : " + str(test_erreur_count)
                            # + "\n\r"
                            # + "Liste des erreurs :\n\r"
                            # + text
                            )


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
