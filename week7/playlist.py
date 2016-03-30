from song import Song
import time
from datetime import date


class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self._playlist = []

    def add_song(self, new_song):
        self._playlist.append(new_song)

    def remove_song(self, old_song):
        self._playlist.remove(old_song)

    def add_songs(self, new_songs):
        for song in new_songs:
            self._playlist.append(song)

    def total_length(self):
        playlist_length = 0
        for song in self._playlist:
            playlist_length += int(song.length(seconds=True))
        if pl


s = Song("ss", "Sandi", "first", "3:24:51")
q = Song("qq", "Sandi", "second", "24:51")
v = Song("vv", "Sandi", "third", "51")

rock = Playlist("rock")

rock.add_song(s)
rock.add_song(q)
rock.add_song(v)
print(rock.total_length())
