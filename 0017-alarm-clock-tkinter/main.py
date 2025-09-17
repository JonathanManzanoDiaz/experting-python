from tkinter import *
from tkinter import Toplevel, messagebox
import datetime

import winsound

window = Tk()
screen_width = '500'
screen_height = '400'
middle_screen = int(screen_width) // 2 - 80
window.geometry(f'{screen_width}x{screen_height}')
window.title("Alarm Clock by Jonathan Manzano Diaz")
window.resizable(0,0)

alarms = []
#creating label time
def current_time():
  window.after(1000, current_time)
  time = datetime.datetime.now()
  hour.config(text=time.strftime("%H:%M:%S"))
  hour.place(x=middle_screen, y=20)
  for i, alarm in enumerate(alarms):
    if alarm == time.strftime("%H:%M"):
      alarms.remove(alarm)
      alarms_listbox.delete(i)
      winsound.PlaySound('alarm.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
      messagebox.showinfo("Alarm", "¡ALARM!")
      winsound.PlaySound(None, winsound.SND_PURGE)
      
      break

    
def add_alarm():
  
  def accept_alarm():

    try:
      h = int(alarm_hour.get())
      m = int(alarm_minute.get())
      if 0 <= h <= 23 and 0 <= m <= 59:
        alarms.append(f"{h:02d}:{m:02d}")
        alarms_listbox.insert(END, f"{h:02d}:{m:02d}")

        new_alarm.destroy()
      else:
        messagebox.showerror(title='Invalid Alarm!', message='Please, introduce time correctly.')
    except ValueError:
      messagebox.showerror(title='Invalid Alarm!', message='Please, introduce time correctly.')
  
  new_alarm = Toplevel(window)
  new_alarm.title("New Alarm")
  new_alarm.geometry('400x175')
  new_alarm.resizable(0,0)
  label2 = Label(new_alarm, font=('Arial', 15, 'bold'), text='Introduce your new alarm')
  label2.place(x=75, y=10)
  
  alarm_hour = Spinbox(new_alarm, width=8, from_=0, to=23, increment=1)
  alarm_hour.config(font=("Arial", 15, 'bold'), justify='center')
  alarm_hour.place(x=90, y=80)
  hLabel = Label(new_alarm, font=('Arial', 15, 'bold'), text='H')
  hLabel.place(x=125, y=50)
  
  alarm_minute = Spinbox(new_alarm,width=8, from_=0, to=59, increment=1)
  alarm_minute.config(font=("Arial", 15, 'bold'), justify='center')
  alarm_minute.place(x=210, y=80)
  mLabel = Label(new_alarm, font=('Arial', 15, 'bold'), text='M')
  mLabel.place(x=245, y=50)
  
  alarm_accept = Button(new_alarm, font=("Arial", 15, 'bold'), text='Accept', command=accept_alarm)
  alarm_accept.place(x=160, y=120)
  
def delete_alarm():
  selected = alarms_listbox.curselection()
  if selected:
    index = selected[0]
    alarms_listbox.delete(index)
    alarms.pop(index)


hour = Label(font=("Arial", 30, 'bold'), text=f"")

addButton = Button(font=("Arial", 15, 'bold'), text='+', width=5, height=0, command=add_alarm)
addButton.place(x=425, y=335)

deleteButton = Button(window, font=("Arial", 15, "bold"), text="x", width=5, command=delete_alarm)
deleteButton.place(x=425, y=285)

alarms_listbox = Listbox(window, font=("Arial", 20, "bold"), justify='center')
alarms_listbox.place(x=20, y=80, width=390, height=300)
current_time()

# Add all the alarms

window.mainloop()