# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.

Usage: docopt.py --filepath=<filepath> --fileoutpath=<fileoutpath>

Options:

--filepath=<filepath>     Takes any value (this is a required option)
--fileoutpath=<fileoutpath>   Takes any value (this is an optional option)
"""

import pandas as pd


def main(filepath,filename):
    df = pd.read_csv(filepath)

