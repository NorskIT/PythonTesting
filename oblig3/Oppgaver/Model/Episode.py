from Oppgaver.Model.Production import Production


class Episode(Production):
    def __init__(self, title, season, episode_number, playtime, release_date, director):
        super().__init__(title, playtime, release_date, director)
        self._season = season
        self._episode_number = episode_number

    def __str__(self):
        return "S: " + str(self._season) + ", E: " + str(self._episode_number) + " Playtime: " + str(
            self._playtime) + ", Title: " + self._title

    @property
    def get_season(self):
        return self._season

    @property
    def get_episode_number(self):
        return self._episode_number

    @property
    def set_title(self, title):
        self._title = title

