from winotify import Notification

toast = Notification(
  app_id="Jonathan says...",
  title="Jonathan Uploaded something!",
  msg="Jonathan uploaded something to GitHub, go for it!!",
  icon=r"C:\Users\Administrator\Desktop\Programacion\python\dominating\0018-desktop-notification\python.ico")
toast.add_actions(label="Open GitHub", launch="https://github.com/JonathanManzanoDiaz/")

toast.show()