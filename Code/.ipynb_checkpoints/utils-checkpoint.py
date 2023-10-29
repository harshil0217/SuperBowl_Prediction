import datetime


def HA_helper(x, stat_col, status_col):
    if (x[status_col] == "away"):
        if "_away" in x[stat_col]:
            return True
    else:
        if "_home" in x[stat_col]:
            return True
    return False


def filter_home_away_stats(data):
    include = data.apply(lambda x: HA_helper(x, "stat", "status"), axis = 1)
    data = data[include]
    return data


def ignore_helper(x, stat_col):
    name = x[stat_col]
    if "_away" in name:
        name = name[:name.index("_away")]
    else:
        name = name[:name.index("_home")]
    x[stat_col] = name
    return x


def ignore_home_away(data):
    data = data.apply(lambda x: ignore_helper(x, "stat"), axis = 1)
    return data


def percent_helper(x):
    x = x.split("-")
    val = float(x[0])/float(x[1])
    return val


def turn_into_percent(data):
    data = data.apply(lambda x: percent_helper(x))
    return data


def simplify_helper(x, col):
    pens = x[col]
    pens = pens.split("-")
    yards = pens[1]
    x[col] = yards
    return x


def simplify_to_yards(data, col):
    data = data.apply(lambda x: simplify_helper(x, col), axis = 1)
    return data


def attempt_helper(x, yards_col, attempt_col):
    yards = x[yards_col]
    attempt = x[attempt_col]
    per = yards/attempt
    return per


def per_attempt(data, yards_col, attempt_col, per_col):
    per_att = data.apply(lambda x: attempt_helper(x, yards_col, attempt_col), axis =1)
    data[per_col] = per_att
    return data


regular_season_timeframes = {
  2002: [datetime.date(2002, 9, 5), datetime.date(2003, 1, 5)],
  2003: [datetime.date(2003, 9, 4), datetime.date(2004, 1, 4)],
  2004: [datetime.date(2004, 9, 9), datetime.date(2005, 1, 2)],
  2005: [datetime.date(2005, 9, 8), datetime.date(2006, 1, 1)],
  2006: [datetime.date(2006, 9, 7), datetime.date(2007, 1, 1)],
  2007: [datetime.date(2007, 9, 6), datetime.date(2008, 12, 30)],
  2008: [datetime.date(2008, 9, 4), datetime.date(2009, 12, 28)],
  2009: [datetime.date(2009, 9, 10), datetime.date(2010, 1, 3)],
  2010: [datetime.date(2010, 9, 9), datetime.date(2011, 1, 2)],
  2011: [datetime.date(2011, 9, 8), datetime.date(2012, 1, 1)],
  2012: [datetime.date(2012, 9, 5), datetime.date(2012, 12, 30)],
  2013: [datetime.date(2013, 9, 5), datetime.date(2013, 12, 29)],
  2014: [datetime.date(2014, 9, 4), datetime.date(2014, 12, 28)],
  2015: [datetime.date(2015, 9, 10), datetime.date(2016, 1, 3)],
  2016: [datetime.date(2016, 9, 8), datetime.date(2017, 1, 1)],
  2017: [datetime.date(2017, 9, 7), datetime.date(2018, 12, 31)],
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
    date = x[date_col]
    season = 0
    for key, value in season_timeframes.items():
        if value[0] <= date <= value[1]:
            season = key
            break
    dates = regular_season_timeframes[season]
    if dates[0] <= date <= dates[1]:
        return True
    return False
        
    


# +
def filter_out_postseason(data, date_col):
    keep = data.apply(lambda x: postseason_helper(x, date_col), axis = 1)
    data = data[keep]
    return data
    
    
    
    
    
    
# -

def date_helper(x, date_col):
    date = x[date_col]
    for key, value in regular_season_timeframes.items():
        if value[0] <= date <= value[1]:
            date = key
            break
    x[date_col] = date
    return x


def simplify_date(data, date_col):
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
    year = x[year_col]
    team = x[team_col]
    winner = superbowls[year]
    if winner == team:
        return 1
    else:
        return 0


def add_superbowl(data, year_col, team_col):
    superbowl = data.apply(lambda x: superbowl_helper(x, year_col, team_col), axis = 1)
    data["Superbowl Status"] = superbowl
    return data


