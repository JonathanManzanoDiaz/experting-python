from tkinter import *
from tkinter import messagebox
import base64

def submit():
  try:
    if variable.get() == 'Encode':
      text = data.get()
      text = text.encode("ascii")
      text = base64.b64encode(text)
    elif variable.get() == 'Decode':
      text = data.get()
      text = base64.b64decode(text)
      text = text.decode("ascii")
  except ValueError:
    messagebox.showerror(title='Invalid Entry!', message='Please, select the option correctly.')
  # input result
  result = Entry(font=("Arial", 27), width=25)
  result.insert(0, text)
  result.config(state="readonly")
  result.place(x=2, y=120)
  
  # Copy Button
  def copy_clipboard():
    window.clipboard_clear()
    window.clipboard_append(text)
    window.update()
    # Change to "Copied"
    result.config(state="normal")
    result.delete(0, "end")
    result.insert(0, "Copied ✅")
    result.config(state="readonly")
    
  copy_btn = Button(window, font=('Arial', 16), text='Copy', command=copy_clipboard)
  copy_btn.place(x=515, y=120)
  result.insert(0, 'Copied')
  

window = Tk()
window.geometry("600x200")
window.title('Encode/Decode with Base64 - Jonathan Manzano Diaz')

title = Label(font=('Ink Free', 20), text="Encode/Decode With Base64")
title.place(x=90, y=10)


# BUTTONS
optionList = [
  "Encode",
  "Decode",

]
variable = StringVar(window)
variable.set("Encode")

opt = OptionMenu(window, variable, *optionList)
opt.config(height=2)
opt.place(x=410, y=55)

submit = Button(font=('Arial', 16), text='Submit', command=submit)
submit.place(x=500, y=55)

# input
data = Entry(font=("Arial", 27))
data.place(x=2, y=55)



# button copy



window.mainloop()