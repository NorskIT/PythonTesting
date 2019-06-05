class Person:
    first = ""
    last = ""
    age = ""

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age


a = Person("A", "B", 5)

print(a.first + " " + a.last + " " + str(a.age))
