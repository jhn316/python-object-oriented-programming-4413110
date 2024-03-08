# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen=True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self,newval):
        self.value2 = newval

obj = ImmutableClass()
print(obj.value1, obj.value2)

# TODO: attempting to change the value of an immutable class throws an exception
#obj.value1 ="blah"
#print(obj.value1, obj.value2)


# TODO: even functions within the class can't change anything
#obj.some_func(10)

# We can still  assign values at creation of the object
# but still cannot change the values aftewards
obj = ImmutableClass("Another string", 20)
obj.some_func(10)