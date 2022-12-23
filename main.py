import random

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
initial_settlers_number = 100
settlers_list = []

settlers_list = [settler() for i in range(initial_settlers_number)]

for i in range(100):

    print("jour: ", i)

    for j in settlers_list:
        
        j.make_old()
        j.is_alive(natural_death_probability(j.age))
        j.show()

    settlers_list = [se for se in settlers_list if se.state]
    women_list = [se for se in settlers_list if se.gender == "woman"]
    for woman in women_list:
        have_baby = int(random.choice([False]* (100-int(reproduction_probability(woman.age))) + [True] * (int(reproduction_probability(woman.age)))))
        if have_baby:
            settlers_list.append(settler(age = 0))

    print("-"* 10)
