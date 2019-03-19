import os
import pandas as pd

def open_data(filename):
    try:
        os.chdir('data')
        fileValues = pd.read_csv(filename)
        os.chdir('..')
        return fileValues
    except FileNotFoundError:
        tf.fnf_popup()

def get_data(df, column):
    rows = len(df.index) # The number of rows in the DataFrame
    dataList = [] # The list of data to retrieve

    for row in range(rows):
        dataList.append(str(df.iloc[row, column])) # Adding each datum to the list

    dataList = list(sorted(set(dataList))) # Creating a set of the data (to eliminate duplicates), then sorting it and making it a list
    dataList.insert(0, "None") # Adding None as an option to the start of the list
    return dataList

def get_aircraft_names(df, aircraftList):
    rows = len(df.index) # The number of rows in the DataFrame
    nameDict = {} # The code accompanied by the name of the aircraft

    for row in range(1, rows):
        currCode = str(df.iloc[row, 0]) # Aircraft code
        currName = str(df.iloc[row, 2]) # Aircraft name
        nameDict[currCode] = currName

    aircraftCodes = len(aircraftList) # For every code found in the main data file
    aircraftNames = [] # The names found in the aircraft names file

    for code in range(aircraftCodes):
        if(aircraftList[code] in nameDict): # If the aircraft code from the main data file is found in the aircraft names file
            aircraftNames.append(nameDict[aircraftList[code]]) # Add it to the names list

    aircraftNames = list(set(aircraftNames)) # Creating a set of the data (to eliminate duplicates), then sorting it and making it a list
    return aircraftNames
