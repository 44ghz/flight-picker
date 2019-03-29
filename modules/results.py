import tkinter as tk # Main GUI capabilities
import operator
from modules import dataretrieval as dr
from modules import options as op
from modules import tkfunctions as tf

def find_flights(mode, frame, flightData):
    if(mode.get() == 1):
        automatic(frame, flightData)
    else:
        manual(frame, flightData)

def automatic(frame, flightData):
    # DIST_COLUMN = 5 # The columns that correspond to the flight dataframe
    CARRIER_COLUMN = 6
    ORIGIN_COLUMN = 7
    DEST_COLUMN = 8
    AIRCRAFT_COLUMN = 9
    OR_STATE_COLUMN = 10
    DEST_STATE_COLUMN = 11
    MONTH_COLUMN = 12

    #TODO: categorize a flight's distance
    #flightsForDistance = {} # Use predetermined ranges
    flightsForCarrier = {}
    flightsForOriginCity = {}
    flightsForDestCity = {}
    flightsForAircraft = {}
    flightsForOriginState = {}
    flightsForDestState = {}
    flightsForMonth = {}
    percForMonth = {}

    flightList = dr.convert_df(flightData)
    optionsList = op.get_options_lists()

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
        flightsForOriginState[originState] = []

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
        flightsForOriginState[currentFlight[OR_STATE_COLUMN]].append(currentFlight)
        flightsForDestState[currentFlight[DEST_STATE_COLUMN]].append(currentFlight)
        flightsForMonth[currentFlight[MONTH_COLUMN]].append(currentFlight)

    listOfBests = [] # The overall list of best things

    percForCarrier = find_best(flightsForCarrier)
    percForOriginCity = find_best(flightsForOriginCity)
    percForDestCity = find_best(flightsForDestCity)
    percForAircraft = find_best(flightsForAircraft)
    percForOriginState = find_best(flightsForOriginState)
    percForDestState = find_best(flightsForDestState)
    percForMonth = find_best(flightsForMonth)

    listOfBests.append(percForCarrier)
    listOfBests.append(percForOriginCity)
    listOfBests.append(percForDestCity)
    listOfBests.append(percForAircraft)
    listOfBests.append(percForOriginState)
    listOfBests.append(percForDestState)
    listOfBests.append(percForMonth) # Add it to the list of best things

    tf.create_auto_tabs(frame, listOfBests) # Create the tabs to display data

def manual(frame, flightData):
    tf.create_manual_results_panel(frame, flightData)

def find_best(critList):
    SCHEDULED_COLUMN = 1
    PERFORMED_COLUMN = 2
    SEATS_COLUMN = 3
    PASSEN_COLUMN = 4

    percForCrit = {}

    for crit in critList:
        comboList = []
        count = 0 # The number of flights
        totalPerc = 0 # Reset the total and count for the new criteria
        totalRank = 0 # The total ranks for the criteria
        currCrit = critList[crit] # Get all the flights for the current criteria

        for flight in range(len(currCrit)):
            rank = 0
            currPercent = round(currCrit[flight][PERFORMED_COLUMN] # Get the flights performed and flights scheduled
                / currCrit[flight][SCHEDULED_COLUMN] * 100, 2)
            if(currPercent > 100): # Check for percentages above 100, as these can skew the results
                currPercent = 100.00 # Just change to 100

            # For rank, take the percent from above and multiply it by the number of available seats
            rank = (currPercent) * (currCrit[flight][SEATS_COLUMN] - currCrit[flight][PASSEN_COLUMN])
            totalRank += rank # Updating the total score for the month
            totalPerc += currPercent # Updating the total percentages
            count += 1.0 # Updating the number of flights

        if(count == 0): # To avoid a divbyzero exception
            continue

        critRank = round(totalRank / count, 2) # Get the average rank for the criteria
        critAverage = round(totalPerc / count, 2) # Get the average percentage for the criteria
        comboList.append(critRank)
        comboList.append(critAverage)
        percForCrit[crit] = comboList # Add that to a dict of averages for the criteria

    #percForCrit = sorted(percForCrit.items(), key = lambda kv: kv[1], reverse = True) # Sort the criteria by their ranks

    percForCrit = sorted(percForCrit.items(), key=operator.itemgetter(1), reverse = True)
    return percForCrit # Returning the newly sorted dictionary
