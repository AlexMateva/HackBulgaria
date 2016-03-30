class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self._length = length

    def __str__(self):
        return "{} - {} from {} - {}".format(self.artist, self.title, self.album, self.length)

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artsit and self.album == other.album and self._length == other._length

    def __hash__(self):
        return hash(self.title)

    def _time_in_seconds(self):
        l = self._length.split(":")
        if len(l) == 3:
            timel = int(l[0])*3600 + int(l[1])*60 + int(l[2])
        if len(l) == 2:
            timel = int(l[0])*60 + int(l[1])
        if len(l) == 1:
            timel = int(l[0])
        return timel

    def length(self, **keywords):

        if not keywords:
            return self._length

        for key in keywords:
            if key == "seconds" and keywords["seconds"] is True:
                return self._time_in_seconds()
            if key == "minutes" and keywords["minutes"] is True:
                return self._time_in_seconds() // 60
            if key == "hours" and keywords["hours"] is True:
                return self._time_in_seconds() // 3600



