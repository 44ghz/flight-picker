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
    SCHEDULED_COLUMN = 1
    PERFORMED_COLUMN = 2
    SEATS_COLUMN = 3
    PASSEN_COLUMN = 4
    # DIST_COLUMN = 5 # The columns that correspond to the flight dataframe
    # CARRIER_COLUMN = 6
    # ORIGIN_COLUMN = 7
    # DEST_COLUMN = 8
    # AIRCRAFT_COLUMN = 9
    # OR_STATE_COLUMN = 10
    # DEST_STATE_COLUMN = 11
    MONTH_COLUMN = 12

    # TODO: categorize a flight's distance
    # flightsForDistance = {} # Use predetermined ranges
    # flightsForCarrier = {}
    # flightsForOriginCity = {}
    # flightsForDestCity = {}
    # flightsForAircraft = {}
    # flightsForOrState = {}
    # flightsForDestState = {}
    flightsForMonth = {}
    percForMonth = {}


    flightList = dr.convert_df(flightData)
    optionsList = op.get_options_lists()

    # Taking each unique option from the options lists and creating the key values for each dictionary
    # for carrier in optionsList[1]:
    #     flightsForCarrier[carrier] = [] # Each value for the keys will be a list, which will then have lists inside (aka flights)
    #
    # for origin in optionsList[2]:
    #     flightsForOriginCity[origin] = []
    #
    # for destination in optionsList[3]:
    #     flightsForDestCity[destination] = []
    #
    # for aircraft in optionsList[4]:
    #     flightsForAircraft[aircraft] = []
    #
    # for originState in optionsList[5]:
    #     flightsForOrState[originState] = []
    #
    # for destState in optionsList[6]:
    #     flightsForDestState[destState] = []

    for month in optionsList[7]:
        flightsForMonth[month] = []

    for currFlight in range(len(flightList)): # For every flight in the list, categorize it to each dict
        currentFlight = flightList[currFlight]
        #flightsForCarrier[flightList[currFlight][CARRIER_COLUMN]].append(currentFlight)
        #flightsForOriginCity[currentFlight[ORIGIN_COLUMN]].append(currentFlight)
        #flightsForDestCity[currentFlight[DEST_COLUMN]].append(currentFlight)
        #flightsForAircraft[currentFlight[AIRCRAFT_COLUMN]].append(currentFlight)
        #flightsForOrState[currentFlight[OR_STATE_COLUMN]].append(currentFlight)
        #flightsForDestState[currentFlight[DEST_STATE_COLUMN]].append(currentFlight)
        flightsForMonth[currentFlight[MONTH_COLUMN]].append(currentFlight)

    listOfBests = [] # The overall list of best things

    for month in flightsForMonth:
        comboList = []
        totalPerc = 0 # Reset the total and count for the new month
        count = 0 # The number of flights
        totalRank = 0 # The total ranks for the month
        currMonth = flightsForMonth[month] # Get all the flights for the current month

        for flight in range(len(currMonth)):
            rank = 0
            currPercent = round(currMonth[flight][PERFORMED_COLUMN] # Get the flights performed and flights scheduled
                / currMonth[flight][SCHEDULED_COLUMN] * 100, 2)
            if(currPercent > 100): # Check for percentages above 100, as these can skew the results
                currPercent = 100.00 # Just change to 100

            # For rank, take the percent from above and multiply it by the number of available seats
            rank = (currPercent) * (currMonth[flight][SEATS_COLUMN] - currMonth[flight][PASSEN_COLUMN])
            totalRank += rank # Updating the total score for the month
            totalPerc += currPercent # Updating the total percentages
            count += 1.0 # Updating the number of flights

        if(count == 0): # To avoid a divbyzero exception
            continue

        monthRank = str(round(totalRank / count, 2)) # Get the average rank for the month
        monthAverage = str(round(totalPerc / count, 2)) # Get the average percentage for the month
        comboList.append(monthRank)
        comboList.append(monthAverage)
        percForMonth[month] = comboList # Add that to a dict of averages for the months

    percForMonth = sorted(percForMonth.items(), key = lambda kv: kv[1], reverse = True) # Sort the months by their ranks
    listOfBests.append(percForMonth) # Add it to the list of best things

    tf.create_auto_tabs(frame, listOfBests) # Create the tabs to display data

def manual(frame, flightData):
    tf.create_manual_results_panel(frame, flightData)
