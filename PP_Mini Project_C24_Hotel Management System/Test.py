from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube  # pip install pytube3

Folder_Name = ""

def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if (len(Folder_Name) > 1):
        patherror.config(text=Folder_Name, fg="green")
    else:
        patherror.config(text="Please choose folder !", fg="Black")


def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if (len(url) > 1):
        errormsg.config(text="")
        yt = YouTube(url)

        if (choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif (choice == choices[1]):
            select = yt.streams.filter(progressive=True, file_extension='mp4').last()

        elif (choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            errormsg.config(text="Paste URL again !", fg='black')

    select.download(Folder_Name)
    errormsg.config(text="Download complete ! :) ")


root = Tk()
root.title("YOUTUBE VIDEO DOWNLOADER")
root.geometry("750x400")  # window size
root.configure(bg='yellow')
root.columnconfigure(0, weight=1)

guiLabel = Label(root, text="WELCOME TO YOUTUBE VIDEO DOWNLOADER !", font=("Times new roman", 17), fg="blue",
                 bg='yellow')
guiLabel.grid()

guiLabel = Label(root, text="Paste you URL below: ", font=("Times new roman", 15), bg='yellow')
guiLabel.grid()

ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=70, )
ytdEntry.grid()

errormsg = Label(root, text="Error : Incorrect URL", font=("Times new roman", 14, "italic"), fg="red", bg='yellow')
errormsg.grid()

saveLabel = Label(root, text=" Download the video:", font=("Times new roman", 16, "bold"), bg='yellow')
saveLabel.grid()

saveEntry = Button(root, width='20', bg='green', fg='black', text="Choose where to save", font=("Times new roman", 10),
                   command=openLocation)
saveEntry.grid()

patherror = Label(root, text="Error in location selected", fg='red', font=("Times new roman", 14, "italic"),
                  bg='yellow')
patherror.grid()

quality = Label(root, text='Select quality for download :', font=("Times new roman", 15, 'bold'), bg='yellow')
quality.grid()

choices = ['720p', '144p', 'only audio']
ytdchoices = ttk.Combobox(root, values=choices)
ytdchoices.grid()

download = Button(root, width='20', bg='green', fg='white', text='DOWNLOAD', font=("Times new roman", 14, 'bold'),
                  command=DownloadVideo)
download.grid(padx=10, pady=10)

root.mainloop()