# Simple program to read a csv file
# Author: Finbar Dennehy

import csv

FILENAME = "data.csv"
DATADIR = "../datafiles/"

with open (DATADIR + FILENAME, "rt") as fp: # fp file pointer
    reader = csv.reader(fp, delimiter="," , quoting = csv.QUOTE_ALL) # assumes everything will be quoted
    linecount = 0 # to address header for operations
    total = 0
    for line in reader:
        if not linecount: # i.e. linecount = 0, linecount is false. This statement is true, so this is the first row, which is the header. 
        #Could also use 'if not linecount >0: or 'if linecount ==0'
            print (f"{line}\n---------------------")
        else: # all subsequent rows
            total += int(line[0])
            print (line)
        linecount += 1 # move onto next line