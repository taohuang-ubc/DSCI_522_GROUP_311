# author: Group 311 - Tao Huang, Xugang(Kirk) Zhong, Hanying Zhang
# date: 2020-01-19

'''This script downloads data file from a url and writes it to local. 
This script takes a URL and a local file path as the arguments.
The URL used for this file should be ended with '.csv', here is an example: 
"https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

Usage: src/data_download.py --url=<url> --filepath=<filepath> --filename=<filename>

Options:
--url=<url>              URL from where to download the data (a zip file with data zipped in standard csv format)
--filepath=<filepath>    Local file path to write the data file
--filename=<filename>    Local file name
'''

import pandas as pd
import requests
import os
from docopt import docopt

opt = docopt(__doc__)

def main(url, filepath, filename):
    filepath_long = filepath + "/" + filename + ".csv"

    # check file path
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    # download csv file from url
    try: 
        data = pd.read_csv(url, sep=";")
        data.to_csv(filepath_long, index=False)
    except Exception as e:
        print("Unable to download. Please check your URL again to see whether it is pointing to a downloadable file.")
        print(e)

def test_url(url):
    '''
    This functions tests the existence of the input URL, and also checks if it is ended as '.csv'.
    '''
    try: 
        request = requests.get(url, stream=True)
        request.status_code == 200 # successful request
    except Exception as ex:
        print("URL does not exist.")
        print(ex)

    assert url[-4:] == '.csv', "The URL must point to a csv file!"

if __name__ == "__main__":
    test_url(opt["--url"])
    main(opt["--url"], opt["--filepath"], opt["--filename"])