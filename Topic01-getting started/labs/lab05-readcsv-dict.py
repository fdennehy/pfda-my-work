# The CVS file could of course have been read in as a Dictionary object Using DictReader()
# Author: Finbar Dennehy

import csv

FILENAME = "data.csv"

with open (FILENAME, "rt") as fp: # fp file pointer
    reader = csv.DictReader(fp, delimiter="," , quoting = csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
            total += line['age']
            count += 1
    print (f"The average age is {total/count}")