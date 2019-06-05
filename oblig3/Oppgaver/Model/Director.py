from Oppgaver.Model.Person import Person


class Director(Person):
    def __init__(self, fullname, birth):
        super().__init__(fullname, birth)
