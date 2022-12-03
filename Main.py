#Importing
from importlib.resources import path
from inspect import Attribute
from customtkinter import *
from customtkinter import filedialog
from tkinter.ttk import Progressbar
from pytube import YouTube
from pytube.cli import on_progress
import threading

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

root = CTk()
#VideoLinkEntry
CTkLabel(root, text="Enter link to video: ").grid(row=0, column=0)
LinkEntry = CTkEntry(root, width=350)
LinkEntry.grid(row=0, column=1)
#Path
def selectPath():
    global path
    path= filedialog.askdirectory(title="Select download location")
    CTkLabel(root, text=path).grid(row=1, column=1, sticky='w')

CTkButton(root, text="Select path", command=selectPath).grid(row=1, column=1, sticky='e')
#progress bar
pb = CTkProgressBar(root, orientation='horizontal', mode='determinate',width=200, height=20)
pb.grid(row=2, column=1, sticky="e")

#DropdownMenu
OPTIONS = [
"Audio",
"Low",
"High"
]

#variable = StringVar(root)
#variable.set(OPTIONS[2])
def optionmenu_callback(choice):
    global variable
    variable = choice

QualitySelect = CTkOptionMenu(root, values=["Audio","Low", "High"], command=optionmenu_callback)
QualitySelect.grid(row=2, column=1, sticky='w')

#update on download progress
def on_progress(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = (size - bytes_remaining)/size
    pb.set(progress)
    root.update_idletasks()  
    print(progress*100)


#downloads
def download():
    Link = LinkEntry.get()
    global path
    Path=path
    yt = YouTube(Link, on_progress_callback=on_progress)
    print(variable)
    
    
    if variable == "High":
        yt = yt.streams.get_highest_resolution()
        yt.download(Path)

    
    if variable == "Low":
        yt = yt.streams.get_lowest_resolution()
        yt.download(Path)

    
    if variable == "Audio":
        yt = yt.streams.get_audio_only()
        yt.download(Path)
def start():
    x = threading.Thread(target=download)
    x.start()
CTkButton(root, text="Download", command=start).grid(row=2, column=0)




root.mainloop()