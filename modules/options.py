import os                                # To change directories
import tkinter as tk                     # Standard Tkinter functions
from tkinter import font                 # For custom fonts
from modules import dataretrieval as dr  # Custom TKinter functions
from modules import tkfunctions as tf    # Custom data retrieval functions


################################################################################
#   FUNCTION NAME: create_options
#   DESCRIPTION: Creates the option boxes for use with manual mode. Includes formatting
#   PARAMETERS: optionsFrame    (tk.Frame): The Frame in which to display the options boxes
#   RETURN VALUES: comboBoxList (List[OptionsCombobox]): The list of comboboxes that correspond to user options
################################################################################
def create_options(optionsFrame):
    helvBold = font.Font(family = 'Helvetica', size = '11', weight = 'bold')

    comboBoxList = [] # List of the comboboxes used for options
    optionsList = get_options_lists() # Getting the options from files

    distanceList = optionsList[0]
    carrierList = optionsList[1]
    originList = optionsList[2]
    destinationList = optionsList[3]
    aircraftList = optionsList[4]
    stateOriginList = optionsList[5]
    stateDestinationList = optionsList[6]
    monthList = optionsList[7]


    ############################################################################

    # Distance selection menu
    distanceLabel = tk.Label(optionsFrame, text = "Distance (mi.)", font = helvBold)
    distanceLabel.grid(row = 1, column = 0, sticky = 'w', ipadx = 6)
    distanceMenu = tf.OptionsCombobox(optionsFrame, distanceList, 2, 0)
    comboBoxList.append(distanceMenu)

    # Carrier selection menu
    carrierLabel = tk.Label(optionsFrame, text = "\nCarrier", font = helvBold)
    carrierLabel.grid(row = 3, column = 0, sticky = 'w', ipadx = 6)
    carrierMenu = tf.OptionsCombobox(optionsFrame, carrierList, 4, 0)
    comboBoxList.append(carrierMenu)

    # Origin City selection menu
    originLabel = tk.Label(optionsFrame, text = "\nOrigin City", font = helvBold)
    originLabel.grid(row = 5, column = 0, sticky = 'w', ipadx = 6)
    originMenu = tf.OptionsCombobox(optionsFrame, originList, 6, 0)
    comboBoxList.append(originMenu)

    # Destination City selection menu
    destinationLabel = tk.Label(optionsFrame, text = "\nDestination City", font = helvBold)
    destinationLabel.grid(row = 7, column = 0, sticky = 'w', ipadx = 6)
    destinationMenu = tf.OptionsCombobox(optionsFrame, destinationList, 8, 0)
    comboBoxList.append(destinationMenu)

    # Aircraft selection menu
    aircraftLabel = tk.Label(optionsFrame, text = "\nAircraft", font = helvBold)
    aircraftLabel.grid(row = 9, column = 0, sticky = 'w', ipadx = 6)
    aircraftMenu = tf.OptionsCombobox(optionsFrame, aircraftList, 10, 0)
    comboBoxList.append(aircraftMenu)

    # State origin selection menu
    stateOriginLabel = tk.Label(optionsFrame, text = "\nOrigin State", font = helvBold)
    stateOriginLabel.grid(row = 11, column = 0, sticky = 'w', ipadx = 6)
    stateOriginMenu = tf.OptionsCombobox(optionsFrame, stateDestinationList, 12, 0)
    comboBoxList.append(stateOriginMenu)

    # State destination selection menu
    stateDestinationLabel = tk.Label(optionsFrame, text = "\nDestination State", font = helvBold)
    stateDestinationLabel.grid(row = 13, column = 0, sticky = 'w', ipadx = 6)
    stateDestinationMenu = tf.OptionsCombobox(optionsFrame, stateOriginList, 14, 0)
    comboBoxList.append(stateDestinationMenu)

    # Month selection menu
    monthLabel = tk.Label(optionsFrame, text = "\nMonth", font = helvBold)
    monthLabel.grid(row = 15, column = 0, sticky = 'w', ipadx = 6)
    monthMenu = tf.OptionsCombobox(optionsFrame, monthList, 16, 0)
    comboBoxList.append(monthMenu)

    ############################################################################


    # Creating a small space between the boxes and the separator
    buffer = tk.Frame(optionsFrame,
        height = 10,
        width = 135)

    buffer.grid(row = 17, column = 0)

    return comboBoxList


################################################################################
#   FUNCTION NAME: get_options_lists
#   DESCRIPTION: Reads the associated data files and returns a list with the unique options
#   PARAMETERS: none
#   RETURN VALUES: optionsList (List[List[String]]): A list of lists with unique options for every criterion
################################################################################
def get_options_lists():
    optionsList = [] # The list of lists for options

    # Reading in every list option from files
    optionsList.append(read_options("distances.dat"))
    optionsList.append(read_options("carriers.dat"))
    optionsList.append(read_options("origincities.dat"))
    optionsList.append(read_options("destinationcities.dat"))
    optionsList.append(read_options("aircraft.dat"))
    optionsList.append(read_options("originstates.dat"))
    optionsList.append(read_options("destinationstates.dat"))
    optionsList.append(read_options("months.dat"))

    return optionsList


################################################################################
#   FUNCTION NAME: update_options_lists
#   DESCRIPTION: Updates the unique options found in the intermediate .dat files
#   PARAMETERS: none
#   RETURN VALUES: none
################################################################################
def update_options_lists():
    # The columns that correspond to the rows
    CARRIER_COLUMN = 5
    ORIGIN_CITY_COLUMN = 6
    DESTINATION_CITY_COLUMN = 7
    AIRCRAFT_COLUMN = 8
    STATE_ORIGIN_COLUMN = 9
    STATE_DESTINATION_COLUMN = 10


    flightData = dr.open_data('ProjectData.csv') # Opening the .csv for data and converting to a DataFrame
    aircraftData = dr.open_data('AircraftNames.csv') # Converting the DataFrame to lists


    ############################################################################
    # Writing the options to the .dat files

    # Creating list for the distances
    distanceList = ["None", "0 - 99", "100 - 199", "200 - 299", "300 - 399", "400 - 499",
                    "500 - 999", "1000 - 1499", "1500 - 1999", "2000 - 2499", ">2500"]
    write_options(distanceList, "distances.dat")

    carrierList = dr.get_data(flightData, CARRIER_COLUMN) # Creating list for the carriers
    write_options(carrierList, "carriers.dat")

    originList = dr.get_data(flightData, ORIGIN_CITY_COLUMN) # Creating list for the origin cities
    write_options(originList, "origincities.dat")

    destinationList = dr.get_data(flightData, DESTINATION_CITY_COLUMN) # Creating list for the destination cities
    write_options(destinationList, "destinationcities.dat")

    aircraftList = sorted(dr.get_aircraft_names(aircraftData, dr.get_data(flightData, AIRCRAFT_COLUMN))) # Creating list for the aircraft
    aircraftList.insert(0, "None") # Adding None as an option to the start of the list
    write_options(aircraftList, "aircraft.dat")

    stateOriginList = dr.get_data(flightData, STATE_ORIGIN_COLUMN) # Creating list for state origins
    write_options(stateOriginList, "originstates.dat")

    stateDestinationList = dr.get_data(flightData, STATE_DESTINATION_COLUMN) # Creating list for state destinations
    write_options(stateDestinationList, "destinationstates.dat")

    # Creating list for months
    monthList = ["None", "January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November", "December"]
    write_options(monthList, "months.dat")


################################################################################
#   FUNCTION NAME: read_options
#   DESCRIPTION: Reads in options from the file specified and compiles them into a list to return
#   PARAMETERS: filename (String): The requested filename from which the options will come
#   RETURN VALUES: none
################################################################################
def read_options(filename):
    optionsList = []

    try:
        os.chdir('data/options') # Change to options folder
        with open(filename, 'r') as optionsFile:
            for option in optionsFile:
                currLine = option[:-1] # Get rid of the newline character
                optionsList.append(currLine) # Add it to the options list
        os.chdir('..') # Go back to the main dir
        os.chdir('..')
        return optionsList
    except FileNotFoundError: # If an options file is missing, or the options folder is missing
        update_options_lists()
        return read_options(filename) # Still want to return the options for that file


################################################################################
#   FUNCTION NAME: write_options
#   DESCRIPTION: Takes a list of options and writes them to a .dat file. Will likely
#                be more efficient than parsing through a .csv every time
#   PARAMETERS: filename    (String): The requested filename from which the options will come
#               optionsList (List[List[String]]): A list of lists with unique options for every criterion
#   RETURN VALUES: none
################################################################################
def write_options(optionsList, filename):
    try:
        os.chdir('data/options') # Change to options folder
        with open(filename, 'w') as file:
            for option in optionsList:
                file.write('%s\n' % option) # Adding each option to the file
        os.chdir('..') # Go back to the main dir
        os.chdir('..')
    except FileNotFoundError: # If the directory does not exist
        os.mkdir('data/options')
        write_options(optionsList, filename)

################################################################################
#   FUNCTION NAME: disable_options
#   DESCRIPTION: Disables the user options and the option buttons (reset and random).
#                User should not have access to these when not in Manual mode
#   PARAMETERS: comboBoxList (List[tk.Combobox]): The list of comboboxes to alter
#               resetButton  (tk.Button): A button to reset the user choices
#               randomButton (tk.Button): A button to randomize the user choices
#   RETURN VALUES: none
################################################################################
def disable_options(comboBoxList, resetButton, randomButton):
    for box in comboBoxList: # Disabling every box in the list
        box.disable()

    # Disabling both buttons
    resetButton.config(state = 'disabled')
    randomButton.config(state = 'disabled')


################################################################################
#   FUNCTION NAME: enable_options
#   DESCRIPTION: Enables the user options and the option buttons (reset and random).
#                Occurs when user selects Manual mode.
#   PARAMETERS: comboBoxList (List[tk.Combobox]): The list of comboboxes to alter
#               resetButton  (tk.Button): A button to reset the user choices
#               randomButton (tk.Button): A button to randomize the user choices
#   RETURN VALUES: none
################################################################################
def enable_options(comboBoxList, resetButton, randomButton):
    for box in comboBoxList: # Enabling every box in the list
        box.enable()

    # Enabling both buttons
    resetButton.config(state = 'normal')
    randomButton.config(state = 'normal')
