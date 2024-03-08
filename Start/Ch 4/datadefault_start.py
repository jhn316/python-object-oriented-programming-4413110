# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(20,40))

@dataclass
class Book:
    # you can define default values when attributes are declared
    #price: float #items without defults need to be declared first 
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    #price: float = field(default=10.0) #we can also use field function
    price: float = field(default_factory=price_func) #can add a function instead of value

b1 = Book()
print(b1)

b2 = Book("War and Peace", "Leo Tolstoy", 1225)
b3 = Book("Blah blag", "Leo Tolstoy",234)
print(b2)
print(b3)