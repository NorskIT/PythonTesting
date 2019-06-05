class TVSeries:
    def __init__(self, totalSeasons, totalEpisodes, description, releaseDate):
        self.totalEpisodes = totalEpisodes
        self.totalSeasons = totalSeasons
        self.description = description
        self.releaseDate = releaseDate
        self.episodes = []
        self._average_time = 0

    def add_episode(self, episode):
        if episode.season>self.totalSeasons+1:
            print("Season number too high. Current season is: " + str(self.totalSeasons))
            return
        elif episode.season==self.totalSeasons+1:
            if episode.episodeNumber == 1:
                self.totalSeasons += 1
                self.episodes.append(episode)
            else:
                print("New season episode has to be number 1 episode number")
                return
        else :
            self.episodes.append(episode)
        self.totalEpisodes += 1
        self.update_average_playtime()

    def get_season_epiodes(self, season):
        episodes = []
        for episode in self.episodes:
            if episode.season == season:
                episodes.append(episode)
        return episodes.sort(key=lambda ep: ep.episodenumber, reverse=False)

    def get_latest_episode_in_season(self, season):
        return self.get_season_epiodes[-1]

    def update_average_playtime(self):
        for episode in self.episodes:
            self._average_time += episode.get_playtime()
        self._average_time = self._average_time/len(self.episodes)

    def average_time(self):
        hour, minute = divmod(self._average_time, 60)
        return "{}t og {}m".format(hour.__int__(), minute.__int__())




