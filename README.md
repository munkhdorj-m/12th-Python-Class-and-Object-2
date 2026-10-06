# Python Class and Objects 2

Python Class and Objects PDF:

https://drive.google.com/file/d/1GHMSwiOsYEQY1oRaJ548FfOX41OujLdd/view?usp=sharing

**Rules for this assignment**

- Write each class in `assignment.py`. Do not rename anything — names of classes,
  attributes and methods must match this README **exactly**.
- Every attribute must be created inside `__init__` using `self.something = ...`
- Every method needs `self` as its first parameter.
- When a method says it **returns** something, use `return` — do not `print`.

## Exercise 1

**Problem:**

- Create a `BusCard` class for a city bus card.
  - Attributes:
    - `owner` → the name given when the card is created
    - `balance` → starts at `0`
    - `trips` → starts at `0`
  - Methods:
    - `top_up(amount)` → adds money to the card and **returns** `True`.
      If `amount` is `0` or negative, nothing changes and it **returns** `False`.
    - `pay(fare)` → takes the fare off the balance, adds 1 to `trips`, and
      **returns** `True`. If the balance is too low, nothing changes and it
      **returns** `False`. Paying exactly the whole balance is allowed.

Example:

    Input:
      card = BusCard("Bat")
      print(card.top_up(5000))
      print(card.top_up(-200))
      print(card.pay(500))
      print(card.pay(10000))
      print(card.balance, card.trips)

    Output:
      True
      False
      True
      False
      4500 1

---

## Exercise 2

**Problem:**

- Create a `Student` class.
  - Attributes:
    - `name`
    - `grades` → starts as an **empty list**
  - Methods:
    - `add_grade(score)` → adds `score` to `grades` and **returns** `True`.
      Only scores from `0` to `100` are allowed (both included).
      Any other score is not added, and it **returns** `False`.
    - `average()` → **returns** the average of the grades, rounded to
      1 decimal place with `round(value, 1)`. If there are no grades,
      **return** `0`.
    - `highest()` → **returns** the highest grade. If there are no grades,
      **return** `None`.

**Important:** create the empty list inside `__init__`. Every student must have
their own list — adding a grade to one student must not change another student.

Example:

    Input:
      s = Student("Saraa")
      s.add_grade(90)
      s.add_grade(85)
      s.add_grade(77)
      print(s.add_grade(150))
      print(s.grades)
      print(s.average())
      print(s.highest())

    Output:
      False
      [90, 85, 77]
      84.0
      90

---

## Exercise 3

**Problem:**

This exercise has **two** classes. A `Playlist` stores `Song` **objects**.

- Create a `Song` class.
  - Attributes: `title`, `artist`, `seconds`
  - Method:
    - `length()` → **returns** the length as a string `"minutes:seconds"`.
      The seconds part always has **two digits**: `65` seconds is `"1:05"`,
      not `"1:5"`.

- Create a `Playlist` class.
  - Attributes:
    - `name`
    - `songs` → starts as an **empty list**
  - Methods:
    - `add_song(song)` → adds a `Song` object to `songs`
    - `count()` → **returns** how many songs are in the playlist
    - `total_seconds()` → **returns** the total of all song lengths in seconds
    - `longest_song()` → **returns** the `Song` **object** with the most seconds.
      If two songs are equally long, return the one added first.
      If the playlist is empty, **return** `None`.
    - `songs_by(artist)` → **returns** a list of the **titles** of all songs by
      that artist, in the order they were added. Return `[]` if there are none.

Example:

    Input:
      p = Playlist("Road Trip")
      p.add_song(Song("Morning Steppe", "Nomin", 205))
      p.add_song(Song("Blue Sky", "Temuulen", 180))
      p.add_song(Song("Night Train", "Nomin", 240))

      print(p.count())
      print(p.total_seconds())
      print(p.songs[0].length())
      print(p.longest_song().title)
      print(p.songs_by("Nomin"))

    Output:
      3
      625
      3:25
      Night Train
      ['Morning Steppe', 'Night Train']

---
