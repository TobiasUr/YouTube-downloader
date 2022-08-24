
from tkinter import *
from pytube import YouTube

root = Tk()

Label(root, text="Enter link to video: ").grid(row=0, column=0)
LinkEntry = Entry(root, width=100, borderwidth=1)
LinkEntry.grid(row=0, column=1)

Label(root, text="Enter path: ").grid(row=1, column=0)
PathEntry=Entry(root, width=100, borderwidth=1)
PathEntry.grid(row=1, column=1)



def download():
    Link = LinkEntry.get()
    Path=PathEntry.get()
    yt = YouTube(Link)
    
    yt = yt.streams.get_highest_resolution()
    yt.download(Path)

Button(root, text="Download", command=download).grid(row=2, column=0)


root.mainloop()