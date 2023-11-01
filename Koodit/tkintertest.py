import tkinter as tk
from lista import my_list

def add_data():
    tieto = entry.get()
    my_list.append(tieto)
    entry.delete(0, 'end')
    result_label.config(text='Tieto lisätty listaan!')

def print_list():
    listbox.delete(0, 'end')
    for tieto in my_list:
        listbox.insert('end', tieto)

def search_item():
    item_to_search = search_entry.get()
    found = False
    for index, tieto in enumerate(my_list):
        if tieto == item_to_search:
            result_label.config(text=f'Tieto "{item_to_search}" löytyy listasta kohdasta {index}.')
            found = True
    if not found:
        result_label.config(text=f'Tietoa "{item_to_search}" ei löytynyt listasta.')

root = tk.Tk()
root.title("List Application")

entry_label = tk.Label(root, text="Syötä tieto:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

add_button = tk.Button(root, text="Lisää listaan", command=add_data)
add_button.pack()

listbox = tk.Listbox(root)
listbox.pack()

print_button = tk.Button(root, text="Tulosta lista", command=print_list)
print_button.pack()

search_label = tk.Label(root, text="Etsi tieto:")
search_label.pack()

search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="Etsi listasta", command=search_item)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

quit_button = tk.Button(root, text="Lopeta ohjelma", command=root.quit)
quit_button.pack()

root.mainloop()
