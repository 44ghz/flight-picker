import tkinter as tk
import os
import pandas as pd
from tkinter import font
from tkinter import ttk
from modules import dataretrieval as dr
from modules import tkfunctions as tf

def openData(filename):
    try:
        os.chdir('data')
        fileValues = pd.read_csv(filename)
        os.chdir('..')
        return fileValues
    except FileNotFoundError:
        tf.fnf_popup()

def create_options(frame):
    flightData = openData('ProjectData.csv')
    carrierData = openData('AircraftNames.csv')

    helvBold = font.Font(family = 'Helvetica', size = '11', weight = 'bold')

    distanceList = ["None", "0 - 100", "100 - 200", "200 - 300", "300 - 400", "400 - 499", "500 - 999", "1000 - 1499", "1500 - 1999", ">2000"]
    carrierList = dr.get_data(flightData, 6) # Creating list for the carriers
    originList = dr.get_data(flightData, 7) # Creating list for the origin cities
    destinationList = dr.get_data(flightData, 11) # Creating list for the destination cities
    aircraftList = dr.get_carrier_names(carrierData, dr.get_data(flightData, 16)) # Creating list for the aircraft
    stateList = [] # Creating list for the state
    monthList = ["None", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    ###################################

    # Distance selection menu
    distanceLabel = tk.Label(frame, text = "Distance", font = helvBold)
    distanceLabel.grid(row = 1, column = 0, sticky = 'w', ipadx = 5)
    distanceMenu = tf.OptionsCombobox(frame, distanceList, 2, 0)

    # Carrier selection menu
    carrierLabel = tk.Label(frame, text = "\nCarrier", font = helvBold)
    carrierLabel.grid(row = 3, column = 0, sticky = 'w', ipadx = 5)
    carrierMenu = tf.OptionsCombobox(frame, carrierList, 4, 0)

    # Origin City selection menu
    originLabel = tk.Label(frame, text = "\nOrigin City", font = helvBold)
    originLabel.grid(row = 5, column = 0, sticky = 'w', ipadx = 5)
    originMenu = tf.OptionsCombobox(frame, originList, 6, 0)

    # Destination City selection menu
    destinationLabel = tk.Label(frame, text = "\nDestination City", font = helvBold)
    destinationLabel.grid(row = 7, column = 0, sticky = 'w', ipadx = 5)
    destinationMenu = tf.OptionsCombobox(frame, destinationList, 8, 0)

    # Aircraft selection menu
    aircraftLabel = tk.Label(frame, text = "\nAircraft", font = helvBold)
    aircraftLabel.grid(row = 9, column = 0, sticky = 'w', ipadx = 5)
    aircraftMenu = tf.OptionsCombobox(frame, aircraftList, 10, 0)

    # Month selection menu
    monthLabel = tk.Label(frame, text = "\nMonth", font = helvBold)
    monthLabel.grid(row = 11, column = 0, sticky = 'w', ipadx = 5)
    monthMenu = tf.OptionsCombobox(frame, monthList, 12, 0)

    # State selection menu
    stateLabel = tk.Label(frame, text = "\nState", font = helvBold)
    stateLabel.grid(row = 13, column = 0, sticky = 'w', ipadx = 5)
    stateMenu = tf.OptionsCombobox(frame, stateList, 14, 0)
