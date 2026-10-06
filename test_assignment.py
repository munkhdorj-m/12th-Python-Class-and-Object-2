import pytest
from assignment import Rectangle, Book, ShoppingCart

@pytest.mark.parametrize("length, width, expected_area, expected_perimeter", [
    (5, 3, 15, 16),   # normal case
    (10, 2, 20, 24),  # different ratio
    (1, 1, 1, 4),     # square
    (0, 5, 0, 10),    # zero length edge case
])
def test1(length, width, expected_area, expected_perimeter):
    rect = Rectangle(length, width)
    assert rect.area() == expected_area
    assert rect.perimeter() == expected_perimeter

@pytest.mark.parametrize("title, author, price, expected_output", [
    ("Python Basics", "Alice", 29.99, "Title: Python Basics, Author: Alice, Price: $29.99"),
    ("AI Guide", "Bob", 45.5, "Title: AI Guide, Author: Bob, Price: $45.5"),
    ("Data Science", "Charlie", 0, "Title: Data Science, Author: Charlie, Price: $0"),
])
def test2(title, author, price, expected_output):
    book = Book(title, author, price)
    assert book.display() == expected_output

def test3_1():
    cart = ShoppingCart()
    cart.add_item("Apple", 1.5)
    cart.add_item("Banana", 2.0)
    cart.add_item("Book", 10.0)
    assert cart.total_price() == pytest.approx(13.5)

@pytest.mark.parametrize("items, expected_output, expected_total", [
    ([("Pen", 2), ("Notebook", 5)], "Pen: $2\nNotebook: $5", 7),
    ([("Milk", 3.5)], "Milk: $3.5", 3.5),
    ([("A", 1), ("B", 2), ("C", 3)], "A: $1\nB: $2\nC: $3", 6),
])
def test3_2(items, expected_output, expected_total):
    cart = ShoppingCart()
    for name, price in items:
        cart.add_item(name, price)

    actual_output = cart.show_items().strip()  
    expected_output = expected_output.strip()  

    assert actual_output == expected_output
    assert cart.total_price() == expected_total
