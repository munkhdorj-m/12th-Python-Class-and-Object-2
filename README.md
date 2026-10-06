# Python Class and Objects 2

Python Class and Objects PDF:

https://drive.google.com/file/d/1GHMSwiOsYEQY1oRaJ548FfOX41OujLdd/view?usp=sharing

**Rules for this assignment**

- Write each class in `assignment.py`. Do not rename anything — names of classes,
  attributes and methods must match this README **exactly**.
- Every attribute must be created inside `__init__` using `self.something = ...`
- Every method needs `self` as its first parameter.
- When a method says it **returns** something, use `return` — do not `print`.

---

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

*Hint:* `205 // 60` gives the minutes, `205 % 60` gives the seconds left over.

---

## Exercise 4

**Problem:**

- Create a `Fighter` class for a simple game.
  - Attributes: `name`, `health`, `power`
  - Methods:
    - `is_alive()` → **returns** `True` if `health` is more than `0`,
      otherwise `False`
    - `hit(other)` → `other` is **another `Fighter` object**.
      Take this fighter's `power` away from the other fighter's `health`.
      - Health can never go below `0`.
      - A fighter who is not alive cannot hit — nothing happens.

Example:

    Input:
      bat = Fighter("Bat", 100, 30)
      dorj = Fighter("Dorj", 50, 20)

      bat.hit(dorj)
      print(dorj.health)

      bat.hit(dorj)
      print(dorj.health, dorj.is_alive())

      dorj.hit(bat)
      print(bat.health)

    Output:
      20
      0 False
      100

---

## Exercise 5 (Optional)

**Problem:**

Battle game: you against the computer.

First, add two things to your `Fighter` class:

- an attribute `max_health` → the health the fighter started with
- a method `heal(amount)` → adds `amount` to `health`, but never above `max_health`

Then write the game in a new file `battle.py`:

- Ask for the player's name. Player: 100 health, 20 power.
  Computer: 100 health, 20 power.
- Each round, show both fighters' health, then ask: attack (`a`) or heal (`h`).
- The player has only **3 potions**. Each heal uses one and gives 25 health.
- After the player's move, the computer hits back (if it is still alive).
  When its health is low, it sometimes heals instead — use `random`.
- The game ends when one fighter is knocked out. Print the winner.

**Example**

    Enter your fighter's name: Bat

    --- Round 1 ---
      Bat: 100/100 HP
      Computer: 100/100 HP
      Potions left: 3
    Attack (a) or heal (h)? a
    Bat hits Computer for 20!
    Computer hits Bat for 20!

    --- Round 2 ---
      Bat: 80/100 HP
      Computer: 80/100 HP
      Potions left: 3
    Attack (a) or heal (h)? h
    Bat heals.
    Computer hits Bat for 20!
    ...

    Bat wins!

---

## How to test your work

    pytest -v

Each exercise is checked by several tests, and each test is worth 1 point.
If a test fails, read the **HINT** box under the error — it usually tells you
exactly what is wrong.
