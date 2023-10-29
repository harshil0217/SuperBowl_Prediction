import pandas as pd
import utils

game_data = pd.read_csv("..//Data/Raw_Data/nfl_team_stats_2002-2022.csv")

len(game_data.columns)

game_data

game_data = pd.melt(game_data, id_vars = game_data.columns[0:3], value_vars = game_data.columns[3:39], var_name = "stat", value_name = "stat_value")

game_data
game_data

game_data = pd.melt(game_data, id_vars = ["date", "stat", "stat_value"], value_vars = ["away", "home"], var_name = "status", value_name = "team")

game_data
game_data

from utils import filter_home_away_stats
game_data = filter_home_away_stats(game_data)

game_data.reset_index(drop = True, inplace= True)
game_data



game_data = game_data.drop(["status"], axis = 1)


from utils import ignore_home_away
game_data = ignore_home_away(game_data)


game_data = game_data.pivot(index = ["date", "team"], columns = "stat", values = "stat_value" )


game_data

game_data = game_data.reset_index()

game_data

new_dates = pd.to_datetime(game_data["date"])

game_data["date"] = new_dates

game_data

game_data = game_data.drop([ "fourth_downs", "possession", "fumbles", "int", "redzone"], axis = 1)

game_data

from utils import turn_into_percent
comp_perc = game_data["comp_att"]
comp_perc = turn_into_percent(comp_perc)
game_data["comp_perc"] = comp_perc
game_data.drop(["comp_att"], inplace = True, axis = 1)

game_data

from utils import simplify_to_yards
game_data = simplify_to_yards(game_data, "penalties")
game_data

from utils import per_attempt
game_data = per_attempt(game_data, "rushing_yards", "rushing_attempts", "yards_per_carry" )

game_data

game_data = simplify_to_yards(game_data, "sacks")
game_data

conv_rate = game_data["third_downs"]
conv_rate = turn_into_percent(conv_rate)
game_data["third_down_conversion_rate"] = comp_perc
game_data.drop(["third_downs"], inplace = True, axis = 1)

game_data

from utils import filter_out_postseason
game_data = filter_out_postseason(game_data, "date")


game_data

from utils import simplify_date
game_data = simplify_date(game_data, "date")

game_data

game_data = game_data.groupby(["date", "team"]).mean()

game_data

game_data = game_data.reset_index()

game_data

# +
from utils import add_superbowl

#game_data = add_superbowl(game_data, "date", "team")
#game_data
# -



# +
from utils import add_conf

game_data = add_conf(game_data, "date", "team")
game_data
# -

game_data.to_csv("..//Data/Processed_Data/game_data.csv", index = False)
