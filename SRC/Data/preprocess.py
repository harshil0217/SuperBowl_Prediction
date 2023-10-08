import pandas as pd
import utils

game_data = pd.read_csv("../../Data/Raw_Data/nfl_team_stats_2002-2022.csv")

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






