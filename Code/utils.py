"""
This utils file contains all the custom functions used to preprocess the data in preprocess.py. It is imported at the
beginning of that file
"""

"""
All function docstrings have been generated by Claude.

Anthropic. (2023). Claude. Accessed from https://claude.ai/chats. 
    Prompt chain: {"write docstrings for the following functions"}
"""

import datetime
import pandas as pd


def HA_helper(x, stat_col, status_col):
    """Check if home/away status matches stat column
    
    Args:
        x: row from a dataframe 
        stat_col: column name in dataframe containing home/away status statistic 
        status_col: column name in dataframe containing current home/away status
        
    Returns: 
        bool: True if home/away status matches stat_col, False otherwise
        
    """
    if (x[status_col] == "away"):
        if "_away" in x[stat_col]:
            return True
    else:
        if "_home" in x[stat_col]:
            return True
    return False


def filter_home_away_stats(data):
    """Filters a dataframe to only include rows where home/away status matches stat
    
    Args:
        data: Dataframe containing:
            - stat: Column with home/away statistic 
            - home_status: Home or away status
            
    Returns: 
        Filtered dataframe where stats match home_away status
            
    """
    include = data.apply(lambda x: HA_helper(x, "stat", "home_status"), axis = 1)
    data = data[include]
    return data


def ignore_helper(x, stat_col):
    """Strips '_home' or '_away' from stat column
    
    Args:
        x: Row from a dataframe
        stat_col: Column in the dataframe containing the stat to strip
        
    Returns: 
        Row with stat_col value stripped of '_home' or '_away'
        
    """
    name = x[stat_col]
    if "_away" in name:
        name = name[:name.index("_away")]
    else:
        name = name[:name.index("_home")]
    x[stat_col] = name
    return x


def ignore_home_away(data):
    """Strips '_home' and '_away' suffixes from 'stat' columns in dataframe
    
    Args:
        data: Dataframe containing 'stat' column
        
    Returns:
        Dataframe with 'stat' column values stripped of '_home' and '_away' suffixes
        
    """
    data = data.apply(lambda x: ignore_helper(x, "stat"), axis = 1)
    return data













regular_season_timeframes = {
  2002: [datetime.date(2002, 9, 5), datetime.date(2003, 1, 5)],
  2003: [datetime.date(2003, 9, 4), datetime.date(2004, 1, 4)],
  2004: [datetime.date(2004, 9, 9), datetime.date(2005, 1, 2)],
  2005: [datetime.date(2005, 9, 8), datetime.date(2006, 1, 1)],
  2006: [datetime.date(2006, 9, 7), datetime.date(2007, 1, 1)],
  2007: [datetime.date(2007, 9, 6), datetime.date(2007, 12, 30)],
  2008: [datetime.date(2008, 9, 4), datetime.date(2008, 12, 28)],
  2009: [datetime.date(2009, 9, 10), datetime.date(2010, 1, 3)],
  2010: [datetime.date(2010, 9, 9), datetime.date(2011, 1, 2)],
  2011: [datetime.date(2011, 9, 8), datetime.date(2012, 1, 1)],
  2012: [datetime.date(2012, 9, 5), datetime.date(2012, 12, 30)],
  2013: [datetime.date(2013, 9, 5), datetime.date(2013, 12, 29)],
  2014: [datetime.date(2014, 9, 4), datetime.date(2014, 12, 28)],
  2015: [datetime.date(2015, 9, 10), datetime.date(2016, 1, 3)],
  2016: [datetime.date(2016, 9, 8), datetime.date(2017, 1, 1)],
  2017: [datetime.date(2017, 9, 7), datetime.date(2017, 12, 31)],
  2018: [datetime.date(2018, 9, 6), datetime.date(2018, 12, 30)],
  2019: [datetime.date(2019, 9, 5), datetime.date(2019, 12, 29)],
  2020: [datetime.date(2020, 9, 10), datetime.date(2021, 1, 3)],
  2021: [datetime.date(2021, 9, 9), datetime.date(2022, 1, 9)],
  2022: [datetime.date(2022, 9, 8), datetime.date(2023, 1, 8)]
}

season_timeframes = {
  2002: [datetime.date(2002, 9, 5), datetime.date(2003, 1, 26)], 
  2003: [datetime.date(2003, 9, 4), datetime.date(2004, 2, 1)],
  2004: [datetime.date(2004, 9, 9), datetime.date(2005, 2, 6)],
  2005: [datetime.date(2005, 9, 8), datetime.date(2006, 2, 5)],
  2006: [datetime.date(2006, 9, 7), datetime.date(2007, 2, 4)],
  2007: [datetime.date(2007, 9, 6), datetime.date(2008, 2, 3)],
  2008: [datetime.date(2008, 9, 4), datetime.date(2009, 2, 1)],
  2009: [datetime.date(2009, 9, 10), datetime.date(2010, 2, 7)],
  2010: [datetime.date(2010, 9, 9), datetime.date(2011, 2, 6)],
  2011: [datetime.date(2011, 9, 8), datetime.date(2012, 2, 5)],
  2012: [datetime.date(2012, 9, 5), datetime.date(2013, 2, 3)],
  2013: [datetime.date(2013, 9, 5), datetime.date(2014, 2, 2)],
  2014: [datetime.date(2014, 9, 4), datetime.date(2015, 2, 1)],
  2015: [datetime.date(2015, 9, 10), datetime.date(2016, 2, 7)],
  2016: [datetime.date(2016, 9, 8), datetime.date(2017, 2, 5)],
  2017: [datetime.date(2017, 9, 7), datetime.date(2018, 2, 4)],
  2018: [datetime.date(2018, 9, 6), datetime.date(2019, 2, 3)],
  2019: [datetime.date(2019, 9, 5), datetime.date(2020, 2, 2)],
  2020: [datetime.date(2020, 9, 10), datetime.date(2021, 2, 7)],
  2021: [datetime.date(2021, 9, 9), datetime.date(2022, 2, 13)],
  2022: [datetime.date(2022, 9, 8), datetime.date(2023, 2, 12)]
}


# +
def postseason_helper(x, date_col):
    """Check if date is in regular season or postseason
    
    Args:
        x (row): Row from a dataframe
        date_col (str): Column name containing the date
                
    Returns:
        bool: True if date is in postseason, False if in regular season
            
    """
    date = x[date_col]
    season = 0
    for key, value in season_timeframes.items():
        if value[0] <= date.date() <= value[1]:
            season = key
            break
    dates = regular_season_timeframes[season]
    if dates[0] <= date.date() <= dates[1]:
        return True
    return False
        
    


# +
def filter_out_postseason(data, date_col):
    """Filter dataframe to only regular season data
    
    Args:
        data (dataframe): Dataframe containing date_col
        date_col (str): Column name containing the date
        
    Returns: 
        Filtered dataframe containing only regular season data
        
    """
    keep = data.apply(lambda x: postseason_helper(x, date_col), axis = 1)
    data = data[keep]
    return data
    
    
    
    
    
    
# -

def date_helper(x, date_col):
    """Converts date to season year
    
    Args:
        x (row): Row from a dataframe
        date_col (str): Column containing date 
        
    Returns:
        Row with date value converted to season year (e.g. 2022)
        
    """
    date = x[date_col]
    for key, value in regular_season_timeframes.items():
        if value[0] <= date.date() <= value[1]:
            date = key
            break
    x[date_col] = date
    return x


def simplify_date(data, date_col):
    """Converts dates in dataframe to season years
    
    Args:
        data (dataframe): Dataframe containing date_col
        date_col (str): Column name with date values
        
    Returns: 
        Dataframe with date values converted to season years 
        
    """
    data = data.apply(lambda x: date_helper(x, date_col), axis = 1)
    return data


superbowls = {
  2002: "Buccaneers",
  2003: "Patriots",
  2004: "Patriots",
  2005: "Steelers",
  2006: "Colts",
  2007: "Giants",
  2008: "Steelers",
  2009: "Saints",
  2010: "Packers",
  2011: "Giants",
  2012: "Ravens",
  2013: "Seahawks",
  2014: "Patriots",
  2015: "Broncos",
  2016: "Patriots",
  2017: "Eagles",
  2018: "Patriots",
  2019: "Chiefs",
  2020: "Buccaneers",
  2021: "Rams",
  2022: "Chiefs"
}


def superbowl_helper(x, year_col, team_col):
    """Check if a team won the Super Bowl in a given year
    
    Args:
        x (row): Row from a dataframe
        year_col (str): Column name with season year 
        team_col (str): Column name with team name
        
    Returns:
        int: 1 if team won Super Bowl in year, 0 otherwise
        
    """
    year = x[year_col]
    team = x[team_col]
    winner = superbowls[year]
    if winner == team:
        return 1
    else:
        return 0


def add_superbowl(data, year_col, team_col):
    """Add column indicating if team won Super Bowl that year
    
    Args:
        data (dataframe): Dataframe
        year_col (str): Season year column name
        team_col (str): Team name column name
        
    Returns:
        Dataframe with new column 'Superbowl Status' indicating 1 if team 
        won SB that year, 0 otherwise
    """
    
    superbowl = data.apply(lambda x: superbowl_helper(x, year_col, team_col), axis = 1)
    data["Superbowl Status"] = superbowl
    return data







def winner_helper(x):
    """Determine winner between home and away teams.
    
    Args:
        x (row): Row from a dataframe containing:
            - score_away: Away team score 
            - score_home: Home team score
            
    Returns: 
        List indicating win/loss for [away team, home team], with 1 indicating
        a win and 0 indicating a loss. Ties return [0, 0]

    """
    away = x["score_away"]
    home = x["score_home"]
    if away > home:
        return [1,0]
    elif away < home:
        return [0,1]
    else:
        return [0,0]


def get_winner(data):
    """Add win/loss columns for away and home teams
    
    Args:
        data (dataframe): Dataframe containing:
            - score_away: Away team score
            - score_home: Home team score
            
    Returns: 
        Dataframe with new columns 'wins_away' and 'wins_home' indicating
        1 for a win and 0 for a loss or tie. Removes the score columns.
        
    """
    x = data.apply(lambda x: winner_helper(x), axis = 1, result_type = "expand")
    data["wins_away"] = x[0]
    data["wins_home"] = x[1]
    return data


