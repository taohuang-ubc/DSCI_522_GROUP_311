# author: Group 311 - Tao Huang, Xugang(Kirk) Zhong, Hanying Zhang
# date: 2020-01-23

'''This script performs data wrangling and paritionting on the data to train and test splits. 
The four splits will be: X_train, X_test, y_train and y_test. These splits will be written to local files.

Usage: src/data_process.py --filepath=<filepath> --output_path=<output_path>

Options: 
--filepath=<filepath>    Local file path to read the original data file (including filename) eg. "data/raw/red_wine.csv"
--output_path=<output_path>    Local file path to write the processed data file (should not include filename and "/" at the end) eg. "data/processed"
'''

# import configparser
import pandas as pd
from janitor import clean_names
from sklearn.model_selection import train_test_split
from docopt import docopt

opt = docopt(__doc__)

def main(filepath, output_path):
    data = pd.read_csv(filepath)
    data = clean_names(data)

    # clean the column names
    X = data.drop(columns = ['quality'])
    y = data[['quality']]

    # split the data and save the splits
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
    X_train.to_csv(output_path + "/X_train.csv", index=False)
    X_test.to_csv(output_path + "/X_test.csv", index=False)
    y_train.to_csv(output_path + "/y_train.csv", index=False)
    y_test.to_csv(output_path + "/y_test.csv", index=False)

if __name__ == "__main__":
    main(opt["--filepath"], opt["--output_path"])
