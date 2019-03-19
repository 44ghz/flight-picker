import tkinter as tk
import pandas as pd
from tkinter import font
from modules import dataretrieval as dr
from modules import tkfunctions as tf

def create_options(leftFrame, flightData):
    CARRIER_COLUMN = 5
    ORIGIN_CITY_COLUMN = 6
    DESTINATION_CITY_COLUMN = 7
    AIRCRAFT_COLUMN = 8
    STATE_ORIGIN_COLUMN = 9
    STATE_DESTINATION_COLUMN = 10

    aircraftData = dr.open_data('AircraftNames.csv')

    helvBold = font.Font(family = 'Helvetica', size = '11', weight = 'bold')

    distanceList = ["None", "0 - 100", "100 - 200", "200 - 300", "300 - 400", "400 - 499", "500 - 999", "1000 - 1499", "1500 - 1999", ">2000"]
    carrierList = dr.get_data(flightData, CARRIER_COLUMN) # Creating list for the carriers
    originList = dr.get_data(flightData, ORIGIN_CITY_COLUMN) # Creating list for the origin cities
    destinationList = dr.get_data(flightData, DESTINATION_CITY_COLUMN) # Creating list for the destination cities

    aircraftList = sorted(dr.get_aircraft_names(aircraftData, dr.get_data(flightData, AIRCRAFT_COLUMN))) # Creating list for the aircraft
    aircraftList.insert(0, "None") # Adding None as an option to the start of the list

    stateOriginList = dr.get_data(flightData, STATE_ORIGIN_COLUMN) # Creating list for state origins
    stateDestinationList = dr.get_data(flightData, STATE_DESTINATION_COLUMN) # Creating list for state destinations
    monthList = ["None", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

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
