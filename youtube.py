from pytube import YouTube
from pytube import Playlist

def checkVideoSize(urlValueEntry: str):
    videoList = []
    totalFileSize = 0
    video = YouTube(urlValueEntry)
    videoList.append(video)
    totalFileSize = video.streams.get_highest_resolution().filesize
    return videoList, int(totalFileSize / 1000000)


def checkPlaylistSize(urlValueEntry: str):
    videoList = []
    playlist = Playlist(urlValueEntry)
    totalFileSize = 0
    for video in playlist.videos:
        size = video.streams.get_highest_resolution().filesize
        totalFileSize += size
        videoList.append(video)
    return videoList, int(totalFileSize / 1000000)


def downloadVideo(video: YouTube, pathValueEntry: str):
    video.streams.get_highest_resolution().download(pathValueEntry)