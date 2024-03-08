# Python Object Oriented Programming by Joe Marini course example
# Using data classes to represent data objects

from dataclasses import dataclass

@dataclass
class Book:
    # note that for dataclass objects, these values will
    # automatically be interpreted by Python as instance 
    # attributes instead of class attribute
    title: str
    author: str
    pages: int
    price: float

    # def __init__(self, title, author, pages, price):
    #     self.title = title
    #     self.author = author
    #     self.pages = pages
    #     self.price = price

    def bookinfo(self):
        return f"{self.title} by {self.author}"



# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__ 
# (__repr__ is automatcially implemented in dataclasses)
print(b1)

# TODO: comparing two dataclasses - they implement __eq__
# (__eq__ is automatcially implemented in dataclasses)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
print(b1==b3)
print(b1==b2)

# TODO: change some fields
b1.title = "Anna Karenina"
b1.pages = 864
print(b1.bookinfo())