import pandas as pd 
from sportsreference.nfl.teams import Teams
from sportsreference.nfl.boxscore import Boxscore, Boxscores
from sportsreference.nfl.roster import Player
import time
from datetime import datetime

def get_boxscores(start_year, end_year):
    """
    Returns a dataframe containing per-game NFL stats
    Input: int @start-year , int @end_year
    Output: pandas dataframe
    """
    t0 = time.time()
    boxscore_URIs = []
    dfs = []
    for year in range(start_year, end_year+1):
        print("Retrieving box scores for year {0}".format(year))
        try:
            games = Boxscores(week = 1, year = year, end_week = 16).games
        except:
            print('Please provide a valid year parameter')
        # iterate over every game of the season
        for week, value in games.items():
            URI = games[week][0]['boxscore']
            game_df = Boxscore(URI).dataframe
            # if game hasn't happened yet, skip ahead
            if game_df is None:
                break
            game_df = game_df[['away_fumbles', 
                'home_fumbles', 'away_interceptions', 'home_interceptions', 'away_pass_yards', 
                'home_pass_yards', 'away_pass_attempts', 'home_pass_attempts', 'away_pass_completions',
                'home_pass_completions', 'away_pass_touchdowns', 'home_pass_touchdowns', 
                'away_points', 'home_points', 'away_rush_attempts', 'home_rush_attempts',
                'away_rush_touchdowns', 'home_rush_touchdowns', 'away_rush_yards', 'home_rush_yards',
                'away_times_sacked', 'home_times_sacked', 'away_turnovers', 'home_turnovers'
            ]]
            game_df['Season'] = year
            game_df['Week'] = week
            game_df['away_abbreviation'] = Boxscore(URI).away_abbreviation
            game_df['home_abbreviation'] = Boxscore(URI).home_abbreviation
            dfs.append(game_df)
            df = pd.concat(dfs)
    elapsed = (time.time() - t0)
    print("Elapsed time: {0}".format(elapsed))
    return  df        


def agg_data_YTD(games_df, end_week):
    """
    Returns the Year-to-Date(YTD) stats per team up until specified ending date (exclusive)
    Input: {@games_df : pandas dataframe,
            @end_week : int
    } 
    Output: pandas dataframe
    """
    return


def if __name__ == "__main__":
    df = get_boxscores(2018, 2020)
    print('end')