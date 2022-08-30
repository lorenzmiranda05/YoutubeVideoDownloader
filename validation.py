import re as regex

youTubeUrl = "https://www.youtube.com/"

def validateYouTubeUrl(urlValueEntry: str) -> bool:
    try:
        urlValueEntry.lower().index(youTubeUrl)
    except ValueError:
        return False
    else:
        if urlValueEntry.lower().index(youTubeUrl) == 0:
            return True
        else:
            return False
        
def checkUrlType(urlValueEntry: str) -> str:
    # https://www.youtube.com/watch?v=YPWG-GhyrZY&t=927s
    # https://www.youtube.com/playlist?list=PLd1apemov4iNgcIn_ErbaHuRI02VXvjqR
    videoUrlRegex = regex.compile("^(https://www.youtube.com/watch\?v=){1}\S+$", regex.I)
    playlistUrlRegex = regex.compile("^(https://www.youtube.com/playlist\?list=){1}\S+$", regex.I)
    if videoUrlRegex.match(urlValueEntry):
        return "Video"
    elif playlistUrlRegex.match(urlValueEntry):
        return "Playlist"
    
    