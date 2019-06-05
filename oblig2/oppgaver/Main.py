import datetime
from random import randint

from oppgaver.Episode import Episode

from oppgaver.TVSeries import TVSeries

newTVSeries = TVSeries(0, 0, "My new tv serie", datetime.date.today())

e = 1
s = 1
for x in range(50):
    newTVSeries.add_episode(Episode("episode title", s, e, randint(60, 160)))
    e += 1
    if x % 10 == 0:
        s += 1
        e = 1

# Sorts episode list by season and then episode
newTVSeries.episodes.sort(key=lambda x: (x.season, x.episodeNumber), reverse=False)

newTVSeries.add_episode(Episode("episode title", 8, 7, randint(60, 160)))

print(newTVSeries.average_time())

for episode in newTVSeries.episodes:
    print(episode)
