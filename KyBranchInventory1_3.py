import tkinter as tk    
from tkinter import *   
from tkinter import filedialog, messagebox
from tkinter.filedialog import asksaveasfile
from PIL import ImageTk, Image
import sqlite3
import csv
import pandas as pd
from classTreeviews import *
from classDatabaseFunctions import *
from classQueryFunctions import *
from classFrame1 import *
from classFrame2 import *
from classFrame3 import *
from classFrame4 import *
from classFrame5 import *
from classFrame6 import *
from classFrame7 import *
from classFrame8 import *

root = Tk()
root.title('Ky Branch Inventory1_3')
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (screenWidth, screenHeight))
root.iconbitmap('webp_net_resizeimage_loR_icon.ico')

#DATABASE = 'Y:\\Private\\Ky Inventory\\KyBranchInventory.db'
DATABASE = 'KyBranchInventory.db'

def testDatabaseConnection(DTATBASE):
    try:
        dbase = sqlite3.connect(DATABASE)
    except sqlite3.OperationalError:
        tk.messagebox.showerror(title='OperationalError:', message="Cannot connect to Database, please check network and VPN connections and restart application...")
        root.destroy()
        
testDatabaseConnection(DATABASE)   

BCOLOR = '#4682B4' # Button Color for Main Root


frame3 = Frame3(root)
#w = frame3.getFrame3()
treeviews = Treeview(frame3.getFrame3())
treeviews.treeview1(DATABASE)
databaseFunctions = DatabaseFunctions(root, DATABASE, treeviews)
queryFunctions = QueryFunctions(root, DATABASE, treeviews)
frame8 = Frame8()
frame8.frame_8(root, treeviews)
frame1 = Frame1()
frame1.frame_1(root, BCOLOR, DATABASE, treeviews)
frame2 = Frame2(root)
frame2.frame_2(root, BCOLOR, DATABASE, treeviews)

#frame3.frame_3(root, DATABASE, treeviews, databaseFunctions, w)

frame4 = Frame4(root)
frame4.frame_4(root, treeviews, BCOLOR, DATABASE)
frame5 = Frame5(root)
frame5.frame_5(root, treeviews, BCOLOR, DATABASE)
frame6 = Frame6()
frame6.frame_6(root, treeviews, BCOLOR)
frame7 = Frame7(root)
frame7.frame_7(treeviews,BCOLOR, DATABASE, databaseFunctions)



clearB = Button(frame5.getFrame5(), text="Clear Window", command=lambda: clear(), bg=BCOLOR, fg='white')
clearB.bind("<Return>", lambda event: event_clear(event))
clearB.grid(row=1, column=0, columnspan=2, pady=5, padx=1, ipadx=93.5, sticky=EW)

def event_clear(event):
        clear()

def clear():
    treeviews.clearTv1()
    frame1.clearSelectBox()
    frame4.clearModelBox()
    frame4.clearDescriptionBox()
    frame4.clearSupplierDD()
    frame4.clearManDD()
    frame4.clearValueLessBox()
    frame4.clearQuantityLessBox()
    frame4.clearTotalLessBox()
    frame4.clearValueGreaterBox()
    frame4.clearQuantityGreaterBox()
    frame4.clearTotalGreaterBox()
    frame5.clearGrandTotal()

root.mainloop()