import sqlite3
from tkinter import *
from tkinter import ttk
import pandas as pd


class Treeview:
    def __init__(self, frame3):
        self.frame3 = frame3

    def treeview1(self, DATABASE):

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background="D7BFDC", foreground="black", rowheight=25, fieldbackground="D7BFDC")
        style.map("Treeview", background=[('selected', '#347083')])

        treescrolly = Scrollbar(self.frame3, orient=VERTICAL)
        treescrollx = Scrollbar(self.frame3)
        treescrolly.pack(side='right', fill='y')

        global tv1
        tv1 = ttk.Treeview(self.frame3, yscrollcommand=treescrolly.set, height=26)
        tv1.bind('<Double-1>', lambda event, arg=DATABASE: self.doubleClick(event, arg))
        tv1.pack(fill="both")
        treescrolly.configure(command=tv1.yview)
        tv1['columns'] = ("UniqueID", "Supplier", "Manufacturer", "Model", "Description", "Value", "Quantity", "TotalValue")
        tv1.column("#0", width=0, stretch=NO)
        tv1.column("UniqueID", anchor=CENTER, width=50)
        tv1.column("Supplier", anchor=CENTER, width=120)
        tv1.column("Manufacturer", anchor=CENTER, width=140)
        tv1.column("Model", anchor=CENTER, width=160)
        tv1.column("Description", anchor=W, width=250)
        tv1.column("Value", anchor=CENTER, width=80)
        tv1.column("Quantity", anchor=CENTER, width=50)
        tv1.column("TotalValue", anchor=CENTER, width=100)


        tv1.heading("#0", text="", anchor=W)
        tv1.heading("UniqueID", text="UniqeID", anchor=CENTER)
        tv1.heading("Supplier", text="Supplier", anchor=CENTER, command=self.headerClick)
        tv1.heading("Manufacturer", text="Manufacturer", anchor=CENTER, command=self.headerClick)
        tv1.heading("Model", text="Model", anchor=CENTER, command=self.headerClick)
        tv1.heading("Description", text="Description", anchor=CENTER, command=self.headerClick)
        tv1.heading("Value", text="Value", anchor=CENTER, command=self.headerClick)
        tv1.heading("Quantity", text="Quantity", anchor=CENTER, command=self.headerClick)
        tv1.heading("TotalValue", text="TotalValue", anchor=CENTER, command=self.headerClick)

        tv1.tag_configure('oddrow', background="white")
        tv1.tag_configure('evenrow', background="lightblue")

    def doubleClick(self, event, DATABASE):
        global doubleclick
        doubleclick = True

    def getDoubleClick(self):
        return doubleclick

    #def doubleClick(self, event, DATABASE):
        #entryBoxes.clearSelectBox()
        #row = tv1.selection()[0]
        #numberID = tv1.item(row)['values'][0]
        #entryBoxes.setSelectBox(numberID)
        #databaseFunctions.edit(self.DATABASE)

    def setTv1(self, x):
        tv1 = set(self.tv1)

    def getTv1(self, tv1):
        return tv1.get()

    def getRow(self):
        return self.tv1.selection()[0]

    def getNumberID(self):
        return tv1.item(self.getRow)['values'][0]

    def headerClick(self):
        data = [tv1.item(item) ['values'] for item in tv1.get_children()]
        df = pd.DataFrame(data)
        records = df.loc[::-1]
        self.rearrangeTv1(records)

    def event_arrangeBySupp(self, event):
        self.arrangeBySupp()

    def arrangeBySupp(self):
        data = [tv1.item(item) ['values'] for item in tv1.get_children()]
        df = pd.DataFrame(data)
        records = df.sort_values(by=1)
        self.rearrangeTv1(records)

    def event_arrangeByMan(self, event):
        self.arrangeByMan()

    def arrangeByMan(self):
        data = [tv1.item(item) ['values'] for item in tv1.get_children()]
        df = pd.DataFrame(data)
        records = df.sort_values(by=2)
        self.rearrangeTv1(records)

    def event_arrangeByModel(self, event):
        self.arrangeByModel()
        
    def arrangeByModel(self):
        data = [tv1.item(item) ['values'] for item in tv1.get_children()]
        df = pd.DataFrame(data)
        df[3] = df[3].astype(str)
        records = df.sort_values(by=3)
        self.rearrangeTv1(records)

    def event_arrangeByDesc(self, event):
        self.arrangeByDesc()

    def arrangeByDesc(self):
        data = [tv1.item(item) ['values'] for item in tv1.get_children()]
        df = pd.DataFrame(data)
        records = df.sort_values(by=4)
        self.rearrangeTv1(records)

    def event_arrangeByValue(self, event):
        self.arrangeByValue()

    def arrangeByValue(self):
        data = [tv1.item(item) ['values'] for item in tv1.get_children()]
        df = pd.DataFrame(data)
        df[5] = df[5].str.replace('$','').astype(float)
        records = df.sort_values(5)
        self.rearrangeTv1_2(records)

    def event_arrangeByQuantity(self, event):
        self.arrangeByQuantity()

    def arrangeByQuantity(self):
        data = [tv1.item(item) ['values'] for item in tv1.get_children()]
        df = pd.DataFrame(data)
        records = df.sort_values(6)
        self.rearrangeTv1(records)

    def event_arrangeByTotal(self, event):
        self.arrangeByTotal()

    def arrangeByTotal(self):
        data = [tv1.item(item) ['values'] for item in tv1.get_children()]
        df = pd.DataFrame(data)
        df[7] = df[7].str.replace('$','').astype(float)
        pd.options.display.float_format = "{:, .2}".format
        records = df.sort_values(7)
        self.rearrangeTv1_1(records)

    def tv1Item(self):
        return [tv1.item(item) ['values'] for item in tv1.get_children()]
    # Function iterates through records from database, decided by 'phrase', and displays in Treeview
    def query(self, phrase, DATABASE):
        self.tv1Item()
        dbase = sqlite3.connect(DATABASE)
        c1 = dbase.cursor()
        self.clearTv1()
        c1.execute(phrase)
        records = c1.fetchall()
        count = 0
        for record in records:
            if count%2==0:
                tv1.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], str(record[3]), record[4], "$" + str("{:.2f}".format(record[5])), record[6], "$" + str("{:.2f}".format(record[5] * record[6]))), tags=('evenrow', ))
            else:
                tv1.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], str(record[3]), record[4], "$" + str("{:.2f}".format(record[5])), record[6], "$" + str("{:.2f}".format(record[5] * record[6]))), tags=('oddrow', ))
            count+=1
        dbase.commit()
        dbase.close()

    # Clears the Treeview
    def clearTv1(self):
        recordLimit = ""
        for i in tv1.get_children():
            tv1.delete(i)

    def rearrangeTv1(self, records):
        self.clearTv1()
        rows = records.to_numpy().tolist()
        count = 0
        for row in rows:
            if count%2==0:
                tv1.insert("", "end", values=row, tags=('evenrow', ))
            else:
                tv1.insert("", "end", values=row, tags=('oddrow', ))
            count+=1

    def rearrangeTv1_1(self, records):
        rows = records.to_numpy().tolist()
        for row in rows:
            row[7] = "$" + str("{:.2f}".format(row[7]))
        self.clearTv1()
        count = 0
        for row in rows:
            if count%2==0:
                tv1.insert("", "end", values=row, tags=('evenrow', ))
            else:
                tv1.insert("", "end", values=row, tags=('oddrow', ))
            count+=1

    def rearrangeTv1_2(self, records):
        rows = records.to_numpy().tolist()
        for row in rows:
            row[5] = "$" + str("{:.2f}".format(row[5]))
        self.clearTv1()
        count = 0
        for row in rows:
            if count%2==0:
                tv1.insert("", "end", values=row, tags=('evenrow', ))
            else:
                tv1.insert("", "end", values=row, tags=('oddrow', ))
            count+=1

    def autoSize(self, root, row, column):
        Grid.rowconfigure(root, row, weight=1)
        Grid.columnconfigure(root, column, weight=1) 