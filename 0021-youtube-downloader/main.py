from tkinter import *
from tkinter import Toplevel, messagebox
from pytubefix import YouTube
import webview

window = Tk()
window.title('Youtube Downloader - JonathanManzanoDiaz')
window.geometry('500x170')
window.resizable(0, 0)

# SCREEN OF PROGRESS DOWNLOAD
def create_progress_screen(parent):
    progress_win = Toplevel(parent)
    progress_win.title("Descargando...")
    progress_win.geometry("250x100")
    Label(progress_win, font=("Arial", 15, 'bold'), text="Descargando...").pack(pady=10)
    percent_label = Label(progress_win, text="0%", font=("Arial", 12, 'bold'))
    percent_label.pack()
    # CALL BACK OF THE PERCENTAGE OF THE DOWNLOAD
    def progress_callback(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        downloaded = total_size - bytes_remaining
        percent = int(downloaded * 100 / total_size)
        percent_label.config(text=f"{percent}%")
        progress_win.update_idletasks()

    return progress_win, progress_callback

# BUTTON MP4
def download_mp4():
    url = urlInput.get()
    if not (url.startswith('http://youtube.com') or url.startswith('www.youtube.com/') or url.startswith('https://youtu.be/')):
        messagebox.showerror("Error Link", "Introduce un link válido que empiece con http o www.")
        return

    # Ventana nueva para elegir resolución
    dwg_mp4 = Toplevel(window)
    dwg_mp4.title('Downloading MP4 Video')
    dwg_mp4.geometry('300x300')
    dwg_mp4.resizable(0, 0)

    resolutions = Listbox(dwg_mp4, font=('Arial', 10, 'bold'))
    resolutions.place(x=10, y=80, width=280, height=210)
    # SHOW THE STREAMS OF THE VIDEO
    yt = YouTube(url)
    streams = yt.streams.filter(file_extension='mp4')
    format_map = {}
    # ADD THE RESOLUTIONS TO THE LISTBOX
    for stream in streams:
        if stream.resolution:
            res = int(stream.resolution.replace("p", ""))
            if res > 360:
                label = f"{stream.resolution} - {round(stream.filesize / 1024 / 1024, 2)} MB"
                list_index = resolutions.size()
                resolutions.insert(END, label)
                format_map[list_index] = stream
    # VIEW VIDEO
    def view_video():
        webview.create_window('Video Selected', url)
        webview.start()
    # DO THE DOWNLOAD
    def do_download_mp4():
        sel = resolutions.curselection()
        if not sel:
            messagebox.showwarning("Atención", "Selecciona una resolución primero")
            return

        stream = format_map[sel[0]]
        progress_win, progress_callback = create_progress_screen(dwg_mp4)

        yt_dl = YouTube(url, on_progress_callback=progress_callback)
        s = yt_dl.streams.get_by_itag(stream.itag)
        s.download()

        progress_win.destroy()
        messagebox.showinfo("Completado", f"Descargado: {s.default_filename}")

    Button(dwg_mp4, font=("Arial", 15, 'bold'), text='View Video', command=view_video).place(x=20, y=20)
    Button(dwg_mp4, font=("Arial", 15, 'bold'), text='Download', command=do_download_mp4).place(x=170, y=20)

 #DOWNLOAD AUDIO
def download_m4a():
    url = urlInput.get()
    if not (url.startswith('http://youtube.com') or url.startswith('www.youtube.com/') or url.startswith('https://youtu.be/')):
        messagebox.showerror("Error Link", "Introduce un link válido que empiece con http o www.")
        return

    progress_win, progress_callback = create_progress_screen(window)

    yt = YouTube(url, on_progress_callback=progress_callback)
    s = yt.streams.get_audio_only()
    s.download()

    progress_win.destroy()
    messagebox.showinfo("Completado", f"Descargado: {s.default_filename}")


# --- GUI Principal ---
labelTitle = Label(font=('Arial', 20, 'bold'), text='Youtube Downloader')
labelTitle.pack(pady=10)

urlInput = Entry(font=('Arial', 20, 'bold'))
urlInput.config(justify='center')
urlInput.place(x=10, y=55, height=50, width=470)

Button(font=("Arial", 15, 'bold'), text='Download MP4', command=download_mp4).place(x=50, y=115)
Button(font=("Arial", 15, 'bold'), text='Download M4A', command=download_m4a).place(x=280, y=115)

window.mainloop()
