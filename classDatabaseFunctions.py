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
    '''
    def event_submit(self, event, DATABASE):
        self.submit(self.DATABASE)

    def submit(self, DATABASE):
        dbase = sqlite3.connect(self.DATABASE)
        c1 = dbase.cursor()
        # Insert into Table 
        c1.execute("INSERT INTO allMaterial VALUES (:supplier, :manufacturer, :model, :description, :value, :quantity, :totalValue)", 
            {
                'supplier': supplierBox_addWindow.get(),
                'manufacturer': manufacturerBox_addWindow.get(),
                'model': modelBox_addWindow.get(),
                'description': descriptionBox_addWindow.get(),
                'value': valueBox_addWindow.get(),
                'quantity': quantityBox_addWindow.get(),
                'totalValue': float(valueBox_addWindow.get()) * float(quantityBox_addWindow.get())  #totalValueBox.get()
             })
        
        dbase.commit()
        dbase.close()
        addWindow.destroy()
        comboBoxes.supplierDD(frames.getFrame4(), self.DATABASE)
        comboBoxes.manufacturerDD(frames.getFrame4(), self.DATABASE)

    def event_add(self, event, DATABASE):
        self.add(self.DATABASE)

    # This function creates another window with the ability to add data to database.
    def add(self, DATABASE):
        global addWindow
        addWindow = Tk()
        addWindow.title("Add New Record")
        addWindow.geometry("350x225")
        bgcolor = '#A45A52'
        fgcolor = 'white'
        addWindow.configure(bg=bgcolor)
        
        dbase = sqlite3.connect(self.DATABASE)
        c1 = dbase.cursor()

        global supplierBox_addWindow
        global manufacturerBox_addWindow
        global modelBox_addWindow
        global descriptionBox_addWindow
        global valueBox_addWindow
        global quantityBox_addWindow

        #  Create Text Boxes for input in new window
        supplierBox_addWindow = Entry(addWindow, width=30)
        supplierBox_addWindow.grid(row=0, column=1, padx=10, pady=(10, 0))
        supplierBox_addWindow.focus_force()
        manufacturerBox_addWindow = Entry(addWindow, width=30)
        manufacturerBox_addWindow.grid(row=1, column=1)
        modelBox_addWindow = Entry(addWindow, width=30)
        modelBox_addWindow.grid(row=2, column=1)
        descriptionBox_addWindow = Entry(addWindow, width=30)
        descriptionBox_addWindow.grid(row=3, column=1)
        valueBox_addWindow = Entry(addWindow, width=30)
        valueBox_addWindow.grid(row=4, column=1)
        quantityBox_addWindow = Entry(addWindow, width=30)
        quantityBox_addWindow.grid(row=5, column=1)

        # Create Text Box Labels in new window
        supplierLabel_addWindow = Label(addWindow, text="Supplier", bg=bgcolor, fg=fgcolor)
        supplierLabel_addWindow.grid(row=0, column= 0, pady=(10, 0), sticky=E)
        manufacturerLabel_addWindow = Label(addWindow, text="Manufacturer", bg=bgcolor, fg=fgcolor)
        manufacturerLabel_addWindow.grid(row=1, column= 0, sticky=E)
        modelLabel_addWindow = Label(addWindow, text="Model", bg=bgcolor, fg=fgcolor)
        modelLabel_addWindow.grid(row=2, column= 0, sticky=E)
        descriptionLabel_addWindow = Label(addWindow, text="Discription", bg=bgcolor, fg=fgcolor)
        descriptionLabel_addWindow.grid(row=3, column= 0, sticky=E)
        valueLabel_addWindow = Label(addWindow, text="Value", bg=bgcolor, fg=fgcolor)
        valueLabel_addWindow.grid(row=4, column= 0, sticky=E)
        quantityLabel_addWindow = Label(addWindow, text="Quantity", bg=bgcolor, fg=fgcolor)
        quantityLabel_addWindow.grid(row=5, column= 0, sticky=E)

        # Create Save Button
        save = Button(addWindow, text="Save Record In Database", command=lambda: self.submit(self.DATABASE), bg='#420D09', fg='white')
        save.bind("<Return>", lambda event, arg=DATABASE: self.event_submit(event, self.DATABASE))
        save.grid(row=8, column=0, columnspan=2, pady=1, padx=10, ipadx=80)

    def event_remove(self, event, DATABASE):
        self.remove(self.DATABASE)

    def editWindow_remove(self, DATABASE):
        self.remove(self.DATABASE)
        self.closeEditWindow()

    def editWindow_event_remove(self, event, DATABASE):
        self.remove(self.DATABASE)
        self.closeEditWindow()

    # Function to remove a record from the database.
    def remove(self, DATABASE, recordID):
        dbase = sqlite3.connect(self.DATABASE)
        c1 = dbase.cursor()

        self.recordID = recordID
        if self.recordID != None:
            try:
                c1.execute("DELETE from allMaterial WHERE oid = " + self.recordID)  
                dbase.commit()
                dbase.close()
                entryBoxes.clearSelectBox()
                comboBoxes.supplierDD(frames.getFrame4(), self.DATABASE)
                comboBoxes.manufacturerDD(frames.getFrame4(), self.DATABASE)
                tk.messagebox.showinfo(title='Information:', message="Record Removed...")
            except:  
                tk.messagebox.showinfo(title='Attention:', message="Please Enter a Unique ID of Record to Remove...")

    def event_edit(self, event, DATABASE):
        self.edit(self.DATABASE)    

    # This function creates another window with the ability to change data in a record.
    def edit(self, DATABASE):
        global editWindow
        editWindow = Tk()
        editWindow.title("Edit Existing Record")
        editWindow.geometry("350x225")
        bgcolor = '#A45A52'
        fgcolor = 'white'
        editWindow.configure(bg=bgcolor)
        
        dbase = sqlite3.connect(self.DATABASE)
        c1 = dbase.cursor()

        recordID = entryBoxes.getSelectBox()
        if recordID != None:
            try:
                # Query Database
                c1.execute("SELECT * FROM allMaterial WHERE oid=" + recordID)
                records = c1.fetchall()

                global supplierBox_editWindow
                global manufacturerBox_editWindow
                global modelBox_editWindow
                global descriptionBox_editWindow
                global valueBox_editWindow
                global quantityBox_editWindow

                #  Create Text Boxes for input in new window
                supplierBox_editWindow = Entry(editWindow, width=30)
                supplierBox_editWindow.grid(row=0, column=1, padx=10, pady=(10, 0))
                supplierBox_editWindow.focus_force()
                manufacturerBox_editWindow = Entry(editWindow, width=30)
                manufacturerBox_editWindow.grid(row=1, column=1)
                modelBox_editWindow = Entry(editWindow, width=30)
                modelBox_editWindow.grid(row=2, column=1)
                descriptionBox_editWindow = Entry(editWindow, width=30)
                descriptionBox_editWindow.grid(row=3, column=1)
                valueBox_editWindow = Entry(editWindow, width=30)
                valueBox_editWindow.grid(row=4, column=1)
                quantityBox_editWindow = Entry(editWindow, width=30)
                quantityBox_editWindow.grid(row=5, column=1)
                totalValueBox_editWindow = Entry(editWindow, width=30)
                totalValueBox_editWindow.grid(row=6, column=1)

                # Create Text Box Labels in new window
                supplierLabel_editWindow = Label(editWindow, text="Supplier", bg=bgcolor, fg=fgcolor)
                supplierLabel_editWindow.grid(row=0, column= 0, pady=(10, 0), sticky=E)
                manufacturerLabel_editWindow = Label(editWindow, text="Manufacturer", bg=bgcolor, fg=fgcolor)
                manufacturerLabel_editWindow.grid(row=1, column= 0, sticky=E)
                modelLabel_editWindow = Label(editWindow, text="Model", bg=bgcolor, fg=fgcolor)
                modelLabel_editWindow.grid(row=2, column= 0, sticky=E)
                descriptionLabel_editWindow = Label(editWindow, text="Discription", bg=bgcolor, fg=fgcolor)
                descriptionLabel_editWindow.grid(row=3, column= 0, sticky=E)
                valueLabel_editWindow = Label(editWindow, text="Value", bg=bgcolor, fg=fgcolor)
                valueLabel_editWindow.grid(row=4, column= 0, sticky=E)
                quantityLabel_editWindow = Label(editWindow, text="Quantity", bg=bgcolor, fg=fgcolor)
                quantityLabel_editWindow.grid(row=5, column= 0, sticky=E)
                totalValueLabel_editWindow = Label(editWindow, text="TotalValue", bg=bgcolor, fg=fgcolor)
                totalValueLabel_editWindow.grid(row=6, column= 0, sticky=E)

                # Loop through results
                for record in records:
                    supplierBox_editWindow.insert(0, record[0])
                    manufacturerBox_editWindow.insert(0, record[1])
                    modelBox_editWindow.insert(0, record[2])
                    descriptionBox_editWindow.insert(0, record[3])
                    valueBox_editWindow.insert(0, record[4])
                    quantityBox_editWindow.insert(0, record[5])
                    totalValueBox_editWindow.insert(0, record[6])

                # Create Save Button
                save = Button(editWindow, text="Save Record In Database", command=lambda: self.editWindow_update(self.DATABASE), bg='#420D09', fg='white')
                save.bind("<Return>", lambda event, arg=DATABASE: self.editWindow_event_update(event, self.DATABASE))
                save.grid(row=8, column=0, columnspan=2, pady=1, padx=10, ipadx=80)
                removeB = Button(editWindow, text="Remove Record", command=lambda: self.editWindow_remove(self.DATABASE), bg='#420D09', fg='white')
                removeB.bind("<Return>", lambda event, arg=DATABASE: self.editWindow_event_remove(event, self.DATABASE))
                removeB.grid(row=9, column=0, columnspan=2, pady=(1), padx=10, ipadx=103)
            except:
                tk.messagebox.showinfo(title='Attention:', message="Please Enter a Unique ID of Record to Edit...")

    def closeEditWindow(self):
        editWindow.destroy()

    def event_update(self, event, DATABASE):
        self.update(self.DATABASE)

    def editWindow_update(self, DATABASE):
        self.update(self.DATABASE)
        self.closeEditWindow()

    def editWindow_event_update(self, event, DATABASE):
        self.update(self.DATABASE)
        self.closeEditWindow()

    # Function updates the database from the text boxes in the pop up window
    def update(self, DATABASE):
        dbase = sqlite3.connect(self.DATABASE)
        c1 = dbase.cursor()
        recordID = entryBoxes.selectBox.get()
                        
        c1.execute("""UPDATE allMaterial SET
            supplier = :supplier,
            manufacturer = :manufacturer,
            model = :model,
            description = :description,
            value = :value,
            quantity = :quantity,
            totalValue = :totalValue
            WHERE oid = :oid""",
            {'supplier': supplierBox_editWindow.get(),
            'manufacturer': manufacturerBox_editWindow.get(),
            'model': modelBox_editWindow.get(),
            'description': descriptionBox_editWindow.get(),
            'value': valueBox_editWindow.get(),
            'quantity': quantityBox_editWindow.get(),
            'totalValue': float(valueBox_editWindow.get()) * float(quantityBox_editWindow.get()),
            'oid': recordID})
           
        entryBoxes.clearSelectBox()               
        dbase.commit()
        dbase.close()
        comboBoxes.supplierDD(frames.getFrame4(), self.DATABASE)
        comboBoxes.manufacturerDD(frames.getFrame4(), self.DATABASE)'''

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