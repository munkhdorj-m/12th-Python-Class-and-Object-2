import pytest

from assignment import BusCard, Student, Song, Playlist


def test1_new_card():
    card = BusCard("Bat")
    assert card.owner == "Bat"
    assert card.balance == 0
    assert card.trips == 0


def test1_top_up_and_pay():
    card = BusCard("Bat")

    assert card.top_up(5000) == True
    assert card.balance == 5000
    assert card.top_up(0) == False
    assert card.top_up(-200) == False
    assert card.balance == 5000

    assert card.pay(500) == True
    assert card.balance == 4500
    assert card.trips == 1

    assert card.pay(10000) == False
    assert card.balance == 4500
    assert card.trips == 1

    assert card.pay(4500) == True
    assert card.balance == 0
    assert card.trips == 2


def test1_separate_cards():
    card1 = BusCard("Bat")
    card2 = BusCard("Saraa")
    card1.top_up(3000)
    card1.pay(500)
    assert card1.balance == 2500
    assert card1.trips == 1
    assert card2.balance == 0
    assert card2.trips == 0


def test2_add_grade():
    s = Student("Saraa")
    assert s.name == "Saraa"
    assert s.grades == []

    assert s.add_grade(90) == True
    assert s.add_grade(0) == True
    assert s.add_grade(100) == True
    assert s.add_grade(101) == False
    assert s.add_grade(-1) == False
    assert s.grades == [90, 0, 100]


@pytest.mark.parametrize("grades, expected_average, expected_highest", [
    [[90, 85, 77], 84.0, 90],
    [[70, 81], 75.5, 81],
    [[1, 2, 2], 1.7, 2],
    [[100], 100.0, 100],
    [[], 0, None],
])
def test2_average_and_highest(grades, expected_average, expected_highest):
    s = Student("Bat")
    for grade in grades:
        s.add_grade(grade)
    assert s.average() == expected_average
    assert s.highest() == expected_highest


def test2_separate_students():
    s1 = Student("Bat")
    s2 = Student("Saraa")
    s1.add_grade(95)
    s1.add_grade(80)
    assert s1.grades == [95, 80]
    assert s2.grades == []


@pytest.mark.parametrize("seconds, expected", [
    [205, "3:25"],
    [65, "1:05"],
    [59, "0:59"],
    [600, "10:00"],
    [0, "0:00"],
])
def test3_song(seconds, expected):
    song = Song("Morning Steppe", "Nomin", seconds)
    assert song.title == "Morning Steppe"
    assert song.artist == "Nomin"
    assert song.seconds == seconds
    assert song.length() == expected


def test3_playlist_basics():
    p = Playlist("Road Trip")
    assert p.name == "Road Trip"
    assert p.songs == []
    assert p.count() == 0
    assert p.total_seconds() == 0

    s1 = Song("Morning Steppe", "Nomin", 205)
    s2 = Song("Blue Sky", "Temuulen", 180)
    p.add_song(s1)
    p.add_song(s2)

    assert p.count() == 2
    assert p.total_seconds() == 385
    assert p.songs[0] is s1
    assert p.songs[1] is s2


def test3_playlist_search():
    p = Playlist("Mix")
    assert p.longest_song() is None

    a = Song("Morning Steppe", "Nomin", 205)
    b = Song("Blue Sky", "Temuulen", 180)
    c = Song("Night Train", "Nomin", 240)
    d = Song("Long Road", "Anu", 240)
    for song in [a, b, c, d]:
        p.add_song(song)

    assert p.longest_song() is c
    assert p.songs_by("Nomin") == ["Morning Steppe", "Night Train"]
    assert p.songs_by("Anu") == ["Long Road"]
    assert p.songs_by("Nobody") == []
