import tkinter as tk    
from tkinter import *
from classFrame5 import *
from classFrame8 import *

class Frame7():
    def __init__(self, root):
        self.froot = root
        global frame5
        frame5 = Frame5(root)
        global frame8
        frame8 = Frame8()

    def frame_7(self, treeviews, BCOLOR, DATABASE, databaseFunctions):
        self.treeviews = treeviews
        frame7 = LabelFrame(frame8.getFrame8(), text='Custom', padx = 5, pady=1)
        frame7.grid(row=1, column=0, columnspan=2, padx=1, pady=0, sticky=EW)
        treeviews.autoSize(frame7, 5, 0) # Original code has frame8, throwing error: 'Frame8' object has no attribute '_grid_configure'

        customB = Button(frame7, text="Custom Database Query", command=lambda: self.customQuery(DATABASE), bg=BCOLOR, fg='white')
        customB.bind("<Return>", lambda event, arg=DATABASE: self.event_customQuery(event, arg))
        customB.grid(row=8, column=0, columnspan=2, padx=10, pady=5, ipadx=60, sticky=EW)
        treeviews.autoSize(frame7, 8, 0)
        saveToXlB = Button(frame7, text="Save Treeview To Excel", command=databaseFunctions.saveToXl, bg=BCOLOR, fg='white')
        saveToXlB.bind("<Return>", databaseFunctions.event_saveToXl)
        saveToXlB.grid(row=9, column=0, columnspan=2, padx=10, pady=(5, 10), ipadx=64.4999, sticky=EW)
        treeviews.autoSize(frame7, 9, 0)

    def event_customPhrase(self, event, DATABASE):
        self.customQuery(DATABASE)

    # this function is a work in progress. Creating options to choose for a custom query using dropdown menu's and possibly radio buttons.
    def customQuery(self, DATABASE): 
        global queryWindow
        global customBox_queryWindow
        queryWindow = Tk()
        queryWindow.title("Edit Existing Record")
        queryWindow.geometry("500x200")
        bgcolor = '#A45A52'
        fgcolor = 'white'
        queryWindow.configure(bg=bgcolor)

        # Create Textbox for custom query command
        customBox_queryWindow = Entry(queryWindow, width=75)
        customBox_queryWindow.grid(row=2, column=1, columnspan=2, padx=5)
        customBox_queryWindow.focus_force()
        # Create Label for custom query phrase
        customLabel_queryWindow = Label(queryWindow, text='Enter Custom SQL Command :', bg=bgcolor, fg=fgcolor)
        customLabel_queryWindow.grid(row=1, column=1, columnspan=2, padx=5, pady=10)
        # Create Save Button
        save_queryWindow = Button(queryWindow, text="Query Database", command=lambda: self.customPhrase(DATABASE), bg='#420D09', fg='white')
        save_queryWindow.bind("<Return>", lambda event, arg=DATABASE: self.event_customPhrase(event, arg))
        save_queryWindow.grid(row=3, column=1, columnspan=2, pady=60, padx=10, ipadx=40, sticky=E)

    def event_customPhrase(self, event, DATABASE):
        self.customPhrase(DATABASE)

    def customPhrase(self, DATABASE):
        phrase = customBox_queryWindow.get()
        try:
            self.treeviews.query(phrase, DATABASE)
            frame5.subTotal(self.treeviews)
        except: 
            tk.messagebox.showerror(title='Attention:', message="OOPS, " + "'" + phrase  + "'" + " is not a valid command...Plese type a valid SQLite3 command.")
        queryWindow.destroy()