# Write a program to read in the data and output each line as a list. 
# Author: Finbar Dennehy

import csv

FILENAME = "data.csv"

with open (FILENAME, "rt") as fp: # fp file pointer
    reader = csv.reader(fp, delimiter="," , quoting = csv.QUOTE_ALL) # assumes everything will be quoted
    for line in reader:
            print (line)

# Note what is printed. What data type are these?
# lists []