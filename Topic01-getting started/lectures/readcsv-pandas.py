# Reading in the csv as a pandas table
# Author: Finbar Dennehy

FILENAME = "data.csv"
DATADIR = "../datafiles/"

import pandas
df = pandas.read_csv(DATADIR + FILENAME)
print (df)