# Case study of iris data set
# Calculate area of sepal and petals
# Author: Finbar Dennehy

import csv

FILENAME= "irisquotes.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)

    for line in reader:
        sepal_size = line[0] * line[1]
        petal_size = line[2] * line[3]
        line.append(sepal_size)
        line.append(petal_size)
        print(line)