import tkinter as tk
button = tk.Button(text='rafraichir')
button.pack()
label = tk.Label(text='fenetre rafraichie')
def update():
    button.pack_forget()
    label.pack()

button['command'] = update
tk.mainloop()