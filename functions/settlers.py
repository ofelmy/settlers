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
            proba = proba_dead/1000
            self.state = random.random() > proba