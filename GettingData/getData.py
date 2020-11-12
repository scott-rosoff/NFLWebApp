import pandas as pd 
from sportsreference.nfl.teams import Teams
from sportsreference.nfl.boxscore import Boxscores
from sportsreference.nfl.roster import Player

start_year = 2019
end_year = 2020

# iterate over each game to retrieve the boxscore URI for more enriched querying later
boxscore_URIs = []
for year in range(start_year, end_year+1):
    print("Retrieving box scores for year {0}".format(year))
    games = Boxscores(week = 1, year = year, end_week = 16).games    
    # iterate over every game of the season
    for week, value in games.items():
        URI = games[week][0]['boxscore']
        boxscore_URIs.append(URI)

for boxscore_uri in boxscore_URIs:
        


