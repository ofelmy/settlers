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
