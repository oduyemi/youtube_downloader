from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300') # Size of the window
root.resizable(0, 0) # makes the window adjustable with its features
root.title('Youtube downloader')
root ["bg"] = "#1A1D1A"

#root.mainloop()

Label(root,text = 'Youtube Video Downloader',  font ='poppins 20 bold').pack()
link = StringVar()

Label(root, text = 'Paste The Video Link Here:', font = 'poppins 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'VIDEO SAVED', font = 'poppins 15').place(x= 180 , y = 210)  
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' , fg = '#ffffff', bg = '#4CB944', padx = 2, command = Downloader).place(x=180 ,y = 150)
root.mainloop()