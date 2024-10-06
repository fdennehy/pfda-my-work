# Simple program to read a csv file as a dictionary
# Author: Finbar Dennehy

import csv

FILENAME = "data.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp: # fp file pointer
    reader = csv.DictReader(fp, delimiter="," , quoting = csv.QUOTE_NONNUMERIC) # if thinsg are not quoted, they are floating points
    total = 0
    for line in reader:
        total += line['id']
        print (line)
    print(f"total of ids is {total}")