from functions.settlers import *
from functions.proba import *
from functions.measure import *
import random

@measure_time
def next_day(s_list):
    
    for j in s_list:
        
        j.make_old()
        j.is_alive(natural_death_probability(j.age))

    s_list = [se for se in s_list if se.state]
    
    for human in s_list:
        if human.gender == 'woman':
            proba = reproduction_probability(human.age)/100
            have_baby = random.random() < proba
            if have_baby:
                s_list.append(settler(age = 0))
    return s_list