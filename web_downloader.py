

from tkinter import *
import os
import requests


def downloader():

    i = t.get()

    a = requests.get(i)

    filename = i.split("/")[-1]

    for chunks in a.iter_content(chunk_size=1024**3):

        x = os.path.join('/home/saed/Downloads',filename)
        y = open(x,'wb')

    if chunks:

        y.write(chunks)

    return x


def clear():

    t.set("")


root = Tk()

root.title("Web Downloader V0")
root.geometry("800x500")

frame = Frame(root)
frame.pack(side = RIGHT)


bframe = Frame(root)
bframe.pack(side = BOTTOM)
t = ""
t = StringVar()


lbl0 = Label(root,text = "Web Downloader App",font = ("arial",25,"bold"),fg = 'blue')
lbl0.pack(side = TOP)
lbl1 = Label(root,text = "Enter the weblink you wish to download",font = ("arial"),fg = 'blue')
lbl1.pack(side = LEFT)

entry = Entry(root,textvariable = t,width = 30,font = ("arial",20))
entry.pack(side = LEFT)

btn = Button(bframe,text = "Click here to start downloading",width = 30,font = ("arial",16,"bold")
             ,command = downloader)
btn.pack(side = LEFT)

btnq = Button(bframe,text = "Quit",width = 30,font = ("arial",16,"bold")
             ,command = root.destroy)
btnq.pack(side = LEFT)

cbtn = Button(frame,text = "clear link",width = 15,font = ("arial",16,"bold"),
              command = clear)
cbtn.pack(side = LEFT)


root.mainloop()