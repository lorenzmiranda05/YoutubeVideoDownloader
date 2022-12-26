class SubRipFormat:
    def __init__(self, index : int, text : str):
        self.index = index
        self.timing = ""
        self.text = text
        
    def __formatFloatToSubripTiming(self, timing : float):
        # HH:MM:SS,TTT
        hours = int(timing // 3600)
        minutes = int((timing % 3600) // 60)
        seconds = int(((timing % 3600) % 60))
        milliseconds = str(timing).split(".")[1]
        subRipTiming = f"{ str(hours).zfill(2) }:{ str(minutes).zfill(2) }:{ str(seconds).zfill(2) },{ milliseconds[:3].ljust(3, '0') }"
        return subRipTiming

    def convertYouTubeTranscriptTimingToSubRipTiming(self, youTubeStart : float, youTubeDuration : float):
        formattedStartTime = self.__formatFloatToSubripTiming(youTubeStart)
        endTimeFloat = youTubeStart + youTubeDuration
        formattedEndTime = self.__formatFloatToSubripTiming(endTimeFloat)
        self.timing = f"{ formattedStartTime } --> { formattedEndTime }"
