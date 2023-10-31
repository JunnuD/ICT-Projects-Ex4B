from lista import my_list

# USE FUNCTIONS !!!!!



while True:
    print('Valitse toiminto: ')
    print('1. Lisää listaan tietoa ')
    print('2. Tulosta lista ')
    print('3. Lopeta ohjelma')

    valinta = input('Syötä valintasi: ')

    if valinta == '1':
        tieto = input('Syötä tieto: ')
        my_list.append(tieto)
        print('Tieto lisätty listaan! ')

    elif valinta == '2':
        print('Listan sisältö: ')
        for tieto in my_list:
            print(tieto)

    elif valinta == '3':
        print('Ohjelma päättyy. ')
        break

    else: 
        print('Virheellinen valinta. Yritä uudelleen')
