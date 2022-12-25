import random
import time
import os
from prettytable import PrettyTable
import msvcrt
import tkinter as tk
import matplotlib.pyplot as plt




class settler():
    next_id = 0
    
    def __init__(self, age=None, gender=None):
        self.id = settler.next_id
        settler.next_id += 1

        if age is None:
            self.age = self.random_age()

        else: 
            self.age = age
        
        if gender is None:
            self.gender = self.random_gender()
        else:
            self.gender = gender

        self.state = True
        
    
    def show(self):
        print(f"id: {self.id}, age: {self.age}, genre: {self.gender}, etat: {self.state}")

    def random_age(self): 
        return random.randint(0, 100)

    def random_gender(self):
        return random.choice(["man", "woman"])
    
    def make_old(self):
        self.age += 1
        return  self.age
    
    def is_alive(self, proba_dead:float):
        if self.state:
            self.state = random.choice([True]*(1000-int(proba_dead)) + [False]*int(proba_dead))


def natural_death_probability(age):
    #proba pour 1000 personnes
    if age < 20:
        return 0.2
    elif age < 30:
        return 0.4
    elif age < 35:
        return 0.6
    elif age < 40:
        return 0.8
    elif age < 45:
        return 1.2
    elif age < 50:
        return 2
    elif age < 55:
        return 3.2
    elif age < 60:
        return 5
    elif age < 65:
        return 7.7
    elif age < 70:
        return 11.2
    elif age < 80:
        return 19.6
    elif age < 90:
        return 62.7
    else:
        return 200

def reproduction_probability(age):
    #proba pour 100 femmes
    if age < 20:
        return 0
    elif age < 30:
        return 11
    elif age < 35:
        return 13
    elif age < 40:
        return 7
    elif age < 50:
        return 1
    else:
        return 0

def next_day(s_list):
    
    for j in s_list:
        
        j.make_old()
        j.is_alive(natural_death_probability(j.age))
        

    s_list = [se for se in s_list if se.state]
    women_list = [se for se in s_list if se.gender == "woman"]
    for woman in women_list:
        have_baby = random.choice([False]* (100-int(reproduction_probability(woman.age))) + [True] * (int(reproduction_probability(woman.age))))
        if have_baby:
            s_list.append(settler(age = 0))
    
    return s_list

def get_table(table, s_list, rows_number):
    row_number = 0
    for row in s_list:
        if row_number > rows_number:
            return table
        if row_number < rows_number:
            table.add_row([row.id, row.age, row.gender, row.state])
            row_number += 1
        if row_number == rows_number:
            table.add_row(["...", "...", "...", "..."])
            row_number += 1
def get_graphique(x, **value):
    None

def get_max_age(s_list, init_age):
    if max(s_list, key=lambda x: x.age).age > init_age:
        return max(settlers_list, key=lambda x: x.age).age
    return init_age


initial_settlers_number = 1000
settlers_list = [settler() for i in range(initial_settlers_number)]
jour = 0
age_max = 0
os.system("cls")

table = PrettyTable()
table.field_names = ["id", "age", "gender", "state"]

root = tk.Tk()
root.geometry("480x640")
text = tk.Text(root, yscrollcommand=True)
text.pack()
scrollbar = tk.Scrollbar(root, command=text.yview)
scrollbar.pack(side="right", fill="y")
text.config(yscrollcommand=scrollbar.set)

plt.hist(jour, initial_settlers_number,alpha=0.5,color='black')
plt.show(block=False)
while len(settlers_list) > 0:
    
    
    age_max = get_max_age(settlers_list, age_max)
    
    string_to_print = "jour: " +  str(jour)
    string_to_print += "\nnombre de femmes: "+ str(len([se for se in settlers_list if se.gender == "woman"]))
    string_to_print += "\nnombre d'hommes: "+ str(len([se for se in settlers_list if se.gender == "man"]))
    string_to_print += "\nnombre d'habitants: "+ str(len(settlers_list))
    string_to_print += "\nage max atteint: "+ str(age_max)
    string_to_print += "\n" + str(get_table(table, settlers_list, 20))
    plt.hist(jour, len(settlers_list),alpha=0.5,color='black')
    plt.draw()
    text.delete("1.0", "end")
    text.insert("end", string_to_print)
    
    root.update()

    table.clear_rows()

    jour += 1
    settlers_list = next_day(settlers_list)
    
     # Si l'utilisateur appuie sur la touche espace
    if msvcrt.kbhit() and msvcrt.getch() == b' ':
        break  # on sort de la boucle

    time.sleep(0.1)
    os.system("cls")
    
