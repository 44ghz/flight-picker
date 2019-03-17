import pandas as pd

def get_data(df, column):
    rows = len(df.index) # The number of rows in the DataFrame
    dataList = [] # The list of data to retrieve

    for row in range(1, rows):
        dataList.append(str(df.iloc[row, column])) # Adding each datum to the list

    dataList = list(sorted(set(dataList))) # Creating a set of the data (to eliminate duplicates), then sorting it and making it a list
    dataList.insert(0, "None") # Adding None as an option to the start of the list
    return dataList

def get_carrier_names(df, carrierList):
    rows = len(df.index) # The number of rows in the DataFrame
    nameDict = {} # The code accompanied by the name of the aircraft

    for row in range(1, rows):
        currCode = str(df.iloc[row, 0]) # Aircraft code
        currName = str(df.iloc[row, 2]) # Aircraft name
        nameDict[currCode] = currName

    carrierCodes = len(carrierList) # For every code found in the main data file
    carrierNames = [] # The names found in the aircraft names file

    for code in range(1, carrierCodes):
        if(carrierList[code] in nameDict): # If the aircraft code from the main data file is found in the aircraft names file
            carrierNames.append(nameDict[carrierList[code]]) # Add it to the names list

    carrierNames = list(sorted(set(carrierNames))) # Creating a set of the data (to eliminate duplicates), then sorting it and making it a list
    carrierNames.insert(0, "None") # Adding None as an option to the start of the list
    return carrierNames
