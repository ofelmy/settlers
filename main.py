import time
import os
from prettytable import PrettyTable
import msvcrt
import tkinter as tk
import matplotlib.pyplot as plt
from functions.show import *
from functions.settlers import *
from functions.evolution import *
from vars.main import *

settlers_list = [settler() for i in range(initial_settlers_number)]
jour = 0
age_max = 0
os.system("cls")



table = PrettyTable()
table.field_names = ["id", "age", "gender", "state"]

# create root window
root = tk.Tk()
root.geometry("640x640")

frame = tk.Frame(root)

# create text zone named "data_show"
data_show = tk.Text(frame)
scrollbar = tk.Scrollbar(frame, command=data_show.yview)

# add text zone in the root windows
data_show.pack(side="left", fill="both", expand=False)
scrollbar.pack(side="right", fill="y")

data_show.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=data_show.yview)

frame.pack(fill="both", expand=True)

# plt.hist(jour, initial_settlers_number,alpha=0.5,color='black')
# plt.show(block=False)
while len(settlers_list) > 0:
    
    
    age_max = get_max_age(settlers_list, age_max)
    
    string_to_print = "jour: " +  str(jour)
    string_to_print += "\nnombre de femmes: "+ str(len([se for se in settlers_list if se.gender == "woman"]))
    string_to_print += "\nnombre d'hommes: "+ str(len([se for se in settlers_list if se.gender == "man"]))
    string_to_print += "\nnombre d'habitants: "+ str(len(settlers_list))
    string_to_print += "\nage max atteint: "+ str(age_max)
    string_to_print += "\n" + str(get_table(table, settlers_list, 20))
    # plt.hist(jour, len(settlers_list),alpha=0.5,color='black')
    # plt.draw()
    data_show.delete("1.0", "end")
    data_show.insert("end", string_to_print)
    
    root.update()

    table.clear_rows()

    jour += 1
    settlers_list = next_day(settlers_list)
    
     # Si l'utilisateur appuie sur la touche espace
    if msvcrt.kbhit() and msvcrt.getch() == b' ':
        break  # on sort de la boucle

    time.sleep(0.001)
    
