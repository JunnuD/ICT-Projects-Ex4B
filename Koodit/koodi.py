from lista import my_list

# Function to add data to the list
def add_data():
    tieto = input('Syötä tieto: ')
    my_list.append(tieto)
    print('Tieto lisätty listaan!')

# Function to print the list
def print_list():
    print('Listan sisältö:')
    for tieto in my_list:
        print(tieto)

# Function to print the item count on the list
def print_item_count():
    count = len(my_list)
    print(f'Listassa on {count} kpl tietoja ')

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

# Loop that will keep on going until the user ends the program
# This loop makes the program run if the user wants to add more strings to the list. 
# Also all the other functionalities are inside this loop. 

while True:
    print()
    print('Valitse toiminto: ')
    print('1. Lisää listaan tietoa ')
    print('2. Tulosta lista ')
    print('3. Tulosta listan pituus')
    print('4. Etsi listasta')
    print('5. Lopeta ohjelma')
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
        print('Ohjelma päättyy. ')
        print()
        break

    else:
        print('Virheellinen valinta. Yritä uudelleen')
