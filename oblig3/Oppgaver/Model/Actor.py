from Oppgaver.Model.Person import Person


class Actor(Person):
    def __init__(self, fullname, birth):
        super().__init__(fullname, birth)
