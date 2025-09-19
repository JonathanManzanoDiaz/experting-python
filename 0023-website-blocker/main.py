import os
import tkinter as tk
from tkinter import messagebox   # <-- para usar Listbox clásico
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


# Ventana principal con tema de ttkbootstrap
window = ttk.Window(themename="cosmo")
window.title('Website Blocker - Jonathan Manzano Diaz')
window.geometry('500x300')
window.resizable(0, 0)

HOSTS_PATH = r"C:\Windows\System32\drivers\etc\hosts"
REDIRECT_IP = "127.0.0.1"

def block_web():
    website = link.get().strip()
    if not website:
        return

    # Primero comprobamos si ya está bloqueado
    with open(HOSTS_PATH, "r") as f:
        if any(website in line for line in f):
            messagebox.showerror("Error", f"{website} is already blocked!")
            return

    # Si no está, lo añadimos
    with open(HOSTS_PATH, "a") as f:
        f.write(f"{REDIRECT_IP} {website}\n")

    list_websites.insert(tk.END, website)
    link.delete(0, tk.END)

def unblock_web():
    selected = list_websites.get(tk.ANCHOR).strip()
    if not selected:
        return

    list_websites.delete(tk.ANCHOR)

    with open(HOSTS_PATH, "r") as f:
        lines = f.readlines()
    with open(HOSTS_PATH, "w") as f:
        for line in lines:
            if selected not in line:
                f.write(line)

# Título
title = ttk.Label(window, text='Website Locker by Jonathan Manzano Diaz', font=('Arial', 15, 'bold'))
title.place(x=40, y=5)

# Caja de entrada
link = ttk.Entry(window, font=('Arial', 15, 'bold'))
link.place(x=10, y=40, height=40, width=480)

# ---- Estilo de botones con fuente personalizada ----
style = ttk.Style()
style.configure("My.TButton", font=("Arial", 15, "bold"))

# Botones
block = ttk.Button(window, text='Block', bootstyle=SUCCESS, style="My.TButton", command=block_web)
block.place(x=10, y=90, width=230)

unblock = ttk.Button(window, text='Unblock', bootstyle=DANGER, style="My.TButton", command=unblock_web)
unblock.place(x=260, y=90, width=230)

# ✅ Listbox debe venir de tkinter, no de ttkbootstrap
list_websites = tk.Listbox(window, font=('Arial', 15, 'bold'))
list_websites.place(x=10, y=145, width=480, height=140)




with open(HOSTS_PATH, "r") as f:
    lines = f.readlines()
    for line in lines:
        if line.strip() and not line.startswith("#") and REDIRECT_IP in line:
            website = line.split()[1]
            list_websites.insert(tk.END, website)

window.mainloop()
