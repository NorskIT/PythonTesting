import datetime
from random import randint

from Oppgaver.Model.Director import Director
from Oppgaver.Model.Episode import Episode
from Oppgaver.Model.Movie import Movie

from Oppgaver.Model.TVSeries import TVSeries


def main():
    new_tv_series = dummy_tv_series()

    print(new_tv_series.average_time())

    """
    Is this a comment?
    """
    for episode in new_tv_series.get_episodes:
        print(episode)

    new_movie = Movie(
        "Movie title",
        120,
        datetime.date(2000, 12, 12),
        Director("Mike John", datetime.date(1978, 1, 4)),
        "A great movie about move titles"
    )

    print(new_movie.get_playtime)

    pass


def dummy_tv_series():
    new_tv_series = TVSeries(0, 0, "My new tv serie", datetime.date.today())

    e = 1
    s = 1
    for x in range(50):
        new_tv_series.add_episode(Episode("episode title", s, e, randint(60, 160), datetime.date(2000, 3, 12),
                                          Director("Mike John", datetime.date(1978, 1, 4))))
        e += 1
        if x % 10 == 0:
            s += 1
            e = 1
    new_tv_series.sort_episodes()

    # Tries to add a episodes 2 numbers about current season
    new_tv_series.add_episode(Episode("episode title", 8, 7, randint(60, 160), datetime.date(2001, 12, 12),
                                      Director("Mike Smith", datetime.date(1999, 2, 2))))

    return new_tv_series


if __name__ == '__main__': main()
