#  Modify the program to calculate the average age, there are a few ways to solve this;
# a) Convert the string that is read into an integer
# b) Use the quote parameter to read in the numbers as floats
# Author: Finbar Dennehy

# METHOD A

import csv

FILENAME = "data.csv"

with open (FILENAME, "rt") as fp: # fp file pointer
    reader = csv.reader(fp, delimiter="," , quoting = csv.QUOTE_ALL) # assumes everything will be quoted
    linecount = 0 # to address header for operations
    total = 0
    for line in reader:
        if not linecount: # i.e. linecount = 0, linecount is false. This statement is true, so this is the first row, which is the header. 
        #Could also use 'if not linecount >0: or 'if linecount ==0'
            pass
        else: # all subsequent rows
            total += int(line[1])
        linecount += 1 # move onto next line
    print (f"The average age is {total/(linecount-1)}")

# METHOD B

import csv

FILENAME = "data.csv"

with open (FILENAME, "rt") as fp: # fp file pointer
    reader = csv.reader(fp, delimiter="," , quoting = csv.QUOTE_NONNUMERIC)
    linecount = 0 # to address header for operations
    total = 0
    for line in reader:
        if not linecount: # i.e. linecount = 0, linecount is false. This statement is true, so this is the first row, which is the header. 
        #Could also use 'if not linecount >0: or 'if linecount ==0'
            pass
        else: # all subsequent rows
            total += line[1]
        linecount += 1 # move onto next line
    print (f"The average age is {total/(linecount-1)}")