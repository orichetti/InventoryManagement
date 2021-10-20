import tkinter as tk    
from tkinter import *
from classFrame8 import *

class Frame6():
    def __init__(self):
        self.x = None
        global frame8
        frame8 = Frame8()

    def frame_6(self, root, treeviews, BCOLOR):
        frame6 = LabelFrame(root, text='Arrange View By:', fg=BCOLOR, padx = 5, pady=5)
        frame6.grid(row=0, column=4, padx=10, pady=0, sticky=EW)
        treeviews.autoSize(frame8.getFrame8(), 0, 1)
        treeviews.autoSize(root, 0, 4)

        BCOLOR = "lightblue"
        groupSupplierB = Button(frame6, text="Supplier", command=lambda: treeviews.arrangeBySupp(), bg=BCOLOR, fg='black')
        groupSupplierB.bind("<Return>", treeviews.event_arrangeBySupp)
        groupSupplierB.grid(row=1, column=0, columnspan=2, padx=20, pady=(7, 3), ipadx=15, sticky=EW)
        treeviews.autoSize(frame6, 1, 0)
        groupManB = Button(frame6, text="Manufacturer", command=lambda: treeviews.arrangeByMan(), bg=BCOLOR, fg='black')
        groupManB.bind("<Return>", treeviews.event_arrangeByMan)
        groupManB.grid(row=2, column=0, columnspan=2, padx=20, pady=3, ipadx=0, sticky=EW)
        treeviews.autoSize(frame6, 2, 0)
        groupModelB = Button(frame6, text="Model", command=lambda: treeviews.arrangeByModel(), bg=BCOLOR, fg='black')
        groupModelB.bind("<Return>", treeviews.event_arrangeByModel)
        groupModelB.grid(row=3, column=0, columnspan=2, padx=20, pady=3, ipadx=19, sticky=EW)
        treeviews.autoSize(frame6, 2, 0)
        groupDescB = Button(frame6, text="Description", command=lambda: treeviews.arrangeByDesc(), bg=BCOLOR, fg='black')
        groupDescB.bind("<Return>", treeviews.event_arrangeByDesc)
        groupDescB.grid(row=4, column=0, columnspan=2, padx=20, pady=3, ipadx=6, sticky=EW)
        treeviews.autoSize(frame6, 4, 0)
        groupValueB = Button(frame6, text="Value", command=lambda: treeviews.arrangeByValue(), bg=BCOLOR, fg='black')
        groupValueB.bind("<Return>", treeviews.event_arrangeByValue)
        groupValueB.grid(row=5, column=0, columnspan=2, padx=20, pady=3, ipadx=21, sticky=EW)
        treeviews.autoSize(frame6, 5, 0)
        groupQuantityB = Button(frame6, text="Quantity", command=lambda: treeviews.arrangeByQuantity(), bg=BCOLOR, fg='black')
        groupQuantityB.bind("<Return>", treeviews.event_arrangeByQuantity)
        groupQuantityB.grid(row=6, column=0, columnspan=2, padx=20, pady=3, ipadx=13, sticky=EW)
        treeviews.autoSize(frame6, 6, 0)
        groupTotalB = Button(frame6, text="TotalValue", command=lambda: treeviews.arrangeByTotal(), bg=BCOLOR, fg='black')
        groupTotalB.bind("<Return>", treeviews.event_arrangeByTotal)
        groupTotalB.grid(row=7, column=0, columnspan=2, padx=20, pady=(3, 7), ipadx=8, sticky=EW)
        treeviews.autoSize(frame6, 7, 0)