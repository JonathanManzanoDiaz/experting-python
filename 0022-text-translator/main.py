from tkinter import *
from tkinter import ttk,messagebox
from googletrans import Translator
import cgi

window = Tk()
translator = Translator()
window.title('Text Translator - Jonathan Manzano Diaz')
window.geometry('500x400')
swapped = False

def translate_now():
    english2.delete("1.0", "end")
    translated = translator.translate(detect2.get("1.0", "end-1c")).text
    english2.insert("1.0", translated)
    
detect = Label(font=("Arial", 15, 'bold'), text='Auto Detect')
detect.place(x=30, y=20)
detect2 = Text(font=('Ink Free', 15, 'bold'))
detect2.place(x=10, y=70, width=220, height=310)

english = Label(font=("Arial", 15, 'bold'), text='English')
english.place(x=325, y=20)
english2 = Text(font=('Ink Free', 15, 'bold'))
english2.place(x=250, y=70, width=220, height=310)

translate = Button(font=('Arial', 15, 'bold'), text='Translate now', command=translate_now)
translate.place(x=160, y=10)



window.mainloop()
