from Oppgaver.Model.Production import Production


class Movie(Production):
    def __init__(self, title, playtime, release_date, director, desc):
        super().__init__(title, playtime, release_date, director)
        self._desc = desc

    @property
    def get_description(self):
        return self._desc

