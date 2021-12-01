from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.filedialog import asksaveasfile
import pandas as pd
import sqlite3
from classQueryFunctions import *
from classTreeviews import *

class DatabaseFunctions:
    def __init__(self, root, DATABASE, treeviews):
        self.root = root
        self.DATABASE = DATABASE
        self.treeviews = treeviews

        #global queryFunctions
        #queryFunctions = QueryFunctions(root, DATABASE)
        #global treeviews
        #treeviews = Treeview(root, DATABASE)
        #global frames
        #frames = Frames(root, DATABASE)
        #global entryBoxes
        #entryBoxes = EntryBoxes(root, DATABASE)

    def event_saveToXl(self, event):
        self.saveToXl()

    def saveToXl(self):
        file = filedialog.asksaveasfilename(title='Save location',defaultextension=[('csv','*.csv')],filetypes=[('CSV','*.csv')])
        if file != '':
            try:
                data = self.treeviews.tv1Item()
                df = pd.DataFrame (data)
                df.to_csv (file, header = False, index = False)
            except:
                tk.messagebox.showinfo(title='Attention:', message="You chose to cancel this operation.")
        else:
            tk.messagebox.showinfo(title='Attention:', message="You chose to cancel this operation.")