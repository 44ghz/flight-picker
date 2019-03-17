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
        tf.fileNotFoundPopup()

def create_options(frame):
    flightData = openData('ProjectData.csv')
    carrierData = openData('AircraftNames.csv')
    helvBold = font.Font(family = 'Helvetica', size = '11', weight = 'bold')

    distanceList = ["None", "0 - 100", "100 - 200", "200 - 300", "300 - 400", "400 - 499", "500 - 999", "1000 - 1499", "1500 - 1999", ">2000"]
    distanceDefault = tk.StringVar()
    distanceDefault.set("None")

    carrierList = dr.get_data(flightData, 6) # Creating list for the carriers
    carrierDefault = tk.StringVar()
    carrierDefault.set("None")

    originList = dr.get_data(flightData, 7) # Creating list for the origin cities
    originDefault = tk.StringVar()
    originDefault.set("None")

    destinationList = dr.get_data(flightData, 11) # Creating list for the destination cities
    destinationDefault = tk.StringVar()
    destinationDefault.set("None")

    aircraftList = dr.get_carrier_names(carrierData, dr.get_data(flightData, 16)) # Creating list for the aircraft
    aircraftDefault = tk.StringVar()
    aircraftDefault.set("None")

    stateList = [] # Creating list for the state
    stateDefault = tk.StringVar()
    stateDefault.set("None")

    monthList = ["None", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthDefault = tk.StringVar()
    monthDefault.set("None")

    ###################################

    # Distance selection menu
    distanceLabel = tk.Label(frame, text = "Distance", font = helvBold)
    distanceLabel.grid(row = 1, column = 0, sticky = 'w', ipadx = 8)
    distanceMenu = ttk.Combobox(frame, textvariable = distanceDefault, values = distanceList)
    distanceMenu.grid(row = 2, column = 0)
    distanceMenu.config(width = 13, justify = tk.LEFT)

    # Carrier selection menu
    carrierLabel = tk.Label(frame, text = "\nCarrier", font = helvBold)
    carrierLabel.grid(row = 3, column = 0, sticky = 'w', ipadx = 8)
    carrierMenu = ttk.Combobox(frame, textvariable = carrierDefault, values = carrierList)
    carrierMenu.grid(row = 4, column = 0)
    carrierMenu.config(width = 13, justify = tk.LEFT)

    # Origin City selection menu
    originLabel = tk.Label(frame, text = "\nOrigin City", font = helvBold)
    originLabel.grid(row = 5, column = 0, sticky = 'w', ipadx = 8)
    originMenu = ttk.Combobox(frame, textvariable = originDefault, values = originList)
    originMenu.grid(row = 6, column = 0)
    originMenu.config(width = 13, justify = tk.LEFT)

    # Destination City selection menu
    destinationLabel = tk.Label(frame, text = "\nDestination City", font = helvBold)
    destinationLabel.grid(row = 7, column = 0, sticky = 'w', ipadx = 8)
    destinationMenu = ttk.Combobox(frame, textvariable = destinationDefault, values = destinationList)
    destinationMenu.grid(row = 8, column = 0)
    destinationMenu.config(width = 13, justify = tk.LEFT)

    # Aircraft selection menu
    aircraftLabel = tk.Label(frame, text = "\nAircraft", font = helvBold)
    aircraftLabel.grid(row = 9, column = 0, sticky = 'w', ipadx = 8)
    aircraftMenu = ttk.Combobox(frame, textvariable = aircraftDefault, values = aircraftList)
    aircraftMenu.grid(row = 10, column = 0)
    aircraftMenu.config(width = 13, justify = tk.LEFT)

    # Month selection menu
    monthLabel = tk.Label(frame, text = "\nMonth", font = helvBold)
    monthLabel.grid(row = 11, column = 0, sticky = 'w', ipadx = 8)
    monthMenu = ttk.Combobox(frame, textvariable = monthDefault, values = monthList)
    monthMenu.grid(row = 12, column = 0)
    monthMenu.config(width = 13, justify = tk.LEFT)

    # State selection menu
    stateLabel = tk.Label(frame, text = "\nState", font = helvBold)
    stateLabel.grid(row = 13, column = 0, sticky = 'w', ipadx = 8)
    stateMenu = ttk.Combobox(frame, textvariable = stateDefault, values = stateList)
    stateMenu.grid(row = 14, column = 0)
    stateMenu.config(width = 13, justify = tk.LEFT)
