import tkinter as tk # Main GUI capabilities
from tkinter import ttk # Various other tkinter widgets (mainly combobox)
from tkinter import Scrollbar
from modules import dataretrieval as dr

def convert_df(df):
    COLUMNS = 12 # Number of relevant columns
    # AIRCRAFT_COLUMN = 8
    #
    # aircraftData = dr.open_data('AircraftNames.csv')
    # aircraftList = dr.get_data(df, AIRCRAFT_COLUMN)
    # aircraftList.pop(0)
    # print(aircraftList)
    # aircraftNames = dr.get_aircraft_names(aircraftData, aircraftList)
    #
    # aircraftDict = {}
    #
    # currAircraft = 0
    # for aircraft in aircraftList:
    #     aircraftDict[aircraft] = aircraftNames[currAircraft]
    #     currAircraft += 1

    monthDict = {}
    monthDict[1] = "January"
    monthDict[2] = "February"
    monthDict[3] = "March"
    monthDict[4] = "April"
    monthDict[5] = "May"
    monthDict[6] = "June"
    monthDict[7] = "July"
    monthDict[8] = "August"
    monthDict[9] = "September"
    monthDict[10] = "October"
    monthDict[11] = "November"
    monthDict[12] = "December"

    flights = [] # The list of lists containing information about every flight
    rows = len(df.index) # The number of rows in the DataFrame

    for row in range(rows):
        currentFlight = [] # Reset the current row
        currentFlight.append("")
        for column in range(COLUMNS):
            currentFlight.append(df.iloc[row, column]) # Add the current cell to the current flight list
        #currentFlight[AIRCRAFT_COLUMN] =
        currentFlight[COLUMNS] = monthDict[currentFlight[COLUMNS]] # Replace the month number with the month name
        flights.append(currentFlight) # Add the new flight list to the list of flights

    return flights

def create_results(frame, flights):
    flightTree = ttk.Treeview(frame)
    flightTree.config(height = 33)
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

    for flight in range(len(flights)):
        flightTree.insert("", 'end', values = flights[flight])
