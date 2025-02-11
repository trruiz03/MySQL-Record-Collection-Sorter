#import prettyTable library
from prettytable import PrettyTable
from prettytable import DOUBLE_BORDER

#Specify Colum names and intitialize 
myTable = PrettyTable()
myTable.set_style(DOUBLE_BORDER)

myTable.field_names = ["Artist", "Ablum", "Version", "Value"]
myTable.header = True

#add rows
myTable.add_row(["ACDC", "Fly on The wall", "Standard", 17.99])

myTable.sortby= "Artist"
print(myTable)


