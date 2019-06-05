class TVSeries:
    def __init__(self, total_seasons, total_episodes, description, release_date):
        self._totalEpisodes = total_episodes
        self._totalSeasons = total_seasons
        self._description = description
        self._release_date = release_date
        self._episodes = []
        self._average_time = 0

    def add_episode(self, episode):
        if episode.get_season > self._totalSeasons + 1:
            print("Season number too high. Current season is: " + str(self._totalSeasons))
            return
        elif episode.get_season == self._totalSeasons + 1:
            if episode.get_episode_number == 1:
                self._totalSeasons += 1
                self._episodes.append(episode)
            else:
                raise ValueError("New season episode has to be number 1 episode number")
        else:
            self._episodes.append(episode)
        self._totalEpisodes += 1
        self.update_average_playtime()

    def get_season_episodes(self, season):
        episodes = []
        for episode in self._episodes:
            if episode.get_season == season:
                episodes.append(episode)
        return episodes.sort(key=lambda ep: ep.episode_number, reverse=False)

    def get_latest_episode_in_season(self, season):
        return self.get_season_episodes(season)[-1]

    def update_average_playtime(self):
        for episode in self._episodes:
            self._average_time += episode.get_playtime
        self._average_time = self._average_time / len(self._episodes)

    def average_time(self):
        hour, minute = divmod(self._average_time, 60)
        return "{}t og {}m".format(hour.__int__(), minute.__int__())

    def sort_episodes(self):
        self._episodes.sort(key=lambda x: (x._season, x._episode_number), reverse=False)

    @property
    def get_episodes(self):
        return self._episodes

    def get_cast(self):
        print("GET_CAST_TVSERIE")
