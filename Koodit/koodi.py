# File name koodi.py
# Author: Junnu Danhammer
# Description: List program that has different functionalities to do with the list.

from lista import my_list

# Function to add data to the list
def add_data():
    tieto = input('Syötä tieto: ')
    my_list.append(tieto)
    print('Tieto lisätty listaan!')
    print()

# Function to print the list
def print_list():
    print('Listan sisältö:')
    for tieto in my_list:
        print(tieto)
    print()

# Function to print the item count on the list
def print_item_count():
    count = len(my_list)
    print(f'Listassa on {count} kpl tietoja ')
    print()

# Function to search for a specific value inside the list
def search_item():
    item_to_search = input('Syötä etsittävä tieto: ')
    found = False
    for index, tieto in enumerate(my_list):
        if tieto == item_to_search:
            print(f'Tieto "{item_to_search}" löytyy listasta kohdasta {index}.')
            found = True
    if not found:
        print(f'Tietoa "{item_to_search}" ei löytynyt listasta.')
    print()


# Function to delete item from list 
def delete_item():
    print()
    item_to_delete = input('Syötä poistettava tieto: ')
    if item_to_delete in my_list:
        my_list.remove(item_to_delete)
        print(f'Tieto "{item_to_delete}" poistettu listasta.')
    else:
        print(f'Tietoa "{item_to_delete}" ei löytynyt listasta.')
    print()


# Function to sort the list. Doesnt matter if the letters are upper or lower case it wont bug.
def sort_list():
    print()
    my_list.sort(key=str.upper)
    print('Lista on järjestetty aakkosjärjestykseen.')
    print(my_list)
    print()

# Loop that will keep on going until the user ends the program
# This loop makes the program run if the user wants to add more strings to the list. 
# Also all the other functionalities are inside this loop. 

while True:
    print('Valitse toiminto: ')
    print('1. Lisää listaan tietoa ')
    print('2. Tulosta lista ')
    print('3. Tulosta listan pituus')
    print('4. Etsi listasta')
    print('5. Poista tieto listasta')
    print('6. Järjestä lista aakkosjärjestykseen')
    print('7. Lopeta ohjelma')
    print()

    valinta = input('Syötä valintasi: ')

    if valinta == '1':
        add_data()

    elif valinta == '2':
        print_list()

    elif valinta == '3':
        print_item_count()

    elif valinta == '4':
        search_item()

    elif valinta == '5':
        delete_item()
    
    elif valinta == '6':
        sort_list()

    elif valinta == '7':
        print('Ohjelma päättyy. ')
        print('Kiva kun kokeilit :) ')
        print()
        break

    else:
        print('Virheellinen valinta. Yritä uudelleen')
