import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import recall_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedShuffleSplit
import statsmodels.api as sm
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score



game_data = pd.read_csv("../Data/Processed_Data/game_data.csv")


game_data


game_stats = game_data[game_data.columns[2:24]]

# +
fig, ax = plt.subplots(figsize = (20,20))

corr_mat = game_stats.corr()
corr_mat
sns.heatmap(corr_mat, annot = True)
# -



game_stats.drop(["fourth_down_conversion_attempts", "first_downs", "int", "completions", "total_yards", "rushing_attempts",
                ], axis = 1, inplace = True)

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

game_train.drop(["def_st_td", "fumbles", "attempts", "penalty_yards", "sack_yards"], axis = 1, inplace = True)
game_test.drop(["def_st_td", "fumbles", "attempts", "penalty_yards", "sack_yards"], axis = 1, inplace = True)
logit_model = sm.Logit(sb_train, sm.add_constant(game_train))
result = logit_model.fit(maxiter = 2000)
print(result.summary())





preds = result.predict(sm.add_constant(game_test))
preds = round(preds)

mat = confusion_matrix(sb_test, preds)
mat

nfl_2022 = game_data[game_data["date"] == 2022]
nfl_2022_stats = nfl_2022.drop(["date", "team"], axis = 1)
nfl_2022_stats = nfl_2022_stats.drop(["def_st_td", "fumbles", "attempts", "penalty_yards", "sack_yards", "fourth_down_conversion_attempts", "first_downs", 
                                      "int", "completions", "total_yards", "rushing_attempts", "Superbowl Status"], axis = 1)
nfl_2022_stats


pred2022 = result.predict(sm.add_constant(nfl_2022_stats))
pred2022

nfl_2022["winner%"] = pred2022
nfl_2022

nfl_2022.sort_values("winner%", ascending = False)

prec = precision_score(sb_test, preds)
prec

print(sb_test[sb_test == 1])

print(len(game_test))
game_test

logreg = LogisticRegression()

logreg.fit(game_train, sb_train)

preds = logreg.predict(game_test)
preds

score = logreg.score(game_test, sb_test)
print(score)

recall = recall_score(sb_test, preds)

recall

mat = confusion_matrix(sb_test, preds)
mat

param_grid = { 
    'C'       : np.logspace(-3,3,7),
    'solver'  : ['newton-cg', 'lbfgs', 'liblinear'],
}

logreg = LogisticRegression()
grid_search = GridSearchCV(logreg, param_grid, cv = 3, scoring = 'recall', return_train_score = True)
grid_search.fit(game_train, sb_train)
preds = grid_search.predict(game_test)
mat = confusion_matrix(sb_test, preds)
mat

feature_importances = grid_search.best_estimator_.coef_

feature_importances

logit_model = sm.Logit(sb_train, sm.add_constant(game_train))
result = logit_model.fit()
print(result.summary())

rfc = RandomForestClassifier()
rfc.fit(game_train, sb_train)

preds = rfc.predict(game_test)
mat = confusion_matrix(sb_test, preds)
mat

preds

param_grid = {
'n_estimators': [100, 200, 500],
'max_depth': [5, 8, 15, 25],
'min_samples_split': [2, 5, 10],
'class_weight': ['balanced'],
}

rfc = RandomForestClassifier()
grid_search = GridSearchCV(rfc, param_grid, cv = 10, scoring = 'recall', return_train_score = True)
grid_search.fit(game_train, sb_train)
preds = grid_search.predict(game_test)
mat = confusion_matrix(sb_test, preds)
mat

len(game_train)

preds




