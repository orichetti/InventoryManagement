import tkinter as tk    
from tkinter import *
from classFrame8 import *
from classQueryFunctions import *

class Frame5():
    def __init__(self, root):
        self.root = root
        global frame8
        frame8 = Frame8()
        
    def frame_5(self, root, treeviews, BCOLOR, DATABASE):
        global frame5
        frame5 = LabelFrame(frame8.getFrame8(), text="Query Entire Database", padx=5, pady=1)
        frame5.grid(row=2, column=0, columnspan=2, padx=1, pady=2, sticky=EW)
        treeviews.autoSize(frame5, 9, 0) # Original code has frame8, throwing error: 'Frame8' object has no attribute '_grid_configure'

        global grandTotalBox
        grandTotalBox = Entry(frame5, width=30)
        grandTotalBox.grid(row=2, column=1, pady=9.499999999999999, sticky=W)
        treeviews.autoSize(frame5, 2, 1)

        queryB = Button(frame5, text="Show All Records", command=lambda: self.allDataQuery(root, treeviews, DATABASE), bg=BCOLOR, fg='white')
        queryB.bind("<Return>", lambda event, arg=DATABASE: self.event_allDataQuery(event, root, treeviews, arg))
        queryB.grid(row=0, column=0, columnspan=2, pady=5, padx=1, ipadx=85, sticky=EW)
        treeviews.autoSize(frame5, 0, 0)
        
        treeviews.autoSize(frame5, 1, 0)

        grandTotalLabel = Label(frame5, text="Grand Total in Treeview = ")
        grandTotalLabel.grid(row=2, column=0, pady=2, sticky=E)
        treeviews.autoSize(frame5, 2, 0)

    def getFrame5(self):
        return frame5

    def grandTotalBox(self, recordLimit, frame5):
        #grandTotalBox = Entry(frame7, width=30)
        #grandTotalBox.grid(row=2, column=1, pady=9.499999999999999, sticky=W)
        self.setGrandTotal(recordLimit)
        #treeviews.autoSize(frame5, 2, 1)

    def clearGrandTotal(self):
        grandTotalBox.delete(0, END)

    def setGrandTotal(self, recordLimit):
        self.clearGrandTotal()
        grandTotalBox.insert(0, recordLimit)

    def allDataQuery(self, root, treeviews, DATABASE):
        queryFunctions = QueryFunctions(root, DATABASE, treeviews)
        print("qeuryFunctions instantiated")
        print("calling queryFunctions.allDataquery")
        queryFunctions.allDataquery(DATABASE, treeviews)
        self.subTotal(treeviews)

    def event_allDataQuery(self, event, root, treeviews, DATABASE):
        self.allDataQuery(root, treeviews, DATABASE)

    def subTotal(self, treeviews):
        data = treeviews.tv1Item()
        newList = []
        for i in data:
            i[7] = i[7].replace("$", "")
            newList.append(float(i[7]))
        newTotal = sum(newList)
        recordLimit = "$" + str("{:.2f}".format(newTotal))
        self.setGrandTotal(recordLimit)