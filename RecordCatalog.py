#import tabulate libraries
from tabulate import tabulate

#create data
data = [
    ["ACDC", "For those about to Rock", "Standard", 7.00 ],
    ["ACDC", "Back in Black", "Standard", 17.99],
    ["ACDC", "Flick of the Switch", "Standard", 5.00],
    ["ACDC", "Fly on The wall", "Standard", 17.99]
]

#define header names
col_names = ["Artist", "Album", "Version",  "Value"]

#sort by artist name and album
data.sort()
#display table
print(tabulate(data, headers = col_names, tablefmt = "fancy_grid"))
