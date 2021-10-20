import tkinter as tk
import tkinter as ttk 
import sqlite3  
from tkinter import *
from tkinter.ttk import *
#from classFrame3 import *
from classFrame5 import *
from classQueryFunctions import *

class Frame4:
    def __init__(self, root):
        self.x = None

        #global frame3
        #frame3 = Frame3(root)
        global frame5
        frame5 = Frame5(root)
        

    def frame_4(self, root, treeviews, BCOLOR, DATABASE):
        self.treeviews = treeviews

        global queryFunctions
        queryFunctions = QueryFunctions(root, DATABASE, treeviews)
        
        global frame4
        frame4 = LabelFrame(root, text="Query Database By", padx=5, pady=5)
        frame4.grid(row=0, column=1, padx=10, pady=0, sticky=EW)
        treeviews.autoSize(root, 0, 1)

        global modelBox
        modelBox = Entry(frame4, width=27)
        modelBox.bind("<Return>", lambda event, arg=DATABASE: self.event_modelQuery(event, arg))
        #supplyDD.bind("<Return>", lambda event, arg=DATABASE: self.event_supplyQuery(event, arg))
        modelBox.bind("<Tab>", lambda event, arg=None: self.focusModelB(event))
        modelBox.grid(row=1, column=4, padx=10, pady=(15, 0), sticky=W)
        treeviews.autoSize(frame4, 0, 3)
        global descriptionBox
        descriptionBox = Entry(frame4, width=27)
        descriptionBox.bind("<Return>", lambda event, arg=DATABASE: self.event_descriptionQuery(event, arg))
        descriptionBox.bind("<Tab>", lambda event, arg=None: self.focusModelB(event))
        descriptionBox.grid(row=3, column=4, padx=10, pady=(0, 0), sticky=W)
        treeviews.autoSize(frame4, 3, 3)

        global valueLessBox
        valueLessBox = Entry(frame4, width=27)
        valueLessBox.bind("<Return>", lambda event, arg=DATABASE: self.event_valueLessQuery(event, arg))
        valueLessBox.grid(row=5, column=1, sticky=W)
        treeviews.autoSize(frame4, 5, 1)

        global quantityLessBox
        quantityLessBox = Entry(frame4, width=27)
        quantityLessBox.bind("<Return>", lambda event, arg=DATABASE: self.event_quantityLessQuery(event, arg))
        quantityLessBox.grid(row=6, column=1, sticky=W)
        treeviews.autoSize(frame4, 6, 1)

        global totalLessBox
        totalLessBox = Entry(frame4, width=27)
        totalLessBox.bind("<Return>", lambda event, arg=DATABASE: self.event_totalLessQuery(event, arg))
        totalLessBox.grid(row=7, column=1, pady=(0, 10), sticky=W)
        treeviews.autoSize(frame4, 7, 1)

        global valueGreaterBox
        valueGreaterBox = Entry(frame4, width=27)
        valueGreaterBox.bind("<Return>", lambda event, arg=DATABASE: self.event_valueGreaterQuery(event, arg))
        valueGreaterBox.grid(row=5, column=4, sticky=W)
        treeviews.autoSize(frame4, 5, 4)

        global quantityGreaterBox
        quantityGreaterBox = Entry(frame4, width=27)
        quantityGreaterBox.bind("<Return>", lambda event, arg=DATABASE: self.event_quantityGreaterQuery(event, arg))
        quantityGreaterBox.grid(row=6, column=4, sticky=W)
        treeviews.autoSize(frame4, 6, 4)

        global totalGreaterBox
        totalGreaterBox = Entry(frame4, width=27)
        totalGreaterBox.bind("<Return>", lambda event, arg=DATABASE: self.event_totalGreaterQuery(event, arg))
        totalGreaterBox.grid(row=7, column=4, pady=(0, 10), sticky=W)
        treeviews.autoSize(frame4, 7, 4)    

        global supplyB
        supplyB = Button(frame4, text="Search By Supplier", command=lambda: self.supplyQuery(DATABASE), bg=BCOLOR, fg='white')
        supplyB.bind("<Return>", lambda event, arg=DATABASE: self.event_supplyQuery(event, arg))
        supplyB.grid(row=2, column=0, columnspan=2, padx=5, pady=(5, 15), ipadx=83, sticky=EW)
        treeviews.autoSize(frame4, 2, 0)
        global manB
        manB = Button(frame4, text="Search By Manufacturer", command=lambda: self.manufactureQuery(DATABASE), bg=BCOLOR, fg='white')
        manB.bind("<Return>", lambda event, arg=DATABASE: self.event_manufactureQuery(event, arg))
        manB.grid(row=4, column=0, columnspan=2, padx=10, pady=(5, 25), ipadx=68, sticky=EW)
        treeviews.autoSize(frame4, 4, 0)
        global modelB
        modelB = Button(frame4, text="Search by Model", command=lambda: self.modelQuery(DATABASE), bg=BCOLOR, fg='white')
        modelB.bind("<Return>", lambda event, arg=DATABASE: self.event_modelQuery(event, arg))
        modelB.grid(row=6, column=0, columnspan=2, padx=10, pady=(5, 5), ipadx=87, sticky=EW)
        treeviews.autoSize(frame4, 6, 0)
        modelB.grid(row=2, column=3, columnspan=2, padx=10, pady=(5, 15), ipadx=87, sticky=EW) 
        treeviews.autoSize(frame4, 2, 3)
        global descriptB
        descriptB = Button(frame4, text="Search by Description", command=lambda: self.descriptionQuery(DATABASE), bg=BCOLOR, fg='white')
        descriptB.bind("<Return>", lambda event, arg=DATABASE: self.event_descriptionQuery(event, arg))
        descriptB.grid(row=8, column=0, columnspan=2, padx=10, pady=(5, 7), ipadx=74, sticky=EW)
        treeviews.autoSize(frame4, 8, 0)
        descriptB.grid(row=4, column=3, columnspan=2, padx=10, pady=(5, 25), ipadx=74, sticky=EW)
        treeviews.autoSize(frame4, 4, 3)

        supplierQuery = Label(frame4, text="Choose Supplier")
        supplierQuery.grid(row=1, column=0, pady=(15, 0), sticky=E)
        treeviews.autoSize(frame4, 1, 0)    

        manufactureLabel = Label(frame4, text="Choose Manufacturer")
        manufactureLabel.grid(row=3, column=0, sticky=E)
        treeviews.autoSize(frame4, 3, 0)
        
        modelLabel = Label(frame4, text="Model")
        modelLabel.grid(row=1, column=3, pady=(15, 0), sticky=E)
        treeviews.autoSize(frame4, 1, 3)
        
        descriptionLabel = Label(frame4, text="Description")
        descriptionLabel.grid(row=3, column=3, pady=(0, 0), sticky=E)
        treeviews.autoSize(frame4, 3, 3)

        valueLess = Label(frame4, text="Value <= ")
        valueLess.grid(row=5, column=0, sticky=E)
        treeviews.autoSize(frame4, 5, 0)

        quantityLess = Label(frame4, text="Quantity <= ")
        quantityLess.grid(row=6, column=0, sticky=E)
        treeviews.autoSize(frame4, 6, 0)

        totalLess = Label(frame4, text="Total <= ")
        totalLess.grid(row=7, column=0, pady=(0, 10), sticky=E)
        treeviews.autoSize(frame4, 7, 0)

        valueGreater = Label(frame4, text="Value >= ")
        valueGreater.grid(row=5, column=3, sticky=E)
        treeviews.autoSize(frame4, 5, 3)

        quantityGreater = Label(frame4, text="Quantity >= ")
        quantityGreater.grid(row=6, column=3, sticky=E)
        treeviews.autoSize(frame4, 6, 3)

        totalGreater = Label(frame4, text="Total >= ")
        totalGreater.grid(row=7, column=3, pady=(0, 10), sticky=E)
        treeviews.autoSize(frame4, 7, 3)

        self.Combobox(treeviews, DATABASE)

    def getself(self):
        return self

    def focusSupplyB(self):
        supplyB.tk_focusNext().tkraise()
        return("break")

    def focusManB(self):
        manB.tk_focusNext().tkraise()
        return("break")

    def focusModelB(self, event):
        modelB.tk_focusNext().tkraise()
        return("break")

    def focusDescriptB(self):
        descriptB.tk_focusNext().tkraise()
        return("break")

    def getClicked1(self):
        return clicked1

    def getClicked(self):
        return clicked


    def Combobox(self, treeviews, DATABASE):
        self.supplierDD(treeviews, DATABASE)
        self.manufacturerDD(treeviews, DATABASE)

    def manufacturerDD(self, treeviews, DATABASE):    
        # Combo Box for Manufacturer
        global clicked
        clicked = StringVar()
        global manDD
        manDD = ttk.Combobox(frame4, width=23, textvariable=clicked)
        manDD.bind("<Return>", lambda event, arg=DATABASE: self.event_manufactureQuery(event, arg))
        manDD.bind("<Tab>", lambda event, arg=None: self.focusManDD(event))
        manDD.grid(row=3, column=1, padx=(0, 0))
        manList = self.getManList(DATABASE)
        manDD['values'] = manList

        #x = frame3.getFrame3()
        #treeviews.autoSize(x, 3, 1)

    def getManufacturerDD(self):
        return manDD

    def focusManDD(self, event):
        manDD.tk_focusNext().tkraise()
        return("break")

    def getManList(self, DATABASE):
        dbase = sqlite3.connect(DATABASE)
        c1 = dbase.cursor()
        c1.execute("SELECT Manufacturer FROM allMaterial")
        records = c1.fetchall()
        manList = []
        dbaseList = records
        for record in dbaseList:
            if record not in manList:
                manList.append(record)
        return manList

    def clearManDD(self):
        manDD.set('')

    def supplierDD(self, treeviews, DATABASE):
        # ComboBox for Supplier
        global clicked1
        clicked1 = StringVar()
        global supplyDD
        supplyDD = ttk.Combobox(frame4, width=23, textvariable=clicked1)
        supplyDD.bind("<Return>", lambda event, arg=DATABASE: self.event_supplyQuery(event, arg))
        supplyDD.bind("<Tab>", lambda event, arg=None: self.focusSupplyDD(event))
        supplyDD.grid(row=1, column=1, padx=10, pady=(15, 0))
        global supplyList
        supplyList = self.getSupplyList(DATABASE)
        supplyDD['values'] = supplyList

        treeviews.autoSize(frame4, 1, 1)

    def getSupplierDD(self):
        return supplyDD

    def clearSupplierDD(self):
        supplyDD.set("")

    def focusSupplyDD(self, event):
        supplyDD.tk_focusNext().tkraise()
        return("break")

    def getSupplyList(self, DATABASE):
        dbase = sqlite3.connect(DATABASE)
        c1 = dbase.cursor()
        c1.execute("SELECT Supplier FROM allMaterial")
        records = c1.fetchall()
        supplyList = []
        dbaseList = records
        for record in dbaseList:
            if record not in supplyList:
                supplyList.append(record)
        return supplyList

    def clearModelBox(self):
        modelBox.delete(0, END)

    def getModelBox(self):
        return modelBox.get()

    def clearDescriptionBox(self):
        descriptionBox.delete(0, END)

    def getDescriptionBox(self):
        return descriptionBox.get()

    def event_modelQuery(self, event, DATABASE):
        self.modelQuery(DATABASE)
    
    def modelQuery(self, DATABASE):
        w = self.getModelBox()
        queryFunctions.modelQuery(DATABASE, w)

    def event_descriptionQuery(self, event, DATABASE):
        self.descriptionQuery(DATABASE)

    def descriptionQuery(self, DATABASE):
        w = self.getDescriptionBox() 
        queryFunctions.descriptionQuery(DATABASE, w)  

    def event_valueLessQuery(self, event, DATABASE):  
        w = self.getValueLessBox()
        queryFunctions.event_valueLessQuery(DATABASE, w)  
        frame5.subTotal(self.treeviews)

    def event_quantityLessQuery(self, event, DATABASE):
        w = self.getQuantityLessBox()  
        queryFunctions.event_quantityLessQuery(DATABASE, w) 
        frame5.subTotal(self.treeviews)

    def event_totalLessQuery(self, event, DATABASE):
        w = self.getTotalLessBox()  
        queryFunctions.event_totalLessQuery(DATABASE, w) 
        frame5.subTotal(self.treeviews)

    def event_valueGreaterQuery(self, event, DATABASE):
        w = self.getValueGreaterBox()
        queryFunctions.event_valueGreaterQuery(DATABASE, w)
        frame5.subTotal(self.treeviews)

    def event_quantityGreaterQuery(self, event, DATABASE):
        w = self.getQuantityGreaterBox()
        queryFunctions.event_quantityGreaterQuery(DATABASE, w)
        frame5.subTotal(self.treeviews)

    def event_totalGreaterQuery(self, event, DATABASE):
        w = self.getTotalGreaterBox()
        queryFunctions.event_totalGreaterQuery(DATABASE, w)
        frame5.subTotal(self.treeviews)

    def event_supplyQuery(self, event, DATABASE):
        self.supplyQuery(DATABASE)

    def supplyQuery(self, DATABASE):
        w = self.getClicked1()
        w = str(w.get())
        queryFunctions.supplyQuery(DATABASE, w)
        frame5.subTotal(self.treeviews)

    def event_manufactureQuery(self, event, DATABASE):
        self.manufactureQuery(DATABASE)

    def manufactureQuery(self, DATABASE):
        w = self.getClicked()
        w = str(w.get())
        queryFunctions.manufactureQuery(DATABASE, w)
        frame5.subTotal(self.treeviews)

    def getValueLessBox(self):
        return valueLessBox.get()
    def clearValueLessBox(self):
        valueLessBox.delete(0, END)

    def getQuantityLessBox(self):
        return quantityLessBox.get()
    def clearQuantityLessBox(self):
        quantityLessBox.delete(0, END)

    def getTotalLessBox(self):
        return totalLessBox.get()
    def clearTotalLessBox(self):
        totalLessBox.delete(0, END)

    def getValueGreaterBox(self):
        return valueGreaterBox.get()
    def clearValueGreaterBox(self):
        valueGreaterBox.delete(0, END)

    def getQuantityGreaterBox(self):
        return quantityGreaterBox.get()
    def clearQuantityGreaterBox(self):
        quantityGreaterBox.delete(0, END)

    def getTotalGreaterBox(self):
        return totalGreaterBox.get()
    def clearTotalGreaterBox(self):
        totalGreaterBox.delete(0, END)