# Case study of iris data set
# Calculate area of sepal and petals
# Author: Finbar Dennehy

import csv

FILENAME= "iris.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter="," , quoting=csv.QUOTE_NONE) # Default quoting is none - no quotes on data.

    for line in reader:
        sepal_size = float(line[0]) * float(line[1])
        petal_size = float(line[2]) * float(line[3])
        line.append(sepal_size)
        line.append(petal_size)
        print(line)