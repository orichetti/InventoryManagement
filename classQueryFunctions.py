from tkinter import *
import tkinter as tk
from classTreeviews import *

class QueryFunctions:
    def __init__(self, root, DATABASE, treeviews):
        self.root = root
        self.DATABASE = DATABASE
        self.treeviews = treeviews

        #global treeviews
        #treeviews = Treeview(root, DATABASE)

    #def event_allDataquery(self, DATABASE):
        #allDataquery(self.DATABASE)

    # Displays the entire database in the Treeview
    def allDataquery(self, DATABASE, treeviews):
        phrase = "SELECT oid, * FROM allMaterial"
        print("calling treeviews.query")
        treeviews.query(phrase, DATABASE)
        
    #def event_supplyQuery(self, event, DATABASE):
        #supplyQuery(self.DATABASE)

    def supplyQuery(self, DATABASE, w):
        #w = comboBoxes.clicked1.get()
        phrase = "SELECT oid, * FROM allMaterial WHERE Supplier LIKE " + "'" + w + "'"
        self.treeviews.query(phrase, DATABASE)
        #entryBoxes.subTotal()

    #def event_manufactureQuery(self, event, DATABASE):
        #manufactureQuery(self.DATABASE)

    # Queries data base from Manufacturer column from dropdown Menu only
    def manufactureQuery(self, DATABASE, w):
        phrase = "SELECT oid, * FROM allMaterial WHERE Manufacturer = " + "'" + w + "'"
        self.treeviews.query(phrase, DATABASE)
        #entryBoxes.subTotal()

    #def event_modelQuery(self, event, DATABASE):
        #modelQuery(self.DATABASE)

    # This function queries the database using the Model column using partial text...not case sensative
    def modelQuery(self, DATABASE, w):
        #w = entryBoxes.getModelBox()
        phrase = "SELECT oid, * FROM allMaterial WHERE Model like " + "'%" + w + "%'"
        self.treeviews.query(phrase, DATABASE)

    #def event_descriptionQuery(self, event, DATABASE):
        #descriptionQuery(self.DATABASE)

    # This function queries the database using the Description column using partial text...not case sensative
    def descriptionQuery(self, DATABASE, w):
        #w = entryBoxes.getDescriptionBox()
        phrase = "SELECT oid, * FROM allMaterial WHERE Description like " + "'%" + w + "%'"
        self.treeviews.query(phrase, DATABASE)

    #def event_groupSupplierQuery(self, event, DATABASE):
        #groupSupplierQuery(self.DATABASE)

    # This function orders the database using the Supplier column ascending from lowest value to highest value
    def groupSupplierQuery(self, DATABASE):
        phrase = "SELECT oid, * FROM allMaterial Order BY Supplier ASC"
        self.treeviews.query(phrase, DATABASE)
       
    #def event_groupManufacturerQuery(self, event, DATABASE):
        #self.groupManufacturerQuery(self.DATABASE)

    # This function orders the database using the Manufacturer column ascending from lowest value to highest value
    def groupManufacturerQuery(self, DATABASE):
        phrase = "SELECT oid, * FROM allMaterial Order BY Manufacturer ASC"
        self.treeviews.query(phrase, DATABASE)
        #entryBoxes.subTotal()

    def event_groupModelQuery(self, event, DATABASE):
        self.groupModelQuery(self.DATABASE)

    # This function orders the database using the Model column ascending from lowest value to highest value
    def groupModelQuery(self, DATABASE):
        phrase = "SELECT oid, * FROM allMaterial Order BY Model ASC"
        self.treeviews.query(phrase, DATABASE)

    def event_groupDescriptionQuery(self, event, DATABASE):
        self.groupDescriptionQuery(DATABASE)

    # This function orders the database using the Description column ascending from lowest value to highest value
    def groupDescriptionQuery(self, DATABASE):
        phrase = "SELECT oid, * FROM allMaterial Order BY Description ASC"
        self.treeviews.query(phrase, self.DATABASE)

    def event_groupValueQuery(self, event, DATABASE):
        self.groupQuantityQuery(DATABASE)

    # This function orders the database using the Value column ascending from lowest value to highest value
    def groupValueQuery(self, DATABASE):
        phrase = "SELECT oid, * FROM allMaterial Order BY Value ASC"
        self.treeviews.query(phrase, self.DATABASE)

    def event_groupQuantityQuery(self, event, DATABASE):
        self.groupQuantityQuery(DATABASE)

    # This function orders the database using the Quantity column ascending from lowest quantity to highest value
    def groupQuantityQuery(self, DATABASE):
        phrase = "SELECT oid, * FROM allMaterial Order BY Quantity ASC"
        self.treeviews.query(phrase, self.DATABASE)

    def event_groupTotalQuery(self, event, DATABASE):
        self.groupTotalQuery(DATABASE)

    # This function orders the database using the TotalValue column ascending from lowest value to Highest value
    def groupTotalQuery(self, DATABASE):
        phrase = "SELECT oid, * FROM allMaterial Order BY TotalValue ASC"
        self.treeviews.query(phrase, DATABASE)
    '''
    def event_customPhrase(self, event, DATABASE):
        self.customQuery(self.DATABASE)

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
        save_queryWindow = Button(queryWindow, text="Query Database", command=lambda: self.customPhrase(self.DATABASE), bg='#420D09', fg='white')
        save_queryWindow.bind("<Return>", lambda event, arg=self.DATABASE: self.event_customPhrase(event, arg))
        save_queryWindow.grid(row=3, column=1, columnspan=2, pady=60, padx=10, ipadx=40, sticky=E)

    def event_customPhrase(self, event, DATABASE):
        self.customPhrase(self.DATABASE)

    def customPhrase(self, DATABASE):
        phrase = customBox_queryWindow.get()
        try:
            treeviews.query(phrase, self.DATABASE)
            entryBoxes.subTotal()
        except: 
            tk.messagebox.showerror(title='Attention:', message="OOPS, " + "'" + phrase  + "'" + " is not a valid command...Plese type a valid SQLite3 command.")
        queryWindow.destroy()'''

    def event_valueLessQuery(self, DATABASE, w):
        #w = entryBoxes.getValueLessBox()
        phrase = "SELECT oid, * FROM allMaterial WHERE Value <= " + "'" + w + "'"
        self.treeviews.query(phrase, DATABASE)
        #entryBoxes.subTotal()

    def event_quantityLessQuery(self, DATABASE, w):
        #w = entryBoxes.getQuantityLessBox()
        phrase = "SELECT oid, * FROM allMaterial WHERE Quantity <= " + "'" + w + "'"
        self.treeviews.query(phrase, DATABASE)
        #entryBoxes.subTotal()

    def event_totalLessQuery(self, DATABASE, w):
        #w = entryBoxes.getTotalLessBox()
        phrase = "SELECT oid, * FROM allMaterial WHERE TotalValue <= " + "'" + w + "'"
        self.treeviews.query(phrase, DATABASE)
        #entryBoxes.subTotal()

    def event_valueGreaterQuery(self, DATABASE, w):
        #w = entryBoxes.getValueGreaterBox()
        phrase = "SELECT oid, * FROM allMaterial WHERE Value >= " + "'" + w + "'"
        self.treeviews.query(phrase, DATABASE)
        #entryBoxes.subTotal()

    def event_quantityGreaterQuery(self, DATABASE, w):
        #w = entryBoxes.getQuantityGreaterBox()
        phrase = "SELECT oid, * FROM allMaterial WHERE Quantity >= " + "'" + w + "'"
        self.treeviews.query(phrase, DATABASE)
        #entryBoxes.subTotal()

    def event_totalGreaterQuery(self, DATABASE, w):
        #w = entryBoxes.getTotalGreaterBox()
        phrase = "SELECT oid, * FROM allMaterial WHERE TotalValue >= " + "'" + w + "'"
        self.treeviews.query(phrase, DATABASE)
        #entryBoxes.subTotal()
