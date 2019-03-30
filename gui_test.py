import pickle
import tkinter as tk  # for python 3
from tkinter import messagebox
import pygubu
import glob

from LVQ.neural_net import *


class Application:
    def __init__(self, master):

        self.net_List = []
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('Net_Ui1.ui')

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
                                        "\n\rInitialisation :"

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
        pickle.dump(self.selected_network, open(self.n.name + ".pkl", "wb"))
        pos = self.networks_listbox.curselection()
        self.networks_listbox.delete(pos)
        self.networks_listbox.insert(pos, self.n.name + "  (saved)")
    def on_load_network_click(self):
        self.builder2 = pygubu.Builder()
        self.builder2.add_from_file('Net_Ui1.ui')
        top3 = tk.Toplevel(self.mainwindow)

        self.selected_acti_type = None
        self.selected_nb_entry = None
        file_list = glob.glob1(__path__[0],'*.pkl')
        self.frame_3 = self.builder2.get_object('Load_Window', top3)
        cbox = self.builder2.get_object('load_combobox')
        cbox['values'] = file_list
    def lw_load_button_click(self):
        k=2

    def on_click_learn_button(self):
        NB_EPOQUES = 10
        n = self.selected_network
        n.setup()
        test = []
        vc = []
        x = []
        for i in range(NB_EPOQUES):
            n.learning_rate = 0.2 - (0.2 / NB_EPOQUES) * i
            n.train()
            x.append(n.test_train())
            vc.append(n.vc_test())
            test.append(n.test())

        print('Train results : ', x)
        print('VC_results : ', vc)
        print('Test_results : ', test)


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    root.mainloop()