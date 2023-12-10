# SuperBowl_Prediction

This Repository is divded into two directories, "Code" and "Data". The Data directory is further divided into Raw_Data and Processed_Data directories. The Raw_Data folder contains the initial csv file that is then cleaned and categorized during preprocessing. It is a documentation of the stats for every NFl game from 2002-2023. The Processed_Data folder contains the output csv generated from preprocessing, titled "game_data.csv". This data contains the regular season summary statistics for every NFL team from 2002-2020.

The Code directory contains four files. Preprocess.py handles the preprocessing of the raw data. It imports various helper functions from utils.py. There are two regressions conducted: a logistic regression and a pca-modified logistic regression. Each is located in its own respective notebook file.
