import youtube
import validation

urlValueEntry = "https://www.youtube.com/playlist?list=PLd1apemov4iPg276VT0JzrWmRpDDdaxWi"
pathValueEntry = "D:\Temperance"

def getDownloadDetails():
    global urlValueEntry
    videoList = []
    totalFileSize = 0
    urlType = validation.checkUrlType(urlValueEntry)
    if urlType == "Video":
        videoList, totalFileSize = youtube.checkVideoSize(urlValueEntry)
    elif urlType == "Playlist":
        videoList, totalFileSize = youtube.checkPlaylistSize(urlValueEntry)
    return videoList, totalFileSize

videoList = []
totalFileSize = 0
videoList, totalFileSize = getDownloadDetails()

for index, video in enumerate(videoList):
        youtube.downloadVideo(video, pathValueEntry)
        youtube.downloadSubtitle(video, pathValueEntry)