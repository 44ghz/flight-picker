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

    critDistance = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # First page

    critCarrier = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # Second page

    critOriginCity = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # Third page

    critDestCity = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # Fourth page

    critAircraft = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # Fifth page

    critOriginState = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # Sixth page

    critDestState = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # Seventh page

    critMonth = ttk.Frame(criteriaTabs,
        width = 1440,
        height = 676)   # Eighth page

    criteriaTabs.add(critDistance, text = 'Distance')
    criteriaTabs.add(critCarrier, text = 'Carrier')
    criteriaTabs.add(critOriginCity, text = 'Origin City')
    criteriaTabs.add(critDestCity, text = 'Destination City')
    criteriaTabs.add(critAircraft, text = 'Aircraft')
    criteriaTabs.add(critOriginState, text = 'Origin State')
    criteriaTabs.add(critDestState, text = 'Destination State')
    criteriaTabs.add(critMonth, text = 'Month') # Add each of the criteria to the tabs frame
    criteriaTabs.grid(row = 0, column = 0)

    display_best(critDistance, listOfBests, 0)
    display_best(critCarrier, listOfBests, 1)
    display_best(critOriginCity, listOfBests, 2)
    display_best(critDestCity, listOfBests, 3)
    display_best(critAircraft, listOfBests, 4)
    display_best(critOriginState, listOfBests, 5)
    display_best(critDestState, listOfBests, 6)
    display_best(critMonth, listOfBests, 7)


def display_best(frame, listOfBests, desiredCriteria):
    critDict = {}
    critDict[0] = "distance (in miles)"
    critDict[1] = "carrier"
    critDict[2] = "origin city"
    critDict[3] = "destination city"
    critDict[4] = "aircraft"
    critDict[5] = "origin state"
    critDict[6] = "destination state"
    critDict[7] = "month"

    bestCriteria = tk.StringVar() # The output of the best month
    bestCriteriaName = listOfBests[desiredCriteria][0][0] # The best criteria name from the list of overall best things
    bestCriteriaRank = listOfBests[desiredCriteria][0][1][0] # The best criteria rank
    bestCriteriaPerc = listOfBests[desiredCriteria][0][1][1] # The best criteria percentage

    bestCriteria.set("The best " + critDict[desiredCriteria] + " to fly is: " + bestCriteriaName +
        "\nwith its average rank of: " + str(bestCriteriaRank) + " points" +
        "\nand its average percentage of: " + str(bestCriteriaPerc) + "%")

    bestCriteriaLabel = tk.Label(frame, textvariable = bestCriteria, bg = 'white', width = 75)
    bestCriteriaLabel.pack(side = 'top')
    #bestCriteriaLabel.grid(row = 0, column = 0, sticky = 'nw')

    criteriaTree = ttk.Treeview(frame)
    criteriaTree["columns"] = ("1", "2", "3")
    criteriaTree['show'] = 'headings'
    criteriaTree.column("1", width = 200, anchor = 'c')
    criteriaTree.column("2", width = 200, anchor = 'c')
    criteriaTree.column("3", width = 200, anchor = 'c')

    criteriaTree.heading("1", text = "Criteria")
    criteriaTree.heading("2", text = "Average Rank")
    criteriaTree.heading("3", text = "Average % of Success")

    criteriaTree.config(height = 12)

    criteriaTree.pack(side = 'top')
    #criteriaTree.grid(row = 0, column = 1)
    for option in range(len(listOfBests[desiredCriteria])): # For every option in the desired criteria
        criteriaTree.insert("", 'end', values =
            (listOfBests[desiredCriteria][option][0],
                listOfBests[desiredCriteria][option][1][0],
                    listOfBests[desiredCriteria][option][1][1]))
        # Insert into the tree: The month for the first column, the score for the second column, and the percentage for the third column

    flightTree = ttk.Treeview(frame)
    flightTree = configure_treeview(frame, flightTree)


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
