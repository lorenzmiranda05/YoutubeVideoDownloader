import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import validation
import youtube
import threading

iconFile = r"Assets\Images\Youtube\icons8-youtube-100.ico"

root = tk.Tk()
root.title("Youtube Video Downloader")
root.iconbitmap(iconFile)

def initializeWidgets():
    global frame
    frame = tk.LabelFrame(root, padx = 10, pady = 10)
    frame.grid(row = 0, column = 0, padx = 5, pady = 2)

    urlLabel = tk.Label(frame, text = "YouTube URL:")
    urlLabel.grid(row = 0, column = 0, sticky = tk.E, padx = 5, pady = 5)
    global urlValueEntry
    urlValueEntry = tk.Entry(frame, width = 52)
    urlValueEntry.grid(row = 0, column = 1, columnspan = 2, padx = 5, pady = 5)

    pathLabel = tk.Label(frame, text = "Download Folder:")
    pathLabel.grid(row = 1, column = 0, sticky = tk.E, padx = 5, pady = 5)
    global pathValueEntry
    pathValueEntry = tk.Entry(frame, width = 46)
    pathValueEntry.grid(row = 1, column = 1, padx = 5, pady = 5)
    pathValueButton = tk.Button(frame, text = "...", command = setPathValueEntry, padx = 5)
    pathValueButton.grid(row = 1, column = 2, padx = 5, pady = 5)
    
    global downloadButton
    downloadButton = tk.Button(frame, text = "Download", command = downloadVideo, padx = 5)
    downloadButton.grid(row = 2, column = 0, columnspan = 3, padx = 5, pady = 5)
    
    global statusLabel
    statusLabel = tk.Label(root, text = "")
    statusLabel.grid(row = 1, column = 0, padx = 5, pady = 2, sticky = tk.E)


def setPathValueEntry():
    filePath = filedialog.askdirectory()
    global pathValueEntry
    pathValueEntry.delete(0, tk.END)
    pathValueEntry.insert(0, filePath)

    
def validateEntries():
    global urlValueEntry
    if urlValueEntry.get() == "":
        messagebox.showwarning("Validation", "Please input a valid YouTube URL.")
        return False
    else:
         if not validation.validateYouTubeUrl(urlValueEntry.get()):
            messagebox.showwarning("Validation", "Please input a valid YouTube URL.")
            return False
    if pathValueEntry.get() == "":
        messagebox.showwarning("Validation", "Please select a folder.")
        return False
    return True
   

def setStatusLabel(status: str):
    global statusLabel
    statusLabel.config(text = status)

        
def downloadVideo():
    if validateEntries() == False:
        return
    
    setStatusLabel("Retrieving total file size...")
    
    showDownloadDetailsTopLevel()
    saveUrlAndFilePath()
    disableFrameChildren(frame)
    threading.Thread(target = populateDownloadDetails).start()

def saveUrlAndFilePath():
    global urlValue
    urlValue = urlValueEntry.get()
    global pathValue
    pathValue = pathValueEntry.get()
    
    
def reloadUrlAndPath():  
    global urlValue  
    global pathValue
    global urlValueEntry
    global pathValueEntry
    urlValueEntry.delete(0, tk.END)
    urlValueEntry.insert(0, urlValue)
    pathValueEntry.delete(0, tk.END)
    pathValueEntry.insert(0, pathValue)


def getDownloadDetails():
    global urlValueEntry
    videoList = []
    totalFileSize = 0
    urlType = validation.checkUrlType(urlValueEntry.get())
    if urlType == "Video":
        videoList, totalFileSize = youtube.checkVideoSize(urlValueEntry.get())
    elif urlType == "Playlist":
        videoList, totalFileSize = youtube.checkPlaylistSize(urlValueEntry.get())
    return videoList, totalFileSize

def disableFrameChildren(frame: tk.Frame):
    for child in frame.winfo_children():
        child.config(state = "disable")
        
        
def enableFrameChildren(frame: tk.Frame):
    for child in frame.winfo_children():
        child.config(state = "normal")

def populateDownloadDetails():
    videoList = []
    totalFileSize = 0
    videoList, totalFileSize = getDownloadDetails()
    
    global totalFileSizeValueLabel
    totalFileSizeValueLabel.config(text = f"~{ totalFileSize } MB")
    global videosValueLabel
    videosValueLabel.config(text = f"{ len(videoList) }")
    global okButton
    okButton.config(command = lambda: okDownload(videoList, totalFileSize), state = "normal")
    global cancelButton
    cancelButton.config(state = "normal")
    

def showDownloadDetailsTopLevel():        
    global downloadDetailsTopLevel
    downloadDetailsTopLevel = tk.Toplevel()
    downloadDetailsTopLevel.title("Youtube Download Details")
    downloadDetailsTopLevel.iconbitmap(iconFile)
    
    downloadDetailsFrame = tk.LabelFrame(downloadDetailsTopLevel, padx = 10, pady = 10)
    downloadDetailsFrame.grid(row = 0, column = 0, padx = 5, pady = 2)

    totalFileSizeLabel = tk.Label(downloadDetailsFrame, text = "Total File Size:")
    totalFileSizeLabel.grid(row = 0, column = 0, sticky = tk.E, padx = 5, pady = 5)
    global totalFileSizeValueLabel
    # totalFileSizeValueLabel = tk.Label(downloadDetailsFrame, text = f"~{ totalFileSize } MB")
    totalFileSizeValueLabel = tk.Label(downloadDetailsFrame, text = "Retrieving...")
    totalFileSizeValueLabel.grid(row = 0, column = 1, sticky = tk.E, columnspan = 2, padx = 5, pady = 5)

    videosLabel = tk.Label(downloadDetailsFrame, text = "Video(s):")
    videosLabel.grid(row = 1, column = 0, sticky = tk.E, padx = 5, pady = 5)
    global videosValueLabel
    # videosValueLabel = tk.Label(downloadDetailsFrame, text = f"{ len(videoList) }")
    videosValueLabel = tk.Label(downloadDetailsFrame, text = "Retrieving...")
    videosValueLabel.grid(row = 1, column = 1, sticky = tk.E, columnspan = 2, padx = 5, pady = 5)
    
    questionLabel = tk.Label(downloadDetailsFrame, text = "Continue to download?")
    questionLabel.grid(row = 2, column = 0, columnspan = 3, padx = 5, pady = 10)
    
    global okButton
    # okButton = tk.Button(downloadDetailsFrame, text = "OK", padx = 15, command = lambda: okDownload(videoList, totalFileSize))
    okButton = tk.Button(downloadDetailsFrame, text = "OK", padx = 15)
    okButton.grid(row = 3, column = 0, sticky = tk.E, padx = 5, pady = 5)
    okButton.config(state = "disabled")
    global cancelButton
    cancelButton = tk.Button(downloadDetailsFrame, text = "Cancel", padx = 15, command = cancelDownload)
    cancelButton.grid(row = 3, column = 1, columnspan = 2, padx = 5, pady = 5)
    cancelButton.config(state = "disabled")
    
    downloadDetailsTopLevel.focus()


def cancelDownload():
    enableFrameChildren(frame)
    setStatusLabel("Cancelled download.")
    global downloadDetailsTopLevel
    downloadDetailsTopLevel.destroy()


def okDownload(videoList, totalFileSize):
    global downloadDetailsTopLevel
    downloadDetailsTopLevel.destroy()
    root.focus()
    threading.Thread(target = lambda: continueDownloadVideo(videoList, totalFileSize)).start()

    
def continueDownloadVideo(videoList, totalFileSize):
    for index, video in enumerate(videoList):
        setStatusLabel(f"Downloading video { index + 1 } of { len(videoList) }")
        youtube.downloadVideo(video, pathValueEntry.get())
    setStatusLabel(f"Done | Total File Size: ~{ totalFileSize }MB | Video(s): { len(videoList)}")
    enableFrameChildren(frame)

initializeWidgets() 
root.mainloop()