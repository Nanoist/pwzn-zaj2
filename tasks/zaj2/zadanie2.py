# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import pickle
import pathlib


def load_animals(large_dataset=False):
    """

    :param bool large_dataset: Jeśli wartość to True zwraca 1E6 zwierząt, w
                               przeciwnym razie 1E5. Test będzie odbywał się
                               przy 1E6 zwierząt.

    :return: Lista zwierząt
    """
    file_name = 'animals-small.bin' if not large_dataset else 'animals.bin'
    file = pathlib.Path(__file__).parent / file_name
    with open(str(file), 'rb') as f:
        return pickle.load(f)

def mass_generator(data):
    mass, unit = data['mass']
    if unit == 'kg':
        return mass
    if unit == 'g':
        return mass/1000
    if unit == 'mg':
        return mass/1E-6
    if unit == 'Mg':
        return mass*1000

def filter_animals(animal_list):
    """
    Jesteś informatykiem w firmie Noe Shipping And Handling. Firma ta zajmuje
    się międzykontynentalnym przewozem zwierząt.

    Dostałeś listę zwierząt które są dostępne w pobliskim zoo do transportu.

    Musisz z tej listy wybrać listę zwierząt które zostaną spakowane na statek,

    Lista ta musi spełniać następujące warunki:

    * Docelowa lista zawiera obiekty reprezentujące zwierzęta (tak jak animal_list)
    * Z każdego gatunku zwierząt (z tej listy) musisz wybrać dokładnie dwa
      egzemplarze.
    * Jeden egzemplarz musi być samicą a drugi samcem.
    * Spośród samic i samców wybierasz te o najmniejszej masie.
    * Dane w liście są posortowane względem gatunku a następnie nazwy zwierzęcia

    Wymaganie dla osób aspirujących na ocenę 5:

    * Ilość pamięci zajmowanej przez program musi być stała względem
      ilości elementów w liście zwierząt.
    * Ilość pamięci może rosnąć liniowo z ilością gatunków.

    Nie podaje schematu obiektów w tej liście, musicie radzić sobie sami
    (można podejrzeć zawartość listy w interaktywnej sesji interpretera).

    Do załadowania danych z listy możesz użyć metody `load_animals`.

    :param animal_list:
    """
    
    dict_animal = {}
    for animal in animal_list:
        key = animal['genus']
        if animal['genus'] not in dict_animal:
            dict_animal[key] = (None, None)
            if animal['sex'] == 'male':
                dict_animal[key] = (animal, None)
            else:
                dict_animal[key] = (None, animal)
        else:
            male, female = dict_animal[key]
            if animal['sex'] == 'male' and male == None:
                dict_animal[key] = (animal, female)
            if animal['sex'] == 'female' and female == None:
                dict_animal[key] = (male, animal)
            else:
                mass = mass_generator(animal)
                if male != None:
                    mass_male = mass_generator(male)
                    if mass < mass_male and animal['sex'] == 'male':
                        dict_animal[key] = (male, animal)
                else:
                    mass_female = mass_generator(female)
                    if mass < mass_female and animal['sex'] == 'female':
                        dict_animal[key] = (animal, female)
                
    print(dict_animal)
if __name__ == "__main__":
    animals = load_animals()
    
filter_animals(animals)
