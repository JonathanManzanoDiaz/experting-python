from tkinter import *
from tkinter import messagebox as msg
import random

root = Tk()
root.title('Guess Number')
root.attributes("-topmost", True)
root.geometry('300x125+750+280')
root.resizable(False, False)

aleatorio = random.randint(0, 1000)
counter = 1

def guess_number():
    global counter, aleatorio
    ask = int(number.get())
    try:
        if ask > aleatorio:
            msg.showwarning('Error', 'Tú numero es más alto!')
            counter += 1
        elif ask < aleatorio:
            msg.showerror('Error', 'Tú numero es más pequeño!')
            counter += 1
        else:
            msg.showinfo('Felicidades!!', f"Lo has adivinado, felicidades! Te ha tomado {counter - 1} intentos, se cerrará programa...")
            root.quit()
    except ValueError:
        msg.showerror('Error!', 'VALOR NO VALIDO, Introduce un numero correctamente')


Label(font=('Ink Free', 20, 'bold'), text='Guess Number Game').pack()


number = Entry(root)
number.config(width=25, font=('Arial', 15, 'bold'), justify='center')
number.insert(0, 'Here your guess')
number.bind('<Button-1>', lambda x:number.delete(0, END))
number.pack()
Button(root,font=('Arial', 12, 'bold'), text='Enviar', command=lambda:guess_number()).pack(pady=10)
root.mainloop()