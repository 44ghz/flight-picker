import os
import pandas as pd
from modules import tkfunctions as tf

def open_data(filename):
    try:
        os.chdir('data')
        fileValues = pd.read_csv(filename)
        os.chdir('..')
        return fileValues
    except FileNotFoundError:
        tf.fnf_popup()


def get_data(flightData, column):
    rows = len(flightData.index) # The number of rows in the DataFrame
    dataList = [] # The list of data to retrieve

    for row in range(rows):
        dataList.append(str(flightData.iloc[row, column])) # Adding each datum to the list

    dataList = list(sorted(set(dataList))) # Creating a set of the data (to eliminate duplicates), then sorting it and making it a list
    dataList.insert(0, "None") # Adding None as an option to the start of the list
    return dataList


def get_aircraft_dict(aircraftData):
    rows = len(aircraftData.index) # The number of rows in the DataFrame
    nameDict = {} # The code accompanied by the name of the aircraft

    for row in range(1, rows):
        currCode = str(aircraftData.iloc[row, 0]) # Aircraft code
        currName = str(aircraftData.iloc[row, 2]) # Aircraft name
        nameDict[currCode] = currName

    return nameDict


def get_aircraft_names(aircraftData, aircraftList):
    nameDict = get_aircraft_dict(aircraftData)

    aircraftCodes = len(aircraftList) # For every code found in the main data file
    aircraftNames = [] # The names found in the aircraft names file

    for code in range(aircraftCodes):
        if(aircraftList[code] in nameDict): # If the aircraft code from the main data file is found in the aircraft names file
            aircraftNames.append(nameDict[aircraftList[code]]) # Add it to the names list

    aircraftNames = list(set(aircraftNames)) # Creating a set of the data (to eliminate duplicates), then sorting it and making it a list
    return aircraftNames


def convert_df(flightData):
    COLUMNS = 12 # Number of relevant columns
    AIRCRAFT_COLUMN = 8

    aircraftData = open_data('AircraftNames.csv')

    nameDict = {}
    totalAircraftDict = get_aircraft_dict(aircraftData)

    aircraftList = get_data(flightData, AIRCRAFT_COLUMN)
    aircraftCodes = len(aircraftList) # For every code found in the main data file

    for code in range(aircraftCodes):
        if(aircraftList[code] in totalAircraftDict): # If the aircraft code from the main data file is found in the aircraft names file
            nameDict[aircraftList[code]] = totalAircraftDict[aircraftList[code]] # Add it to the names list

    monthDict = {} # The months that correspond to each number
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
    rows = len(flightData.index) # The number of rows in the DataFrame

    for row in range(rows):
        currentFlight = [] # Reset the current row
        #currentFlight.append("")
        for column in range(COLUMNS):
            currentFlight.append(flightData.iloc[row, column]) # Add the current cell to the current flight list
        currentFlight[AIRCRAFT_COLUMN] = nameDict[str(currentFlight[AIRCRAFT_COLUMN])] # Replace the aircraft code with the aircraft name
        currentFlight[COLUMNS - 1] = monthDict[currentFlight[COLUMNS - 1]] # Replace the month number with the month name
        flights.append(currentFlight) # Add the new flight list to the list of flights

    return flights
