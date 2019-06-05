from Oppgaver.Model.Person import Person


class Production:

    def __init__(self, title, playtime, release_date, director):
        self._title = title
        self._playtime = playtime
        self._release_date = release_date
        self._director = director
        self._cast = []

    @property
    def get_playtime(self):
        return self._playtime

    @property
    def get_director(self):
        return self._director

    def add_cast(self, role):
        self._cast.append(role)

    def add_casts(self, roles):
        for role in roles:
            self._cast.append(role)

    @property
    def get_cast(self):
        return self._cast
