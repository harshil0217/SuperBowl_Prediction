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



game_data = pd.read_csv("../Data/Processed_Data/game_data.csv")

game_data

game_stats = game_data[game_data.columns[:15]]

game_stats = game_stats.drop(["date", "team"], axis = 1)

game_stats
atts = game_stats.columns

len(game_stats)

game_stats
wins = game_stats[game_stats["Made_Conf_Fin"] == 1]
len(wins)/len(game_stats)

# +
split = StratifiedShuffleSplit(n_splits = 1, test_size = 0.2, random_state = 69)

for train_index, test_index in split.split(game_stats, game_stats["Made_Conf_Fin"]):
    game_train = game_stats.loc[train_index]
    game_test = game_stats.loc[test_index]

    


sb_train = game_train["Made_Conf_Fin"]
sb_test = game_test["Made_Conf_Fin"]

game_train = game_train.drop(["Made_Conf_Fin"], axis = 1)
game_test = game_test.drop(["Made_Conf_Fin"], axis = 1)

game_train
# -

game_test

logit_model = sm.Logit(sb_train, sm.add_constant(game_train))
result = logit_model.fit()
print(result.summary())



print(len(game_test))
game_test

logreg = LogisticRegression(penalty = "l2")

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
    'penalty' : ['l2'], 
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




