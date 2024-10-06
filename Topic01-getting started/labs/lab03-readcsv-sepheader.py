# Modify the program to deal with the header line separately
# Author: Finbar Dennehy

import csv

FILENAME = "data.csv"

with open (FILENAME, "rt") as fp: # fp file pointer
    reader = csv.reader(fp, delimiter="," , quoting = csv.QUOTE_ALL) # assumes everything will be quoted
    linecount = 0 # to address header for operations
    for line in reader:
        if not linecount: # i.e. linecount = 0, linecount is false. This statement is true, so this is the first row, which is the header. 
        #Could also use 'if not linecount >0: or 'if linecount ==0'
            print (f"{line}\n---------------------")
        else: # all subsequent rows
            print (line)
        linecount += 1 # move onto next line