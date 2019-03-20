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

    fnfButton = tk.Button(text = "OK", command = win.destroy)
    fnfButton.pack()

def create_auto_tabs(frame, listOfBests):
    helvBold = font.Font(family = 'Helvetica', size = '11', weight = 'bold')
    criteriaTabs = ttk.Notebook(frame) # The pages used to tab through the criteria

    critMonth = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # First page

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

    criteriaTabs.add(critMonth, text = 'Month') # Add each of the criteria to the tabs frame
    criteriaTabs.add(critDistance, text = 'Distance')
    criteriaTabs.add(critCarrier, text = 'Carrier')
    criteriaTabs.add(critOriginCity, text = 'Origin City')
    criteriaTabs.add(critDestCity, text = 'Destination City')
    criteriaTabs.add(critAircraft, text = 'Aircraft')
    criteriaTabs.add(critOriginState, text = 'Origin State')
    criteriaTabs.add(critDestState, text = 'Destination State')
    criteriaTabs.grid(row = 0, column = 0)

    bestMonth = tk.StringVar() # The output of the best month
    bestMonthName = listOfBests[0][0][0] # The best month name from the list of overall best things
    bestMonthRank = listOfBests[0][0][1][0] # The best month rank
    bestMonthPerc = listOfBests[0][0][1][1] # The best month percentage

    bestMonth.set("The best month to fly is: " + bestMonthName +
        "\nwith its average rank of: " + bestMonthRank + " points" +
        "\nand its average percentage of: " + bestMonthPerc + "%")

    bestMonthLabel = tk.Label(critMonth, textvariable = bestMonth, bg = 'white', width = 75)
    bestMonthLabel.pack(side = 'top')
    #bestMonthLabel.grid(row = 0, column = 0, sticky = 'nw')

    monthTree = ttk.Treeview(critMonth)
    monthTree["columns"] = ("1", "2", "3")
    monthTree['show'] = 'headings'
    monthTree.column("1", width = 200, anchor = 'c')
    monthTree.column("2", width = 200, anchor = 'c')
    monthTree.column("3", width = 200, anchor = 'c')

    monthTree.heading("1", text = "Month")
    monthTree.heading("2", text = "Average Rank")
    monthTree.heading("3", text = "Average % of Success")

    monthTree.config(height = 12)

    monthTree.pack(side = 'top')
    #monthTree.grid(row = 0, column = 1)
    for month in range(len(listOfBests[0])): # For every month in the list of best flights
        monthTree.insert("", 'end', values = (listOfBests[0][month][0], listOfBests[0][month][1][0], listOfBests[0][month][1][1]))
        # Insert into the tree: The month for the first column, the score for the second column, and the percentage for the third column

    flightTree = ttk.Treeview(critMonth)
    flightTree = configure_treeview(critMonth, flightTree)

def create_manual_results_panel(frame, flightData):
    flightList = dr.convert_df(flightData)

    text = tk.Label(frame, text = "This panel will be for manual results")
    text.pack(side = 'top', fill = 'both', expand = 1)

    flightTree = ttk.Treeview(frame)
    flightTree = configure_treeview(frame, flightTree)

    for flight in range(len(flightList)): # Adding each flight to the tree view
        flightTree.insert("", 'end', values = flightList[flight])

def configure_treeview(frame, flightTree):
    flightTree.config(height = 20) # 33 for max height
    flightTree.pack(side = 'left', expand = 1)
    #flightTree.grid(row = 1, column = 0)

    treeScrollBar = ttk.Scrollbar(frame,
        orient = "vertical",
        command = flightTree.yview)
    treeScrollBar.pack(side = 'right', fill = 'y')
    #treeScrollBar.grid(row = 1, column = 2, sticky = 'e')

    flightTree.configure(yscrollcommand= treeScrollBar.set)

    flightTree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
    flightTree['show'] = 'headings'

    # Adding all columns
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

    # Adding all headings
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

    return flightTree
