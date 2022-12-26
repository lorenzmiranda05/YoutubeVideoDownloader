from pytube import YouTube
from pytube import Playlist
from youtube_transcript_api import YouTubeTranscriptApi
from json import loads
from subripformat import SubRipFormat

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


def downloadSubtitle(video: YouTube, pathValueEntry: str):
    try:
        # Check if YouTube video has an English Subtitle
        subtitleEntryList = YouTubeTranscriptApi.get_transcript(video_id = video.video_id, languages = ["en"])
    except:
        # Skip downloading the subtitle of this YouTube video
        return

    # Clean Video Title
    videoTitle = video.title
    videoTitle = videoTitle.replace("\"", "")
    videoTitle = videoTitle.replace(".", "")
    
    # Create the .srt file of the subtitle
    with open(f"{pathValueEntry}\\{videoTitle}.srt", "w", encoding="utf-8") as file:
        for index, jsonSubtitle in enumerate(subtitleEntryList):
            # Clean jsonSubtitle
            subtitleEntry = str(jsonSubtitle)
            subtitleEntry = subtitleEntry.replace("\\\'", "\'")
            subtitleEntry = subtitleEntry.replace("\"", "*")
            subtitleEntry = subtitleEntry.replace("'text'", "\"text\"")
            subtitleEntry = subtitleEntry.replace("'start'", "\"start\"")
            subtitleEntry = subtitleEntry.replace("'duration'", "\"duration\"")
            subtitleEntry = subtitleEntry.replace("\"text\": *", "\"text\": \"")
            subtitleEntry = subtitleEntry.replace("*, \"start\"", "\", \"start\"")
            subtitleEntry = subtitleEntry.replace("\"text\": '", "\"text\": \"")
            subtitleEntry = subtitleEntry.replace("', \"start\"", "\", \"start\"")
            jsonSubtitleEntry = loads(subtitleEntry)
                            
            subRipEntry = SubRipFormat(index + 1, jsonSubtitleEntry["text"])
            subRipEntry.convertYouTubeTranscriptTimingToSubRipTiming(jsonSubtitleEntry["start"]
                                                                     , jsonSubtitleEntry["duration"])
            
            # Write two new lines at the start of every subtitle entry after index 0
            if index != 0:
                file.write("\n\n")

            # Write subtitle entry number
            file.write(f"{ subRipEntry.index }")
            
            # Write the time span of the subtitle entry
            file.write(f"\n{ subRipEntry.timing }")
            
            # Write the text of the subtitle entry
            file.write(f"\n{ subRipEntry.text }")