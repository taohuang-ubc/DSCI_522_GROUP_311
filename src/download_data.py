# author: Group 311 - Tao Huang, Xugang(Kirk) Zhong, Hanying Zhang
# date: 2020-01-19

'''This script downloads data file from a url and writes it to local with train and 
test data split. This script takes a URL and a local file path as the arguments.

Usage: src/download_data.py --url=<url> --filepath=<filepath> --filename=<filename>

Options:
--url=<url>              URL from where to download the data (a zip file with data zipped in standard csv format)
--filepath=<filepath>    Local file path to write the data file
--filename=<filename>    Local file name
'''

import pandas as pd
import requests
import os
from sklearn.model_selection import train_test_split
from docopt import docopt

opt = docopt(__doc__)

def main(url, filepath, filename):
    filepath_long = filepath + "/" + filename + ".csv"

    # check file path
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    # download file from url
    try: 
        request = requests.get(url, stream=True)
        request.status_code == 200 # successful request
    except Exception as ex:
        print("False url.")
        print(ex)
    data = pd.read_csv(url, sep=";")
    data.to_csv(filepath_long, index=False)

    # split the data and save the splits
    train, test = train_test_split(data, test_size=0.20, random_state=1)
    train.to_csv(filepath + "/" + filename + "_train.csv", index=False)
    test.to_csv(filepath + "/" + filename +  "_test.csv", index=False)

if __name__ == "__main__":
    main(opt["--url"], opt["--filepath"], opt["--filename"])