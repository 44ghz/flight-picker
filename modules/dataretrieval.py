import os                              # To change directories
import pandas as pd                    # For data tabulation of .csv's
from modules import tkfunctions as tf  # Custom TKinter functions


################################################################################
#   FUNCTION NAME: open_data
#   DESCRIPTION: Opens the csv and returns a pandas DataFrame with the data
#   PARAMETERS: filename (String): The requested filename from which the options will come
#   RETURN VALUES: flightData (pd.DataFrame): DataFrame with the data from .csv
################################################################################
def open_data(filename):
    try:
        os.chdir('data')                   # Change to the data directory
        flightData = pd.read_csv(filename) # Converting the .csv to a DataFrame
        os.chdir('..')                     # Changing back to the main directory
        return flightData
    except FileNotFoundError:
        tf.file_not_found()


################################################################################
#   FUNCTION NAME: data_exists
#   DESCRIPTION: Touches data files and ensures they exist before continuing with the creation of the
#                main window and execution of the program
#   PARAMETERS: none
#   RETURN VALUES: none
################################################################################
def data_exists():
    dataName =     "ProjectData.csv"
    aircraftName = "AircraftNames.csv"
    os.chdir('data')

    dataExists = os.path.isfile(dataName)
    aircraftNamesExist = os.path.isfile(aircraftName)

    os.chdir('..')  # Changing back to the main directory

    if dataExists and aircraftNamesExist: # If all data files exist then everything is fine
        return
    else: # If they're not all present, alert user and close the program
        tf.file_not_found()


################################################################################
#   FUNCTION NAME: get_data
#   DESCRIPTION: Gathering the data for the specified column (for all rows). Used for finding
#                the unique options available for criteria
#   PARAMETERS: flightData (pd.DataFrame): DataFrame with the data from .csv
#               column     (Integer): The corresponding column from which options are retrieved
#   RETURN VALUES: dataList (List): The list of options retrieved from the column
################################################################################
def get_data(flightData, column):
    rows = len(flightData.index) # The number of rows in the DataFrame
    dataList = []                # The list of data to retrieve

    for row in range(rows):
        dataList.append(str(flightData.iloc[row, column])) # Adding each datum to the list

    dataList = list(sorted(set(dataList))) # Creating a set of the data (to eliminate duplicates), then sorting it and making it a list
    dataList.insert(0, "None")             # Adding None as an option to the start of the list
    return dataList


################################################################################
#   FUNCTION NAME: get_aircraft_dict
#   DESCRIPTION: Generates a dict that has pairs of aircraft names that correspond to the aircraft codes.
#                Note: this is for all aircraft, not just for the ones found in the .csv
#   PARAMETERS: aircraftData (pd.DataFrame): DataFrame with aircraft codes and their names
#   RETURN VALUES: nameDict (Dict[]): DataFrame with the data from .csv
################################################################################
def get_aircraft_dict(aircraftData):
    rows = len(aircraftData.index) # The number of rows in the DataFrame
    nameDict = {}                  # The code accompanied by the name of the aircraft

    # For every row, match the name with the code
    for row in range(1, rows):
        currCode = str(aircraftData.iloc[row, 0]) # Aircraft code
        currName = str(aircraftData.iloc[row, 2]) # Aircraft name
        nameDict[currCode] = currName

    return nameDict


################################################################################
#   FUNCTION NAME: get_aircraft_names
#   DESCRIPTION: Converts the aircraft codes from the .csv and gather a list of their corresponding names
#   PARAMETERS: aircraftData (pd.DataFrame): DataFrame with aircraft codes and their names
#               aircraftList (List): List of aircraft codes
#   RETURN VALUES: aircraftNames (List[String]): List of aircraft names from the .csv
################################################################################
def get_aircraft_names(aircraftData, aircraftList):
    nameDict = get_aircraft_dict(aircraftData)

    aircraftCodes = len(aircraftList) # For every code found in the main data file
    aircraftNames = []                # The names found in the aircraft names file

    for code in range(aircraftCodes):
        if(aircraftList[code] in nameDict): # If the aircraft code from the main data file is found in the aircraft names file
            aircraftNames.append(nameDict[aircraftList[code]]) # Add it to the names list

    aircraftNames = list(set(aircraftNames)) # Creating a set of the data (to eliminate duplicates), then sorting it and making it a list
    return aircraftNames


################################################################################
#   FUNCTION NAME: convert_df
#   DESCRIPTION: Converts a DataFrame into a list of flights (rows). Replaces month numbers with month names,
#                and replaces aircraft codes with aircraft names instead
#   PARAMETERS: flightData (pd.DataFrame): DataFrame with the data from .csv
#   RETURN VALUES: flights (List): The list of flights that were converted from the DataFrame rows
################################################################################
def convert_df(flightData):
    COLUMNS = 12 # Number of relevant columns
    AIRCRAFT_COLUMN = 8

    aircraftData = open_data('AircraftNames.csv')

    nameDict = {}
    totalAircraftDict = get_aircraft_dict(aircraftData)

    aircraftList = get_data(flightData, AIRCRAFT_COLUMN)
    aircraftCodes = len(aircraftList) # For every code found in the main data file

    for code in range(aircraftCodes):
        # If the aircraft code from the main data file is found in the aircraft names file
        if(aircraftList[code] in totalAircraftDict):
            nameDict[aircraftList[code]] = totalAircraftDict[aircraftList[code]] # Add it to the names list

    # The months that correspond to each number
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

    flights = []                 # The list of lists containing information about every flight
    rows = len(flightData.index) # The number of rows in the DataFrame

    for row in range(rows):
        currentFlight = [] # Reset the current row
        for column in range(COLUMNS):
            currentFlight.append(flightData.iloc[row, column])             # Add the current cell to the current flight list
        currentFlight[AIRCRAFT_COLUMN] = nameDict[str(currentFlight[AIRCRAFT_COLUMN])] # Replace the aircraft code with the aircraft name
        currentFlight[COLUMNS - 1] = monthDict[currentFlight[COLUMNS - 1]] # Replace the month number with the month name
        flights.append(currentFlight)                                      # Add the new flight list to the list of flights

    return flights
