import tkinter as tk    
from tkinter import * 
import sqlite3
 
class Frame1():
    def __init__(self):
        self.x = None

    def frame_1(self, root, BCOLOR, DATABASE, treeviews):
        global frame1
        frame1 = LabelFrame(root, text='Input for Database', padx = 5, pady=5)
        frame1.grid(row=0, column=2, padx=10, pady=0, sticky=EW)   
        treeviews.autoSize(root, 0, 2)

        global selectBox
        selectBox = Entry(frame1, width=10)
        selectBox.bind("<Return>", lambda event, arg=DATABASE: self.event_edit(event, arg))
        selectBox.grid(row=2, column=1, padx=(0, 65), pady=(15, 0), sticky=EW)

        updateB = Button(frame1, text="Edit Record", command=lambda: self.edit(DATABASE), bg=BCOLOR, fg='white')
        updateB.bind("<Return>", lambda event, arg=DATABASE: self.event_edit(event, arg))
        updateB.grid(row=3, column=0, columnspan=2, pady=(5, 15), padx=10, ipadx=103, sticky=EW)
        treeviews.autoSize(frame1, 3, 0)
        removeB = Button(frame1, text="Remove Record", command=lambda: self.remove(DATABASE), bg=BCOLOR, fg='white')
        removeB.bind("<Return>", lambda event, arg=DATABASE: self.event_remove(event, DATABASE))
        removeB.grid(row=4, column=0, columnspan=2, pady=(30, 20), padx=10, ipadx=91, sticky=EW)
        treeviews.autoSize(frame1, 4, 0)
        submitB = Button(frame1, text="Add To Database", command=lambda: self.add(DATABASE), bg=BCOLOR, fg='white')
        submitB.bind("<Return>", lambda event, arg=DATABASE: self.event_add(event, arg))
        submitB.grid(row=1, column=0, columnspan=2, pady=(20, 30), padx=10, ipadx=90, sticky=EW)

        selectLabel = Label(frame1, text="Select Unique ID")
        selectLabel.grid(row=2, column=0, pady=(10, 0), sticky=E)

    def getFrame1(self):
        return frame1.get()

    def setSelectBox(self, numberID):
        selectBox.insert(0, numberID)

    def getSelectBox(self):
        return selectBox.get()

    def clearSelectBox(self):
        selectBox.delete(0, END)

    def event_add(self, event, DATABASE):
        self.add(DATABASE)

    def event_submit(self, event, DATABASE):
        self.submit(DATABASE)

    def submit(self, DATABASE):
        dbase = sqlite3.connect(DATABASE)
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
        #self.frame4.supplierDD(self.frame4, self.DATABASE)
        #self.frame4.manufacturerDD(self.frame4, self.DATABASE)

    # This function creates another window with the ability to add data to database.
    def add(self, DATABASE):
        global addWindow
        addWindow = Tk()
        addWindow.title("Add New Record")
        addWindow.geometry("350x225")
        bgcolor = '#A45A52'
        fgcolor = 'white'
        addWindow.configure(bg=bgcolor)
        
        dbase = sqlite3.connect(DATABASE)
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
        save = Button(addWindow, text="Save Record In Database", command=lambda: self.submit(DATABASE), bg='#420D09', fg='white')
        save.bind("<Return>", lambda event, arg=DATABASE: self.event_submit(event, DATABASE))
        save.grid(row=8, column=0, columnspan=2, pady=1, padx=10, ipadx=80)  

    def event_edit(self, event, DATABASE):
        self.edit(DATABASE)    

    # This function creates another window with the ability to change data in a record.
    def edit(self, DATABASE):
        global editWindow
        editWindow = Tk()
        editWindow.title("Edit Existing Record")
        editWindow.geometry("350x225")
        bgcolor = '#A45A52'
        fgcolor = 'white'
        editWindow.configure(bg=bgcolor)
        
        dbase = sqlite3.connect(DATABASE)
        c1 = dbase.cursor()

        recordID = self.getSelectBox()
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
                save = Button(editWindow, text="Save Record In Database", command=lambda: self.editWindow_update(DATABASE), bg='#420D09', fg='white')
                save.bind("<Return>", lambda event, arg=DATABASE: self.editWindow_event_update(event, DATABASE))
                save.grid(row=8, column=0, columnspan=2, pady=1, padx=10, ipadx=80)
                removeB = Button(editWindow, text="Remove Record", command=lambda: self.editWindow_remove(DATABASE), bg='#420D09', fg='white')
                removeB.bind("<Return>", lambda event, arg=DATABASE: self.editWindow_event_remove(event, DATABASE))
                removeB.grid(row=9, column=0, columnspan=2, pady=(1), padx=10, ipadx=103)
            except:
                tk.messagebox.showinfo(title='Attention:', message="Please Enter a Unique ID of Record to Edit...")

    def event_remove(self, event, DATABASE):
        self.remove(DATABASE)

    def editWindow_event_remove(self, event, DATABASE):
        self.remove(DATABASE)
        self.closeEditWindow()

    def editWindow_remove(self, DATABASE):
        self.remove(DATABASE)
        self.closeEditWindow()

    # Function to remove a record from the database.
    def remove(self, DATABASE):
        dbase = sqlite3.connect(DATABASE)
        c1 = dbase.cursor()

        recordID = self.getSelectBox()
        if recordID != None:
            try:
                c1.execute("DELETE from allMaterial WHERE oid = " + recordID)  
                dbase.commit()
                dbase.close()
                self.clearSelectBox()
                #self.supplierDD(self.frame4, self.DATABASE)
                #self.manufacturerDD(self.frame4, self.DATABASE)
                tk.messagebox.showinfo(title='Information:', message="Record Removed...")
            except:  
                tk.messagebox.showinfo(title='Attention:', message="Please Enter a Unique ID of Record to Remove...")

    def closeEditWindow(self):
        editWindow.destroy()

    def event_update(self, event, DATABASE):
        self.update(DATABASE)

    def editWindow_update(self, DATABASE):
        self.update(DATABASE)
        self.closeEditWindow()

    def editWindow_event_update(self, event, DATABASE):
        self.update(DATABASE)
        self.closeEditWindow()

    # Function updates the database from the text boxes in the pop up window
    def update(self, DATABASE):
        dbase = sqlite3.connect(DATABASE)
        c1 = dbase.cursor()
        recordID = self.getSelectBox()
                        
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
           
        self.clearSelectBox()               
        dbase.commit()
        dbase.close()
        #self.supplierDD(self.frame4, self.DATABASE)
        #self.manufacturerDD(self.frame4, self.DATABASE)