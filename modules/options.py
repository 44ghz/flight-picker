import os
import tkinter as tk
import pandas as pd
from tkinter import font
from modules import dataretrieval as dr
from modules import tkfunctions as tf

def get_options_lists():
    optionsList = [] # The list of lists for options
    # Reading in every list option from files
    optionsList.append(dr.read_options("distances.dat"))
    optionsList.append(dr.read_options("carriers.dat"))
    optionsList.append(dr.read_options("origincities.dat"))
    optionsList.append(dr.read_options("destinationcities.dat"))
    optionsList.append(dr.read_options("aircraft.dat"))
    optionsList.append(dr.read_options("stateorigins.dat"))
    optionsList.append(dr.read_options("statedestinations.dat"))
    optionsList.append(dr.read_options("months.dat"))

    return optionsList


def create_options(leftFrame):
    helvBold = font.Font(family = 'Helvetica', size = '11', weight = 'bold')

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

    # Carrier selection menu
    carrierLabel = tk.Label(leftFrame, text = "\nCarrier", font = helvBold)
    carrierLabel.grid(row = 3, column = 0, sticky = 'w', ipadx = 6)
    carrierMenu = tf.OptionsCombobox(leftFrame, carrierList, 4, 0)

    # Origin City selection menu
    originLabel = tk.Label(leftFrame, text = "\nOrigin City", font = helvBold)
    originLabel.grid(row = 5, column = 0, sticky = 'w', ipadx = 6)
    originMenu = tf.OptionsCombobox(leftFrame, originList, 6, 0)

    # Destination City selection menu
    destinationLabel = tk.Label(leftFrame, text = "\nDestination City", font = helvBold)
    destinationLabel.grid(row = 7, column = 0, sticky = 'w', ipadx = 6)
    destinationMenu = tf.OptionsCombobox(leftFrame, destinationList, 8, 0)

    # Aircraft selection menu
    aircraftLabel = tk.Label(leftFrame, text = "\nAircraft", font = helvBold)
    aircraftLabel.grid(row = 9, column = 0, sticky = 'w', ipadx = 6)
    aircraftMenu = tf.OptionsCombobox(leftFrame, aircraftList, 10, 0)

    # Month selection menu
    monthLabel = tk.Label(leftFrame, text = "\nMonth", font = helvBold)
    monthLabel.grid(row = 11, column = 0, sticky = 'w', ipadx = 6)
    monthMenu = tf.OptionsCombobox(leftFrame, monthList, 12, 0)

    # State origin selection menu
    stateOriginLabel = tk.Label(leftFrame, text = "\nState Origin", font = helvBold)
    stateOriginLabel.grid(row = 13, column = 0, sticky = 'w', ipadx = 6)
    stateOriginMenu = tf.OptionsCombobox(leftFrame, stateDestinationList, 14, 0)

    # State destination selection menu
    stateDestinationLabel = tk.Label(leftFrame, text = "\nState Destination", font = helvBold)
    stateDestinationLabel.grid(row = 15, column = 0, sticky = 'w', ipadx = 6)
    stateDestinationMenu = tf.OptionsCombobox(leftFrame, stateOriginList, 16, 0)


def update_options_lists(flightData):
    optionsList = []

    CARRIER_COLUMN = 5
    ORIGIN_CITY_COLUMN = 6
    DESTINATION_CITY_COLUMN = 7
    AIRCRAFT_COLUMN = 8
    STATE_ORIGIN_COLUMN = 9
    STATE_DESTINATION_COLUMN = 10

    aircraftData = dr.open_data('AircraftNames.csv')

    distanceList = ["None", "0 - 99", "100 - 199", "200 - 299", "300 - 399", "400 - 499",
        "500 - 999", "1000 - 1499", "1500 - 1999", "2000 - 2499", ">2500"]
    dr.write_options(distanceList, "distances.dat")
    optionsList.append(distanceList)

    carrierList = dr.get_data(flightData, CARRIER_COLUMN) # Creating list for the carriers
    dr.write_options(carrierList, "carriers.dat")
    optionsList.append(carrierList)

    originList = dr.get_data(flightData, ORIGIN_CITY_COLUMN) # Creating list for the origin cities
    dr.write_options(originList, "origincities.dat")
    optionsList.append(originList)

    destinationList = dr.get_data(flightData, DESTINATION_CITY_COLUMN) # Creating list for the destination cities
    dr.write_options(destinationList, "destinationcities.dat")
    optionsList.append(destinationList)

    aircraftList = sorted(dr.get_aircraft_names(aircraftData, dr.get_data(flightData, AIRCRAFT_COLUMN))) # Creating list for the aircraft
    aircraftList.insert(0, "None") # Adding None as an option to the start of the list
    dr.write_options(aircraftList, "aircraft.dat")
    optionsList.append(aircraftList)

    stateOriginList = dr.get_data(flightData, STATE_ORIGIN_COLUMN) # Creating list for state origins
    dr.write_options(stateOriginList, "stateorigins.dat")
    optionsList.append(stateOriginList)

    stateDestinationList = dr.get_data(flightData, STATE_DESTINATION_COLUMN) # Creating list for state destinations
    dr.write_options(stateDestinationList, "statedestinations.dat")
    optionsList.append(stateDestinationList)

    monthList = ["None", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    dr.write_options(monthList, "months.dat")
    optionsList.append(monthList)

    return optionsList
