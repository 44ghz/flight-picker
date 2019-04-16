import os
import tkinter as tk
import pandas as pd
from tkinter import font
from modules import dataretrieval as dr
from modules import tkfunctions as tf

def create_options(leftFrame):
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

    ###################################

    # Distance selection menu
    distanceLabel = tk.Label(leftFrame, text = "Distance (mi.)", font = helvBold)
    distanceLabel.grid(row = 1, column = 0, sticky = 'w', ipadx = 6)
    distanceMenu = tf.OptionsCombobox(leftFrame, distanceList, 2, 0)
    comboBoxList.append(distanceMenu)

    # Carrier selection menu
    carrierLabel = tk.Label(leftFrame, text = "\nCarrier", font = helvBold)
    carrierLabel.grid(row = 3, column = 0, sticky = 'w', ipadx = 6)
    carrierMenu = tf.OptionsCombobox(leftFrame, carrierList, 4, 0)
    comboBoxList.append(carrierMenu)

    # Origin City selection menu
    originLabel = tk.Label(leftFrame, text = "\nOrigin City", font = helvBold)
    originLabel.grid(row = 5, column = 0, sticky = 'w', ipadx = 6)
    originMenu = tf.OptionsCombobox(leftFrame, originList, 6, 0)
    comboBoxList.append(originMenu)

    # Destination City selection menu
    destinationLabel = tk.Label(leftFrame, text = "\nDestination City", font = helvBold)
    destinationLabel.grid(row = 7, column = 0, sticky = 'w', ipadx = 6)
    destinationMenu = tf.OptionsCombobox(leftFrame, destinationList, 8, 0)
    comboBoxList.append(destinationMenu)

    # Aircraft selection menu
    aircraftLabel = tk.Label(leftFrame, text = "\nAircraft", font = helvBold)
    aircraftLabel.grid(row = 9, column = 0, sticky = 'w', ipadx = 6)
    aircraftMenu = tf.OptionsCombobox(leftFrame, aircraftList, 10, 0)
    comboBoxList.append(aircraftMenu)

    # State origin selection menu
    stateOriginLabel = tk.Label(leftFrame, text = "\nState Origin", font = helvBold)
    stateOriginLabel.grid(row = 11, column = 0, sticky = 'w', ipadx = 6)
    stateOriginMenu = tf.OptionsCombobox(leftFrame, stateDestinationList, 12, 0)
    comboBoxList.append(stateOriginMenu)

    # State destination selection menu
    stateDestinationLabel = tk.Label(leftFrame, text = "\nState Destination", font = helvBold)
    stateDestinationLabel.grid(row = 13, column = 0, sticky = 'w', ipadx = 6)
    stateDestinationMenu = tf.OptionsCombobox(leftFrame, stateOriginList, 14, 0)
    comboBoxList.append(stateDestinationMenu)

    # Month selection menu
    monthLabel = tk.Label(leftFrame, text = "\nMonth", font = helvBold)
    monthLabel.grid(row = 15, column = 0, sticky = 'w', ipadx = 6)
    monthMenu = tf.OptionsCombobox(leftFrame, monthList, 16, 0)
    comboBoxList.append(monthMenu)

    buffer = tk.Frame(leftFrame,
        height = 10,
        width = 135)

    buffer.grid(row = 17, column = 0)

    return comboBoxList


def get_options_lists():
    optionsList = [] # The list of lists for options

    # Reading in every list option from files
    optionsList.append(read_options("distances.dat"))
    optionsList.append(read_options("carriers.dat"))
    optionsList.append(read_options("origincities.dat"))
    optionsList.append(read_options("destinationcities.dat"))
    optionsList.append(read_options("aircraft.dat"))
    optionsList.append(read_options("stateorigins.dat"))
    optionsList.append(read_options("statedestinations.dat"))
    optionsList.append(read_options("months.dat"))

    return optionsList


def update_options_lists(flightData):
    CARRIER_COLUMN = 5
    ORIGIN_CITY_COLUMN = 6
    DESTINATION_CITY_COLUMN = 7
    AIRCRAFT_COLUMN = 8
    STATE_ORIGIN_COLUMN = 9
    STATE_DESTINATION_COLUMN = 10

    aircraftData = dr.open_data('AircraftNames.csv')

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
    write_options(stateOriginList, "stateorigins.dat")

    stateDestinationList = dr.get_data(flightData, STATE_DESTINATION_COLUMN) # Creating list for state destinations
    write_options(stateDestinationList, "statedestinations.dat")

    monthList = ["None", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    write_options(monthList, "months.dat")


def read_options(filename):
    optionList = []

    try:
        os.chdir('data/options') # Change to options folder
        with open(filename, 'r') as optionsFile:
            for option in optionsFile:
                currLine = option[:-1] # Get rid of the newline character
                optionList.append(currLine) # Add it to the options list
        os.chdir('..') # Go back to the main dir
        os.chdir('..')
        return optionList
    except FileNotFoundError:
        tf.fnf_popup()


def write_options(optionList, filename):
    os.chdir('data/options') # Change to options folder
    with open(filename, 'w') as file:
        for option in optionList:
            file.write('%s\n' % option) # Adding each option to its file
    os.chdir('..') # Go back to the main dir
    os.chdir('..')


def disable_options(comboBoxList):
    for box in range(len(comboBoxList)):
        comboBoxList[box].disable()


def enable_options(comboBoxList):
    for box in range(len(comboBoxList)):
        comboBoxList[box].enable()
