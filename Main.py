#Importing
from importlib.resources import path
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Progressbar
from pytube import YouTube
from pytube.cli import on_progress
import threading

root = Tk()
#VideoLinkEntry
Label(root, text="Enter link to video: ").grid(row=0, column=0)
LinkEntry = Entry(root, width=100, borderwidth=1)
LinkEntry.grid(row=0, column=1)
#Path
def selectPath():
    global path
    path= filedialog.askdirectory(title="Select download location")
    Label(root, text=path).grid(row=1, column=1, sticky='w')

Button(root, text="Select path", command=selectPath).grid(row=1, column=1, sticky='e')
#progress bar
pb = Progressbar(root, orient='horizontal', mode='determinate',length=320)
pb.grid(row=2, column=1)

#DropdownMenu
OPTIONS = [
"Audio",
"Low",
"High"
]

variable = StringVar(root)
variable.set(OPTIONS[2])

QualitySelect = OptionMenu(root, variable, *OPTIONS)
QualitySelect.grid(row=2, column=1, sticky='w')

#update on download progress
def on_progress(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = (size - bytes_remaining)/size
    pb['value'] = progress*100
    root.update_idletasks()  
    print(progress*100)


#downloads
def download():
    Link = LinkEntry.get()
    global path
    Path=path
    yt = YouTube(Link, on_progress_callback=on_progress)
    
    
    if variable.get() == "High":
        yt = yt.streams.get_highest_resolution()
        yt.download(Path)

    
    if variable.get() == "Low":
        yt = yt.streams.get_lowest_resolution()
        yt.download(Path)

    
    if variable.get() == "Audio":
        yt = yt.streams.get_audio_only()
        yt.download(Path)
def start():
    x = threading.Thread(target=download)
    x.start()
Button(root, text="Download", command=start).grid(row=2, column=0)




root.mainloop()