class Episode:
    def __init__(self, title, season, episoderNumber, playtime):
        self.title = title
        self.season = season
        self.episodeNumber = episoderNumber
        self._playtime = playtime

    def get_playtime(self):
        return self._playtime

    def __str__(self):
        return "S: " + str(self.season) + ", E: " + str(self.episodeNumber) + " Playtime: " + str(self._playtime) + ", Title: " + self.title

