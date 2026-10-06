# Python Class and Objects

Python Class and Objects PDF:

https://drive.google.com/file/d/1GHMSwiOsYEQY1oRaJ548FfOX41OujLdd/view?usp=sharing


---

## Exercise 1

**Problem:**

- Create a `Rectangle` class with:
  - Attributes: `length`, `width`
  - Methods:
    - `area()` → returns the area
    - `perimeter()` → returns the perimeter

Example:

    Input:
      r1 = Rectangle(5, 3)
      print("Area:", r1.area())
      print("Perimeter:", r1.perimeter())

    Output:
      Area: 15
      Perimeter: 16

---

## Exercise 2

**Problem:**

- Create a `Book` class with:
  - Attributes: `title`, `author`, `price`
  - Method:
    - `display()` → returns formatted string

Example:

    Input: 
      b1 = Book("Python Basics", "Alice", 29.99)
      print(b1.display())
      
    Output: 
      Title: Python Basics, Author: Alice, Price: $29.99
---

## Exercise 3

**Problem:**

- Create a `ShoppingCart` class with:
  - Method `add_item(name, price)` # where name and price are list
  - Method `total_price()` → returns total cost
  - Method `show_items()` → returns all items neatly listed
 
  
Example:

    Input: 
      cart = ShoppingCart()
      cart.add_item("Apple", 1.5)
      cart.add_item("Banana", 2.0)
      cart.add_item("Book", 10.0)
      print(cart.show_items())
      print("Total:", cart.total_price())
            
    Output: 
      Apple: $1.5
      Banana: $2.0
      Book: $10.0
      Total: 13.5

---

