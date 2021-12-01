from tkinter import *
import tkinter as tk
from classTreeviews import *

class QueryFunctions:
    def __init__(self, root, DATABASE, treeviews):
        self.root = root
        self.DATABASE = DATABASE
        self.treeviews = treeviews

    # Displays the entire database in the Treeview
    def allDataquery(self, DATABASE, treeviews):
        phrase = "SELECT oid, * FROM allMaterial"
        print("calling treeviews.query")
        treeviews.query(phrase, DATABASE)

    # Queries data base from Supplier column from dropdown Menu only
    def supplyQuery(self, DATABASE, w):
        phrase = "SELECT oid, * FROM allMaterial WHERE Supplier LIKE " + "'" + w + "'"
        self.treeviews.query(phrase, DATABASE)

    # Queries data base from Manufacturer column from dropdown Menu only
    def manufactureQuery(self, DATABASE, w):
        phrase = "SELECT oid, * FROM allMaterial WHERE Manufacturer = " + "'" + w + "'"
        self.treeviews.query(phrase, DATABASE)

    # This function queries the database using the Model column using partial text...not case sensative
    def modelQuery(self, DATABASE, w):
        #w = entryBoxes.getModelBox()
        phrase = "SELECT oid, * FROM allMaterial WHERE Model like " + "'%" + w + "%'"
        self.treeviews.query(phrase, DATABASE)

    # This function queries the database using the Description column using partial text...not case sensative
    def descriptionQuery(self, DATABASE, w):
        #w = entryBoxes.getDescriptionBox()
        phrase = "SELECT oid, * FROM allMaterial WHERE Description like " + "'%" + w + "%'"
        self.treeviews.query(phrase, DATABASE)

    # This function orders the database using the Supplier column ascending from lowest value to highest value
    def groupSupplierQuery(self, DATABASE):
        phrase = "SELECT oid, * FROM allMaterial Order BY Supplier ASC"
        self.treeviews.query(phrase, DATABASE)

    # This function orders the database using the Manufacturer column ascending from lowest value to highest value
    def groupManufacturerQuery(self, DATABASE):
        phrase = "SELECT oid, * FROM allMaterial Order BY Manufacturer ASC"
        self.treeviews.query(phrase, DATABASE)

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
