from tkinter import *
from tkinter import messagebox
import re
def submit():
  email = entry.get()
  patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
  emailList = entry.get().split('@')
  
  if re.match(patron, email):
    username = Label(font=('Arial', 15), text=f"Username: {emailList[0]}")
    domain = Label(font=('Arial', 15), text=f"Domain: {emailList[1]}")
    username.place(x=20, y=120)
    domain.place(x=20, y=155)
    
  else:
    messagebox.showerror("Error", "This email is not valid")
    
window = Tk()
window.geometry("535x200")
window.resizable(0,0)
window.title('Email Slicer by Jonathan Manzano Diaz')

label = Label(font=('Ink Free', 20), text='Email Slicer')
label.pack()

entry = Entry(font=('Arial', 30))
entry.place(x=0, y=40)


submit = Button(window, text='Submit', width=10, height=3, command=submit)
submit.place(x=448, y=35)



window.mainloop()
