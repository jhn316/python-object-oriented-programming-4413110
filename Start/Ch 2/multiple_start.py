# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance

# Note that, the super().__init__() line in both class A and class B 
# definitions ensures that both A and B contribute to the initialization 
# process when creating an instance of C. It maintains a consistent behavior 
# across the inheritance hierarchy.

class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.name = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.name = "Class B"

class C(A, B):
    def __init__(self):
        super().__init__()

    def showprops(self):
        print(self.prop1)
        print(self.prop2)
        print(self.name)


c = C()
print(C.__mro__)
c.showprops()