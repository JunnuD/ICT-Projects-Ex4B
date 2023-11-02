# File name tkintertest.py
# Author: Junnu Danhammer
# Description: This is the same code as in koodi.py, but i tried to implement the GUI with Tkinter.

# Not working, but tried and wanted to leave this here still. 
# Gets out an GUI block, but the buttons aren't working and also flashing weirdly. After some more messing around couldn't get it to work.
# Also 2.11. getting ModuleNotFoundError on my laptop with tkinter. Could not test it furthermore.

import tkinter as tk
from lista import my_list

# Function to add data to the list
def add_data():
    tieto = entry.get()
    my_list.append(tieto)
    entry.delete(0, tk.END)  # Clear the entry field
    update_listbox()
    action_label.config(text="Tieto lisätty listaan!")

# Function to print the list
def update_listbox():
    listbox.delete(0, tk.END)  # Clear the listbox
    for tieto in my_list:
        listbox.insert(tk.END, tieto)

# Function to print the item count on the list
def print_item_count():
    count = len(my_list)
    count_label.config(text=f'Listassa on {count} kpl tietoja')
    action_label.config(text="Listan pituus tulostettu.")

# Function to search for a specific value inside the list
def search_item():
    item_to_search = entry.get()
    found_indices = [i for i, tieto in enumerate(my_list) if tieto == item_to_search]
    if found_indices:
        result_label.config(text=f'Tieto "{item_to_search}" löytyy kohdista {", ".join(map(str, found_indices))}.')
    else:
        result_label.config(text=f'Tietoa "{item_to_search}" ei löytynyt listasta.')
    action_label.config(text="Etsintä suoritettu.")

# Function to delete item from the list
def delete_item():
    item_to_delete = entry.get()
    if item_to_delete in my_list:
        my_list.remove(item_to_delete)
        update_listbox()
        result_label.config(text=f'Tieto "{item_to_delete}" poistettu listasta.')
    else:
        result_label.config(text=f'Tietoa "{item_to_delete}" ei löytynyt listasta.')
    action_label.config(text="Tieto poistettu listasta.")

# Function to sort the list
def sort_list():
    my_list.sort(key=str.upper)
    update_listbox()
    result_label.config(text='Lista on järjestetty aakkosjärjestykseen.')
    action_label.config(text="Lista järjestetty.")

# Create a tkinter window
root = tk.Tk()
root.title("List Program")

# Create and place widgets
entry_label = tk.Label(root, text="Syötä tieto:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

add_button = tk.Button(root, text="Lisää listaan", command=add_data)
add_button.pack()

listbox = tk.Listbox(root)
listbox.pack()

update_listbox()

item_count_button = tk.Button(root, text="Tulosta listan pituus", command=print_item_count)
item_count_button.pack()

search_button = tk.Button(root, text="Etsi listasta", command=search_item)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

delete_button = tk.Button(root, text="Poista tieto listasta", command=delete_item)
delete_button.pack()

sort_button = tk.Button(root, text="Järjestä lista aakkosjärjestykseen", command=sort_list)
sort_button.pack()

action_label = tk.Label(root, text="")
action_label.pack()

# Start the tkinter main loop
root.mainloop()
