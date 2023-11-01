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

def print_item_count():
    count = len(my_list)
    print(f'Listassa on {count} kpl tietoja ')

while True:
    print()
    print('Valitse toiminto: ')
    print('1. Lisää listaan tietoa ')
    print('2. Tulosta lista ')
    print('3. Tulosta listan pituus')
    print('4. Lopeta ohjelma')
    print()

    valinta = input('Syötä valintasi: ')

    if valinta == '1':
        add_data()

    elif valinta == '2':
        print_list()

    elif valinta == '3':
        print_item_count()

    elif valinta == '4':
        print('Ohjelma päättyy. ')
        print()
        break

    else:
        print('Virheellinen valinta. Yritä uudelleen')
