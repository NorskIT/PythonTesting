class Person:
    age = None

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


aDuded = Person("Joar", "Knudsen")

n = input("What is your age?")

aDuded.age = n

print(aDuded.lastname + " " + aDuded.firstname + ", age " + aDuded.age)
