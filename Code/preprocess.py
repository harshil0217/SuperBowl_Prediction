import pandas as pd
import utils

game_data = pd.read_csv("..//Data/Raw_Data/nfl_team_stats_2002-2022.csv")

len(game_data.columns)

game_data

from utils import get_winner
game_data = get_winner(game_data)

game_data = pd.melt(game_data, id_vars = game_data.columns[0:3], value_vars = game_data.columns[3:39], var_name = "stat", value_name = "stat_value")

game_data
game_data

game_data = pd.melt(game_data, id_vars = ["date", "stat", "stat_value"], value_vars = ["away", "home"], var_name = "home_status", value_name = "team")

game_data
game_data

from utils import filter_home_away_stats
game_data = filter_home_away_stats(game_data)

game_data.reset_index(drop = True, inplace= True)
game_data



game_data = game_data.drop(["home_status"], axis = 1)


from utils import ignore_home_away
game_data = ignore_home_away(game_data)


game_data = game_data.pivot(index = ["date", "team"], columns = "stat", values = "stat_value" )


game_data

game_data = game_data.reset_index()

game_data

new_dates = pd.to_datetime(game_data["date"])

game_data["date"] = new_dates

game_data



game_data



game_data





game_data





game_data

from utils import filter_out_postseason
game_data = filter_out_postseason(game_data, "date")


game_data



game_data



game_data



game_data



# +
from utils import simplify_date

game_data = simplify_date(game_data, "date")
game_data
# -

game_data = game_data.drop(["redzone"], axis = 1)

# +
game_data[["completions", "attempts"]] = game_data["comp_att"].str.split("-", expand = True)
game_data[["fourth_down_conversions", "fourth_down_conversion_attempts"]] = game_data["fourth_downs"].str.split("-", expand = True)
game_data[["penalties", "penalty_yards"]] = game_data["penalties"].str.split("-", expand = True)
game_data[["sacks", "sack_yards"]] = game_data["sacks"].str.split("-", expand = True)
game_data[["third_down_conversions", "third_down_attempts"]] = game_data["third_downs"].str.split("-", expand = True)

game_data.drop(["comp_att", "fourth_downs", "penalties", "sacks", "third_downs"], axis = 1, inplace = True)
game_data
# -

len(game_data.columns)

vals = game_data["possession"].str.split(":", expand = True)
game_data["possession"] = pd.to_numeric(vals[0]) + pd.to_numeric(vals[1])/60
game_data

# +
for i in range(2,len(game_data.columns)):
    game_data[game_data.columns[i]] = pd.to_numeric(game_data[game_data.columns[i]])
    
game_data
# -

game_data = game_data.groupby(["date", "team"]).sum()
game_data = game_data.reset_index()
game_data



# +
from utils import add_superbowl

game_data = add_superbowl(game_data, "date", "team")
game_data
# -





game_data.to_csv("..//Data/Processed_Data/game_data.csv", index = False)


