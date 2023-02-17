import pandas as pd
import tkinter as tk
from tkinter import ttk

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("ParamTbl.csv")

print (df)

# Create a Tkinter dialog frame
my_w = tk.Tk()
my_w.geometry("800x600")
my_w.title("Data Table")

# Create a Treeview widget to display the data
tree = ttk.Treeview(my_w,selectmode='browse',show='headings',height=10)
# tree['show'] = 'headings'
# tree.column("#0", width = 0, stretch = "no") 

tree['columns']=df.columns.values.tolist()
#               Gr,     Idx, Name,     Addr, Val, Def, Min, Max, Div,     Unit
colWid = [      50,      50,  500,       50,  50,  50,  50,  50,  50,       50]
colAln = ["center","center",  "w", "center", "e", "e", "e", "e", "e", "center"]

# sb = ttk.Scrollbar(my_w, orient="vertical", command=tree.yview)
# sb.grid(row=1,column=1,sticky="NS",pady=5)
# tree.configure(yscrollcommand=sb.set)

for idx, i in enumerate(df.columns.values.tolist(), start=0):
#    print(idx,i)    
    tree.column(i,width=colWid[idx],anchor=colAln[idx])
    tree.heading(idx, text=i)

for index, row in df.iterrows():
    tree.insert("", 'end', text=index, values=list(row))
# print(df.iterrows())
style = ttk.Style(my_w) 
style.configure('Treeview', 
                rowheight=25)

tree.pack()

my_w.mainloop()

