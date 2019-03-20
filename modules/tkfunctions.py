import tkinter as tk
import pandas as pd
from tkinter import font
from tkinter import ttk
from modules import dataretrieval as dr

class OptionsCombobox():
    def __init__(self, frame, list, row, column):
        self._frame = frame
        self._list = list
        self._row = row
        self._column = column
        self._state = 'readonly'
        self._default = "None"
        self._createBox()
        self._displayBox()

    def _createBox(self):
        self._box = ttk.Combobox(self._frame, values = self._list, state = self._state)
        self._box.set(self._default)

    def _displayBox(self):
        self._box.grid(row = self._row, column = self._column)
        self._box.config(width = 13, justify = tk.LEFT)


def fnf_popup():
    win = tk.Tk()
    win.title("File Error")

    fnfLabel = tk.Label(win, text = "The data file was not found.\n Please ensure the file 'ProjectData.csv' is present in the data folder.")
    fnfLabel.pack()

    fnfButton = tk.Button(text = "OK", command = win.destroy).pack()

def create_auto_tabs(frame):
    criteriaTabs = ttk.Notebook(frame) # The pages used to tab through the criteria

    critMonth = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # First page,

    critDistance = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # Second page

    critCarrier = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # Third page

    critOriginCity = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # Fourth page

    critDestCity = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # Fifth page

    critAircraft = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # Sixth page

    critOriginState = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # Seventh page

    critDestState = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # Eigth page

    criteriaTabs.add(critMonth, text = 'Month')
    criteriaTabs.add(critDistance, text = 'Distance')
    criteriaTabs.add(critCarrier, text = 'Carrier')
    criteriaTabs.add(critOriginCity, text = 'Origin City')
    criteriaTabs.add(critDestCity, text = 'Destination City')
    criteriaTabs.add(critAircraft, text = 'Aircraft')
    criteriaTabs.add(critOriginState, text = 'Origin State')
    criteriaTabs.add(critDestState, text = 'Destination State')
    criteriaTabs.pack()

    text = tk.Label(critMonth, text = "EEEEE")
    text.pack(side = "top", fill = 'both', expand = 1)

    flightTree = ttk.Treeview(critMonth)
    flightTree.config(height = 20) # 33 for max height
    flightTree.pack(side = 'left')

    treeScrollBar = ttk.Scrollbar(critMonth,
        orient = "vertical",
        command = flightTree.yview)
    treeScrollBar.pack(side = 'right', fill = 'y')

    flightTree.configure(yscrollcommand= treeScrollBar.set)

    flightTree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
    flightTree['show'] = 'headings'

    flightTree.column("1", width = 110, anchor = 'c')
    flightTree.column("2", width = 110, anchor = 'c')
    flightTree.column("3", width = 110, anchor = 'c')
    flightTree.column("4", width = 110, anchor = 'c')
    flightTree.column("5", width = 110, anchor = 'c')
    flightTree.column("6", width = 110, anchor = 'c')
    flightTree.column("7", width = 110, anchor = 'c')
    flightTree.column("8", width = 110, anchor = 'c')
    flightTree.column("9", width = 110, anchor = 'c')
    flightTree.column("10", width = 110, anchor = 'c')
    flightTree.column("11", width = 110, anchor = 'c')
    flightTree.column("12", width = 110, anchor = 'c')
    flightTree.column("13", width = 110, anchor = 'c')

    flightTree.heading("1", text = "% of Success")
    flightTree.heading("2", text = "Scheduled")
    flightTree.heading("3", text = "Performed")
    flightTree.heading("4", text = "Seats")
    flightTree.heading("5", text = "Passengers")
    flightTree.heading("6", text = "Distance (mi.)")
    flightTree.heading("7", text = "Carrier")
    flightTree.heading("8", text = "Origin")
    flightTree.heading("9", text = "Destination")
    flightTree.heading("10", text = "Aircraft")
    flightTree.heading("11", text = "Origin State")
    flightTree.heading("12", text = "Dest State")
    flightTree.heading("13", text = "Month")

def create_manual_results_panel(frame, flightData):
    flightList = dr.convert_df(flightData)

    text = tk.Label(frame, text = "EEEEE")
    text.pack(side = "top", fill = 'both')

    flightTree = ttk.Treeview(frame)
    flightTree.config(height = 20) # 33 for max height
    flightTree.pack(side = 'left')

    treeScrollBar = ttk.Scrollbar(frame,
        orient = "vertical",
        command = flightTree.yview)
    treeScrollBar.pack(side = 'right', fill = 'y')

    flightTree.configure(yscrollcommand= treeScrollBar.set)

    flightTree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
    flightTree['show'] = 'headings'

    flightTree.column("1", width = 110, anchor = 'c')
    flightTree.column("2", width = 110, anchor = 'c')
    flightTree.column("3", width = 110, anchor = 'c')
    flightTree.column("4", width = 110, anchor = 'c')
    flightTree.column("5", width = 110, anchor = 'c')
    flightTree.column("6", width = 110, anchor = 'c')
    flightTree.column("7", width = 110, anchor = 'c')
    flightTree.column("8", width = 110, anchor = 'c')
    flightTree.column("9", width = 110, anchor = 'c')
    flightTree.column("10", width = 110, anchor = 'c')
    flightTree.column("11", width = 110, anchor = 'c')
    flightTree.column("12", width = 110, anchor = 'c')
    flightTree.column("13", width = 110, anchor = 'c')

    flightTree.heading("1", text = "% of Success")
    flightTree.heading("2", text = "Scheduled")
    flightTree.heading("3", text = "Performed")
    flightTree.heading("4", text = "Seats")
    flightTree.heading("5", text = "Passengers")
    flightTree.heading("6", text = "Distance (mi.)")
    flightTree.heading("7", text = "Carrier")
    flightTree.heading("8", text = "Origin")
    flightTree.heading("9", text = "Destination")
    flightTree.heading("10", text = "Aircraft")
    flightTree.heading("11", text = "Origin State")
    flightTree.heading("12", text = "Dest State")
    flightTree.heading("13", text = "Month")

    for flight in range(len(flightList)):
        flightTree.insert("", 'end', values = flightList[flight])
