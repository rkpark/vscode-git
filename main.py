import csv

class Param():
    Name : str
    Addr : int
    Val  : int
    Def  : int
    Min  : int
    Max  : int
    Div  : int
    Unit : str

"""
fields = ['Name','Branch','Year','CGPA']

rows = [ [ 'Nikhil','COE','2','9.0'],
        [ 'Sanchit','COE','2','9.1'],
        [ 'Aditya','IT','2','9.3'],
        [ 'Sagar','SE','1','9.5'],
        [ 'Prateek','MCE','3','7.8'],
        [ 'Sahil','EP','2','9.1']]

filename = "test.csv"

with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

# initializing the titles and rows list
"""

fields = []
rows = []
# Params = [Param() for i in range(100)]
Params = [Param() for i in range(100)]

filename = "ParamTbl.csv"
# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
     
    # extracting field names through first row
    fields = next(csvreader)
    #print(fields)
    # extracting each data row one by one
    for row in csvreader:
        print(row,csvreader.line_num)
        rows.append(row)        
        Params[csvreader.line_num-2].Name = row[0]
        Params[csvreader.line_num-2].Addr = int(row[1],base=16)
        Params[csvreader.line_num-2].Val = int(row[2])
        Params[csvreader.line_num-2].Def = int(row[3])
        Params[csvreader.line_num-2].Min = int(row[4])
        Params[csvreader.line_num-2].Max = int(row[5])
        Params[csvreader.line_num-2].Div = int(row[6])
        Params[csvreader.line_num-2].Unit= row[7]
        print(Params[csvreader.line_num-2].Name,hex(Params[csvreader.line_num-2].Addr))

    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))
 
# for i in range(2,4):
#     print(i)
#     print(Params[i].Name,hex(Params[i].Addr))

print(len(Params))
print("line_Num : ",csvreader.line_num)

for i in range(0,csvreader.line_num-1):
    print(Params[i].Name,hex(Params[i].Addr))



