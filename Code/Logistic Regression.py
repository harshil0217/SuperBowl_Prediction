import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import StratifiedShuffleSplit
import statsmodels.api as sm
from imblearn.over_sampling import SMOTE
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA



game_data = pd.read_csv("../Data/Processed_Data/game_data.csv")


game_data


game_stats = game_data[game_data.columns[2:27]]

# +
fig, ax = plt.subplots(figsize = (20,20))

corr_mat = game_stats.corr()
corr_mat
sns.heatmap(corr_mat, annot = True)
# -



game_stats.drop(["fourth_down_conversion_attempts", "first_downs", "turnovers", "completions", "total_yards", "rushing_attempts",
                "penalties_number", "sacks_number", "score", "attempts"], axis = 1, inplace = True)
dropped = ["fourth_down_conversion_attempts", "first_downs", "turnovers", "completions", "total_yards", "rushing_attempts",
                "penalties_number", "sacks_number", "score", "attempts"]

game_stats

# +
fig, ax = plt.subplots(figsize = (20,20))

corr_mat = game_stats.corr()
corr_mat
sns.heatmap(corr_mat, annot = True)
# -

game_stats
atts = game_stats.columns

len(game_stats)

game_stats
wins = game_stats[game_stats["Superbowl Status"] == 1]
len(wins)/len(game_stats)


# +
split = StratifiedShuffleSplit(n_splits = 1, test_size = 0.2, random_state = 69)

for train_index, test_index in split.split(game_stats, game_stats["Superbowl Status"]):
    game_train = game_stats.loc[train_index]
    game_test = game_stats.loc[test_index]

    


sb_train = game_train["Superbowl Status"]
sb_test = game_test["Superbowl Status"]

game_train = game_train.drop(["Superbowl Status"], axis = 1)
game_test = game_test.drop(["Superbowl Status"], axis = 1)

game_train
# -

game_test

smote = SMOTE(random_state = 69)
game_train, sb_train = smote.fit_resample(game_train, sb_train)




game_train
sb_train

logit_model = sm.Logit(sb_train, sm.add_constant(game_train))
result = logit_model.fit(maxiter = 2000)
print(result.summary())

game_train.drop(["def_st_td", "fumbles", "rushing_yards", "fourth_down_conversions", "penalty_yards"
                ,"sack_yards"], axis = 1, inplace = True)
game_test.drop(["def_st_td", "fumbles", "rushing_yards", "fourth_down_conversions", "penalty_yards"
                ,"sack_yards"], axis = 1, inplace = True)
drop = ["def_st_td", "fumbles", "rushing_yards", "fourth_down_conversions", "penalty_yards"
                ,"sack_yards"]
for cat in drop:
    dropped.append(cat)
logit_model = sm.Logit(sb_train, sm.add_constant(game_train))
result = logit_model.fit(maxiter = 2000)
print(result.summary())

# +
grid = {
    
}
# -



preds = result.predict(sm.add_constant(game_test))
preds = round(preds)

mat = confusion_matrix(sb_test, preds)
mat

# +

print(classification_report(sb_test, preds))
# -







nfl_2022 = game_data[game_data["date"] == 2022]
nfl_2022_stats = nfl_2022.drop(["date", "team"], axis = 1)
nfl_2022_stats = nfl_2022_stats.drop(dropped, axis = 1)
nfl_2022_stats = nfl_2022_stats.drop("Superbowl Status", axis = 1)
nfl_2022_stats


pred2022 = result.predict(sm.add_constant(nfl_2022_stats))
pred2022

nfl_2022["winner%"] = pred2022
nfl_2022

nfl_2022 = nfl_2022.sort_values("winner%", ascending = False)
nfl_2022 = nfl_2022.drop(dropped, axis  = 1)

nfl_2022














































