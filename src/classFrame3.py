import tkinter as ttk    
from tkinter import *
from classTreeviews import *
from classDatabaseFunctions import *
from classFrame1 import *

class Frame3:
    def __init__(self, root):
        self.root = root
        global frame1
        frame1 = Frame1()
        global frame3
        frame3 = LabelFrame(root, text='Search Results')
        frame3.grid(row=1, column=0, columnspan=5, padx=10, pady=0, sticky=EW)
        
            

    def frame_3(self, root, DATABASE, treeviews, databaseFunctions, w):
        frame3 = LabelFrame(root, text='Search Results')
        frame3.grid(row=1, column=0, columnspan=5, padx=10, pady=0, sticky=EW)
        treeviews.autoSize(root, 1, 0)
        
        if treeviews.getDoubleClick() == True:
            print(doubleclick)
            self.doubleClick()
        else:
            pass

    def getFrame3(self):
        return frame3

    def doubleClick(self, DATABASE, treeviews, databaseFunctions):
        frame1.clearSelectBox()
        row = treeviews.getRow()
        numberID = treeviews.getNumberID()
        frame1.setSelectBox(numberID)
        databaseFunctions.edit(DATABASE)
        