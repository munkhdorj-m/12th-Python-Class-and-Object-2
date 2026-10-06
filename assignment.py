# ANSWER KEY - Python Class and Object 2
# Do not put this file in the students' repository.


# Exercise 1 -----------------------------------------------------------------

class BusCard:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
        self.trips = 0

    def top_up(self, amount):
        if amount <= 0:
            return False
        self.balance = self.balance + amount
        return True

    def pay(self, fare):
        if fare > self.balance:
            return False
        self.balance = self.balance - fare
        self.trips = self.trips + 1
        return True


# Exercise 2 -----------------------------------------------------------------

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []            # created HERE, so every student gets a new list

    def add_grade(self, score):
        if score < 0 or score > 100:
            return False
        self.grades.append(score)
        return True

    def average(self):
        if len(self.grades) == 0:
            return 0
        total = 0
        for grade in self.grades:
            total = total + grade
        return round(total / len(self.grades), 1)

    def highest(self):
        if len(self.grades) == 0:
            return None
        best = self.grades[0]
        for grade in self.grades:
            if grade > best:
                best = grade
        return best


# Exercise 3 -----------------------------------------------------------------

class Song:
    def __init__(self, title, artist, seconds):
        self.title = title
        self.artist = artist
        self.seconds = seconds

    def length(self):
        minutes = self.seconds // 60
        secs = self.seconds % 60
        if secs < 10:
            return str(minutes) + ":0" + str(secs)
        return str(minutes) + ":" + str(secs)


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def count(self):
        return len(self.songs)

    def total_seconds(self):
        total = 0
        for song in self.songs:
            total = total + song.seconds
        return total

    def longest_song(self):
        if len(self.songs) == 0:
            return None
        best = self.songs[0]
        for song in self.songs:
            if song.seconds > best.seconds:     # > (not >=) keeps the first on a tie
                best = song
        return best

    def songs_by(self, artist):
        titles = []
        for song in self.songs:
            if song.artist == artist:
                titles.append(song.title)
        return titles
