import tkinter as tk    
from tkinter import *
from classTreeviews import *

class Frame8():
    def __init__(self):
        self.x = None

    def frame_8(self, root, treeviews):
        global frame8
        frame8 = LabelFrame(root, text='Database Output', padx = 5, pady=5)
        frame8.grid(row=0, column=0, padx=10, pady=0, sticky=EW)
        treeviews.autoSize(root, 0, 0)
        self.setFrame8(frame8)

    def setFrame8(self, x):
        self.x = frame8

    def getFrame8(self):
        return frame8