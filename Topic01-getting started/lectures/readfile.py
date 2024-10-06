# read in a simple file
# Author: Finbar Dennehy

FILENAME = "data.txt"
DATADIR = "../datafiles/"

print (DATADIR + FILENAME)
with open(DATADIR + FILENAME, "rt") as fp:
    total = 0
    for line in fp:
        total += int(line) # sum each line as integers
        print (f"{line} is size {len(line)}") # shows count of additional (new line) character at end of each line. end ="" can be used to remove new line spaces.
    print("") # ensures next print out is on new line
    print (f"total is {total}")