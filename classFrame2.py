import tkinter as tk    
from tkinter import * 
from classFrame5 import *
from classQueryFunctions import *
from classTreeviews import *

class Frame2():
    def __init__(self, root):
        self.root = root
        global frame5
        frame5 = Frame5(root)
        
    def frame_2(self, root, BCOLOR, DATABASE, treeviews):
        self.treeviews = treeviews
        global queryFunctions
        queryFunctions = QueryFunctions(root, DATABASE, treeviews)
        
        frame2 = LabelFrame(root, text='Arrange Database By:', fg=BCOLOR, padx = 5, pady=5)
        frame2.grid(row=0, column=3, padx=10, pady=0, sticky=EW)
        treeviews.autoSize(root, 0, 3)
        groupSupplierB = Button(frame2, text="Supplier", command=lambda: self.groupSupplierQuery(DATABASE), bg=BCOLOR, fg='white')
        groupSupplierB.bind("<Return>", lambda event, arg=DATABASE: self.event_groupSupplierQuery(event, arg))
        groupSupplierB.grid(row=1, column=0, columnspan=2, padx=20, pady=(7, 3), ipadx=15, sticky=EW)
        treeviews.autoSize(frame2, 1, 0)
        groupManB = Button(frame2, text="Manufacturer", command=lambda: self.groupManufacturerQuery(DATABASE), bg=BCOLOR, fg='white')
        groupManB.bind("<Return>", lambda event, arg=DATABASE: self.event_groupManufacturerQuery(event, arg))
        groupManB.grid(row=2, column=0, columnspan=2, padx=20, pady=3, ipadx=0, sticky=EW)
        treeviews.autoSize(frame2, 2, 0)
        groupModelB = Button(frame2, text="Model", command=lambda: self.groupModelQuery(DATABASE), bg=BCOLOR, fg='white')
        groupModelB.bind("<Return>", lambda event, arg=DATABASE: self.event_groupModelQuery(event, arg))
        groupModelB.grid(row=3, column=0, columnspan=2, padx=20, pady=3, ipadx=19, sticky=EW)
        treeviews.autoSize(frame2, 3, 0)
        groupDescB = Button(frame2, text="Description", command=lambda: self.groupDescriptionQuery(DATABASE), bg=BCOLOR, fg='white')
        groupDescB.bind("<Return>", lambda event, arg=DATABASE: self.event_groupDescriptionQuery(event, arg))
        groupDescB.grid(row=4, column=0, columnspan=2, padx=20, pady=3, ipadx=6, sticky=EW)
        treeviews.autoSize(frame2, 4, 0)
        groupValueB = Button(frame2, text="Value", command=lambda: self.groupValueQuery(DATABASE), bg=BCOLOR, fg='white')
        groupValueB.bind("<Return>", lambda event, arg=DATABASE: self.event_groupValueQuery(event, arg))
        groupValueB.grid(row=5, column=0, columnspan=2, padx=20, pady=3, ipadx=21, sticky=EW)
        treeviews.autoSize(frame2, 5, 0)
        groupQuantityB = Button(frame2, text="Quantity", command=lambda: self.groupQuantityQuery(DATABASE), bg=BCOLOR, fg='white')
        groupQuantityB.bind("<Return>", lambda event, arg=DATABASE: self.event_groupQuantityQuery(event, arg))
        groupQuantityB.grid(row=6, column=0, columnspan=2, padx=20, pady=3, ipadx=13, sticky=EW)
        treeviews.autoSize(frame2, 6, 0)
        groupTotalB = Button(frame2, text="TotalValue", command=lambda: self.groupTotalQuery(DATABASE), bg=BCOLOR, fg='white')
        groupTotalB.bind("<Return>", lambda event, arg=DATABASE: self.event_groupTotalQuery(event, arg))
        groupTotalB.grid(row=7, column=0, columnspan=2, padx=20, pady=(3, 6), ipadx=8, sticky=EW)
        treeviews.autoSize(frame2, 7, 0)

    def event_groupSupplierQuery(self, DATABASE):
        self.groupSupplierQuery(DATABASE)

    def groupSupplierQuery(self, DATABASE):
        queryFunctions.groupSupplierQuery(DATABASE)
        frame5.subTotal(self.treeviews)

    def event_groupManufacturerQuery(self, DATABASE):
        self.groupManufacturerQuery(DATABASE)

    # This function orders the database using the Manufacturer column ascending from lowest value to highest value
    def groupManufacturerQuery(self, DATABASE):
        queryFunctions.groupManufacturerQuery(DATABASE)
        frame5.subTotal(self.treeviews)

    def event_groupModelQuery(self, DATABASE):
        self.groupModelQuery(DATABASE)

    def groupModelQuery(self, DATABASE):
        queryFunctions.groupModelQuery(DATABASE)
        frame5.subTotal(self.treeviews)

    def event_groupDescriptionQuery(self, DATABASE):
        self.groupModelQuery(DATABASE)

    def groupDescriptionQuery(self, DATABASE):
        queryFunctions.groupDescriptionQuery(DATABASE)
        frame5.subTotal(self.treeviews)  

    def event_groupValueQuery(self, DATABASE):
        self.groupValueQuery(DATABASE)

    def groupValueQuery(self, DATABASE):
        queryFunctions.groupValueQuery(DATABASE)
        frame5.subTotal(self.treeviews) 

    def event_groupQuantityQuery(self, DATABASE):
        self.groupQuantityQuery(DATABASE)

    def groupQuantityQuery(self, DATABASE):
        queryFunctions.groupQuantityQuery(DATABASE)
        frame5.subTotal(self.treeviews) 

    def event_groupTotalQuery(self, DATABASE):
        self.groupTotalQuery(DATABASE)

    def groupTotalQuery(self, DATABASE):
        queryFunctions.groupTotalQuery(DATABASE)
        frame5.subTotal(self.treeviews) 