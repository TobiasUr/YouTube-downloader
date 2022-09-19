#Importing
from importlib.resources import path
from tkinter import *
from tkinter import filedialog
from pytube import YouTube

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

#downloads
def download():
    Link = LinkEntry.get()
    global path
    Path=path
    yt = YouTube(Link)
    
    if variable.get() == "High":
        yt = yt.streams.get_highest_resolution()
        yt.download(Path)

    
    if variable.get() == "Low":
        yt = yt.streams.get_lowest_resolution()
        yt.download(Path)

    
    if variable.get() == "Audio":
        yt = yt.streams.get_audio_only()
        yt.download(Path)

Button(root, text="Download", command=download).grid(row=2, column=0)




root.mainloop()