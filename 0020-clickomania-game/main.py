from tkinter import *
import random
from functools import partial

selected = []
congratulations = None  # reference victory message

def reset_game():
  global buttons, score_value, congratulations
  # delete anterior buttons
  for b in buttons:
      b.destroy()
  buttons = []

    # reset score
  score_value = 0
  score.config(text=str(score_value))

    # delete victory message if exists
  if congratulations:
    congratulations.destroy()
    congratulations = None

  full_colors = colors * 2  # 16 elementos
  random.shuffle(full_colors)

  def select(b, c):
    global selected, score_value, congratulations
    selected.append([b, c])
    b.config(bg='darkviolet')

    if len(selected) == 2 and selected[0][1] == selected[1][1]:
      selected[0][0].destroy()
      selected[1][0].destroy()
      selected.clear()
      score_value += 1
      score.config(text=str(score_value))

          # check victory
      if score_value == 8:
        congratulations = Label(window, font=('Arial', 25, 'bold'),
                                text='Congratulations! You win!')
        congratulations.place(x=80, y=150)
    else:
      if len(selected) == 2:
        # If not the same color, reset
        selected[0][0].config(bg=selected[0][1])
        selected[1][0].config(bg=selected[1][1])
        selected.clear()

  for i, color in enumerate(full_colors):
    row = i // 4
    column = i % 4
    x = 50 + column * 120
    y = 100 + row * 80

    button = Button(window, font=('Arial', 15, 'bold'), text=color, bg=color)
    button.config(command=lambda b=button, c=color: select(b, c))
    button.place(x=x, y=y)
    buttons.append(button)


# ventana principal
window = Tk()
window.title('Clickomania Game - Jonathan Manzano Diaz')
window.geometry('550x500')
window.resizable(0,0)

# marcador
text = Label(font=('Arial', 30, 'bold'), text="Score: ")
text.place(x=180, y=10)

score_value = 0
score = Label(font=('Arial', 30, 'bold'), text=f"{score_value}")
score.place(x=320, y=10)

# colores base
colors = ['green', 'white', 'yellow', 'blue', 'red', 'cyan', 'brown', 'grey']
buttons = []

# botón reset
reset = Button(font=('Arial', 15, 'bold'), text='Reset', command=reset_game)
reset.place(x=230, y=425)

# primera partida
reset_game()

window.mainloop()
