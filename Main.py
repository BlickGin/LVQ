import pickle
import tkinter as tk
from tkinter import messagebox
import pygubu
import glob
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from copy import deepcopy

from LVQ.neural_net import *


#
#
#
#
#
#
#

class Application:
    def __init__(self, master):

        self.net_List = []
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('Net_Ui1.ui')
        self.root = master
        self.builder2 = pygubu.Builder()
        self.builder2.add_from_file('Net_Ui1.ui')
        self.frame_3 = None

        self.mainwindow = builder.get_object('Toplevel_2', master)
        builder.connect_callbacks(self)
        self.networks_listbox = builder.get_object('Network_list')
        self.netinfos_label = builder.get_object('Network_Infos')
        self.input_menu = builder.get_object("Number_Of_Inputs_Menu_Button")

        self.selected_network_filename = ""
        self.selected_network = None
        self.selected_nb_entry = STATIC_40
        self.selected_proto_sel = 10

        def curselect(event):
            widget = event.widget
            selection = widget.curselection()
            self.selected_network = self.net_List[selection[0]]
            self.selected_network.input_car_text = str(self.selected_network.input_caracteristics)
            car = self.selected_network.input_car_text

            if car[:2] == "12":
                car = "STATIC " + car[2:]
            else:
                car = "STATIC + DYNAMIC " + car[2:]

            txt = "Nom : " + self.selected_network.name + \
                                        "\n\rNombre de prototype : " + str(self.selected_network.nb_of_prototypes) + \
                                        "\n\rDonnées d'entrée : " + car +\
                                        "\n\rInitialisation :" +\
                                        "\n\rMeilleur résultat (test) : " + str(self.selected_network.best_performance)

            self.netinfos_label.config(text=txt)
            # percent_hit = net.vc_test()
            # draw_graph(frame_13, 1)

        self.networks_listbox.bind('<<ListboxSelect>>', curselect)
    def on_new_network_click(self):
        self.builder2 = pygubu.Builder()
        self.builder2.add_from_file('Net_Ui1.ui')
        top3 = tk.Toplevel(self.mainwindow)

        self.selected_acti_type = None
        self.selected_nb_entry = None

        self.frame_3 = self.builder2.get_object('New_Network_Window', top3)
        self.builder2.connect_callbacks(self)
    #-------------------- ON ok Click -----------------------------------------------------------
    # Une fois qu'on appuie sur le boutton Ok dans la fenêtre de création du network la fonction
    # définie une liste des paramètres d'entrées
    #--------------------------------------------------------------------------------------------
    def on_click_nnw_ok_button(self):
        name_input = self.builder2.get_object('Network_Name_Entry').get()
        Number_Of_Prototypes = int(self.builder2.get_object('Number_Of_Prototypes_Entry').get())
        nb_input = self.selected_nb_entry

        self.builder2.connect_callbacks(self)
        token = 1
        if name_input != "":
            for i in self.networks_listbox.get(0, self.networks_listbox.size()):
                if i == name_input :
                    token = 0
            if token == 1:
                self.networks_listbox.insert(tk.END, name_input)
                n = neural_net(Number_Of_Prototypes, nb_input)
                self.net_List.append(n)
                n.name = name_input
            else:
                tk.messagebox.showinfo("Error", "A network with this name already exist")
        else:
            tk.messagebox.showinfo("Error", "Please enter a network name")
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
    def on_click_nnw_cancel_button(self):
        self.frame_3.master.destroy()
    def on_delete_network_click(self):
        select = self.networks_listbox.curselection()
        self.net_List.pop(select[0])
        self.networks_listbox.delete(select)
    def on_save_network_click(self):
        pickle.dump(self.selected_network, open(self.selected_network.name + ".pkl", "wb"))
        pos = self.networks_listbox.curselection()
        self.networks_listbox.delete(pos)
        self.networks_listbox.insert(pos, self.selected_network.name + "  (saved)")
    def on_load_network_click(self):
        self.builder2 = pygubu.Builder()
        self.builder2.add_from_file('Net_Ui1.ui')
        top3 = tk.Toplevel(self.mainwindow)
        file_list = glob.glob1(".", '*.pkl')
        self.frame_3 = self.builder2.get_object('Load_Window', top3)
        self.builder2.connect_callbacks(self)
        cbox = self.builder2.get_object('load_combobox')
        cbox['values'] = file_list
    def lw_load_button_click(self):
        cbox = self.builder2.get_object('load_combobox')
        with open(cbox.get(), 'rb') as pickle_file:
            net = pickle.load(pickle_file)
        self.net_List.append(net)
        self.networks_listbox.insert(tk.END, net.name + "  (Loaded)")
        self.frame_3.master.destroy()
    def on_click_learn_button(self):
        self.builder2 = pygubu.Builder()
        self.builder2.add_from_file('Net_Ui1.ui')
        top3 = tk.Toplevel(self.mainwindow)
        self.frame_3 = self.builder2.get_object('Learn_Window', top3)
        self.builder2.connect_callbacks(self)
    def On_Click_LW_button(self):
        ep_user_input = self.builder2.get_object("Nb_Epoques_Entry")
        NB_EPOQUES = int(ep_user_input.get())
        app_user_input = self.builder2.get_object("Taux_App_Entry")
        alpha = float(app_user_input.get())
        n = self.selected_network
        temp_best_performance = n.best_performance
        if not n.train_status:
            n.setup()
            n.train_status = 1
        test = []
        vc = []
        x = []
        for i in range(NB_EPOQUES):
            n.learning_rate = alpha - (alpha / NB_EPOQUES) * i
            n.train()
            x.append(n.test_train())
            vc.append(n.vc_test())
            test.append(n.test())
            self.draw_graph(self.builder2.get_object('Frame_13'), x,vc,test)
            self.root.update()
            if test[i] > temp_best_performance:
                temp_best_performance = test[i]
                n.best_w_matrix = deepcopy(n.w_matrix)
        self.frame_3.master.destroy()
        n.best_performance = temp_best_performance
        self.selected_network = n
        print('Train results : ', x)
        print('VC_results : ', vc)
        print('Test_results : ', test)
        print("Meilleur performance : ", n.best_performance, " %")
    def on_click_test_button(self):
        n = self.selected_network
        n.test()
    def on_click_load_w(self):
        self.selected_network.w_matrix = self.selected_network.best_w_matrix
    def on_click_export_button(self):
        numpy.savetxt(self.selected_network.name + ".csv", self.selected_network.best_w_matrix, delimiter=",")
    def draw_graph(self,frame, train_error_values, vc_error_values, test_error_values):
        fig = plt.figure(1)
        plt.ion()
        t = list(range(len(train_error_values)))
        x1 = train_error_values
        x2 = vc_error_values
        x3 = test_error_values
        fig.clear()
        plt.plot(t, x1, marker='', color='skyblue', label="learning")
        plt.plot(t, x2, marker='', color='red', label="vc")
        plt.plot(t, x3, marker='', color='green', label="test")
        plt.xlabel("nb d'époques")
        plt.ylabel("% de réussite")
        plt.legend()

        canvas = FigureCanvasTkAgg(fig, master=frame)
        plot_widget = canvas.get_tk_widget()

        plot_widget.grid(row=0, column=0)

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()