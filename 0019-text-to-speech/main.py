from tkinter import *
from gtts import gTTS
import playsound3 as playsound

def text_to_speech():
  data = text.get()
  tts = gTTS(data)
  tts.save('1.mp3')

window = Tk()
window.title('Text to Speech by JonathanManzanoDiaz')
window.geometry('500x125')
window.resizable(0,0)

info = Label(font=("Arial", 17, 'bold'), text="Type your text")
info.place(x=170, y=20)

text = Entry(font=('Ink Free', 20, 'bold'))
text.place(x=5, y=60, width=380, height=50)

accept = Button(font=('Arial', 18, 'bold'), text='Accept', command=text_to_speech)
accept.place(x=390, y=60)
window.mainloop()