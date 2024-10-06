# Case study of iris data set
# Calculate area of sepal and petals
# Author: Finbar Dennehy

import csv

FILENAME= "irisquotes_header.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)

    for line in reader:
        sepal_area = line['sepal_length'] * line['sepal_width']
        petal_area = line['petal_length'] * line['petal_width']
        line["sepal_area"] = sepal_area
        line["petal_area"] = petal_area
        print(line)