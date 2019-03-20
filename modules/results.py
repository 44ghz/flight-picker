import tkinter as tk # Main GUI capabilities
from modules import dataretrieval as dr
from modules import options as op
from modules import tkfunctions as tf

def find_flights(mode, frame, flightData):
    if(mode.get() == 1):
        automatic(frame, flightData)
    else:
        manual(frame, flightData)

def automatic(frame, flightData):
    DIST_COLUMN = 5 # The columns that correspond to the flight dataframe
    CARRIER_COLUMN = 6
    ORIGIN_COLUMN = 7
    DEST_COLUMN = 8
    AIRCRAFT_COLUMN = 9
    OR_STATE_COLUMN = 10
    DEST_STATE_COLUMN = 11
    MONTH_COLUMN = 12

    flightsForDistance = {} # Use predetermined ranges
    flightsForCarrier = {}
    flightsForOriginCity = {}
    flightsForDestCity = {}
    flightsForAircraft = {}
    flightsForOrState = {}
    flightsForDestState = {}
    flightsForMonth = {}

    flightList = dr.convert_df(flightData)
    optionsList = op.get_options_lists(flightData)

    # Taking each unique option from the options lists and creating the key values for each dictionary
    for carrier in optionsList[1]:
        flightsForCarrier[carrier] = [] # Each value for the keys will be a list, which will then have lists inside (aka flights)

    for origin in optionsList[2]:
        flightsForOriginCity[origin] = []

    for destination in optionsList[3]:
        flightsForDestCity[destination] = []

    for aircraft in optionsList[4]:
        flightsForAircraft[aircraft] = []

    for originState in optionsList[5]:
        flightsForOrState[originState] = []

    for destState in optionsList[6]:
        flightsForDestState[destState] = []

    for month in optionsList[7]:
        flightsForMonth[month] = []

    for currFlight in range(len(flightList)): # For every flight in the list, categorize it to each dict
        currentFlight = flightList[currFlight]
        flightsForCarrier[flightList[currFlight][CARRIER_COLUMN]].append(currentFlight)
        flightsForOriginCity[currentFlight[ORIGIN_COLUMN]].append(currentFlight)
        flightsForDestCity[currentFlight[DEST_COLUMN]].append(currentFlight)
        flightsForAircraft[currentFlight[AIRCRAFT_COLUMN]].append(currentFlight)
        flightsForOrState[currentFlight[OR_STATE_COLUMN]].append(currentFlight)
        flightsForDestState[currentFlight[DEST_STATE_COLUMN]].append(currentFlight)
        flightsForMonth[currentFlight[MONTH_COLUMN]].append(currentFlight)

    tf.create_auto_tabs(frame)

def manual(frame, flightData):
    tf.create_manual_results_panel(frame, flightData)
