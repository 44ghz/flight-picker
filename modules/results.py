import tkinter as tk # Main GUI capabilities
import operator
from modules import dataretrieval as dr
from modules import options as op
from modules import tkfunctions as tf

# Should only be called once to prevent altering the list a second time
def rank_flights(flightList):
    SCHEDULED_COLUMN = 0
    DEPARTURES_COLUMN = 1
    SEATS_COLUMN = 2

    for flight in range(len(flightList)): # For every row in the list
        currFlight = flightList[flight]

        success = currFlight[DEPARTURES_COLUMN] / currFlight[SCHEDULED_COLUMN]
        weight = currFlight[SEATS_COLUMN] / currFlight[DEPARTURES_COLUMN]

        if(currFlight[DEPARTURES_COLUMN] > currFlight[SCHEDULED_COLUMN]):
            success = 1.0

        score = weight * success

        score = round(score, 2)
        success = round(success * 100, 2)

        currFlight.insert(0, success)
        currFlight.insert(0, score)

    flightList = sorted(flightList, key = operator.itemgetter(0), reverse = True)
    return flightList


def find_flights(mode, resultsFrame, flightList, userChoices):
    if(mode.get() == 1):
        automatic(resultsFrame, flightList)
    else:
        manual(resultsFrame, flightList, userChoices)


def automatic(resultsFrame, flightList):
    DIST_COLUMN = 6 # The columns that correspond to the row
    CARRIER_COLUMN = 7
    ORIGIN_COLUMN = 8
    DEST_COLUMN = 9
    AIRCRAFT_COLUMN = 10
    OR_STATE_COLUMN = 11
    DEST_STATE_COLUMN = 12
    MONTH_COLUMN = 13

    flightsForDistance = {} # Use predetermined ranges
    flightsForCarrier = {}
    flightsForOriginCity = {}
    flightsForDestCity = {}
    flightsForAircraft = {}
    flightsForOriginState = {}
    flightsForDestState = {}
    flightsForMonth = {}

    optionsList = op.get_options_lists()

    # Taking each unique option from the options lists and creating the key values for each dictionary
    for distance in optionsList[0]:
        flightsForDistance[distance] = []

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

    for flight in range(len(flightList)): # For every flight in the list, categorize it to each dict
        currentFlight = flightList[flight]
        # Convert the distance from the flight to a range supported by the criteria
        flightsForDistance[str(find_dist_range(currentFlight[DIST_COLUMN]))].append(currentFlight)

        # Everything else goes normally
        flightsForCarrier[currentFlight[CARRIER_COLUMN]].append(currentFlight)
        flightsForOriginCity[currentFlight[ORIGIN_COLUMN]].append(currentFlight)
        flightsForDestCity[currentFlight[DEST_COLUMN]].append(currentFlight)
        flightsForAircraft[currentFlight[AIRCRAFT_COLUMN]].append(currentFlight)
        flightsForOriginState[currentFlight[OR_STATE_COLUMN]].append(currentFlight)
        flightsForDestState[currentFlight[DEST_STATE_COLUMN]].append(currentFlight)
        flightsForMonth[currentFlight[MONTH_COLUMN]].append(currentFlight)

    flightsForCriteria = []

    flightsForCriteria.append(flightsForDistance)
    flightsForCriteria.append(flightsForCarrier)
    flightsForCriteria.append(flightsForOriginCity)
    flightsForCriteria.append(flightsForDestCity)
    flightsForCriteria.append(flightsForAircraft)
    flightsForCriteria.append(flightsForOriginState)
    flightsForCriteria.append(flightsForDestState)
    flightsForCriteria.append(flightsForMonth)

    # Returning the list of best distances, passing in the list of flights and the thing we want to filter by
    ranksForDistance = find_best_auto(flightsForDistance)
    ranksForCarrier = find_best_auto(flightsForCarrier)
    ranksForOriginCity = find_best_auto(flightsForOriginCity)
    ranksForDestCity = find_best_auto(flightsForDestCity)
    ranksForAircraft = find_best_auto(flightsForAircraft)
    ranksForOriginState = find_best_auto(flightsForOriginState)
    ranksForDestState = find_best_auto(flightsForDestState)
    ranksForMonth = find_best_auto(flightsForMonth)

    listOfBests = [] # The overall list of best things

    listOfBests.append(ranksForDistance)
    listOfBests.append(ranksForCarrier)
    listOfBests.append(ranksForOriginCity)
    listOfBests.append(ranksForDestCity)
    listOfBests.append(ranksForAircraft)
    listOfBests.append(ranksForOriginState)
    listOfBests.append(ranksForDestState)
    listOfBests.append(ranksForMonth) # Add it to the list of best things

    tf.create_auto_panel(resultsFrame, listOfBests, flightsForCriteria) # Create the tabs to display data


def find_best_auto(critList):
    SCORE_COLUMN = 0
    PERCENTAGE_COLUMN = 1

    critInfo = {}

    # Each criteria has a list of flights associated with it
    # Take the score for each flight in the list and add it to the total
    # Take the total score and divide it by the number of rows to find average score
    # Do the same thing with percentage
    for criteria in critList:
        comboList = []
        totalScore = 0
        totalPercentage = 0
        currCriteria = critList[criteria]

        for flight in range(len(currCriteria)):
            totalScore += currCriteria[flight][SCORE_COLUMN]
            totalPercentage += currCriteria[flight][PERCENTAGE_COLUMN]

        if(len(currCriteria) == 0):
            continue

        averageScore = round((totalScore / len(currCriteria)), 2)
        averagePercentage = round((totalPercentage / len(currCriteria)), 2)

        comboList.append(averageScore)
        comboList.append(averagePercentage)

        critInfo[criteria] = comboList

    critInfo = sorted(critInfo.items(), key = operator.itemgetter(1), reverse = True) # Sorting the dict by score
    return critInfo


def manual(resultsFrame, flightList, userChoices):
    manualFlightList = filter_flights(flightList, userChoices)

    tf.create_manual_panel(resultsFrame, manualFlightList)


def filter_flights(manualFlightList, userChoices):
    DIST_COLUMN = 6 # The columns that correspond to the row
    CARRIER_COLUMN = 7
    ORIGIN_COLUMN = 8
    DEST_COLUMN = 9
    AIRCRAFT_COLUMN = 10
    OR_STATE_COLUMN = 11
    DEST_STATE_COLUMN = 12
    MONTH_COLUMN = 13

    emptyChoices = True
    matchCounter = 0
    matchList = []
    filteredList = []

    for criteria, choice in userChoices.items():
        matchList.append(False)
        if(choice != "None"):
            matchList[matchCounter] = False
            emptyChoices = False

        matchCounter += 1

    if(emptyChoices is False):
        for flight in range(len(manualFlightList)):
            matchCounter = 0

            for criteria, choice in userChoices.items():
                matchList[matchCounter] = True
                if(choice != "None"):
                    matchList[matchCounter] = False

                matchCounter += 1

            currentFlight = manualFlightList[flight]

            if(userChoices["Distance"] != "None"):
                convertedDistance = find_dist_range(currentFlight[DIST_COLUMN])

                if(convertedDistance == userChoices["Distance"]):
                    matchList[0] = True

            if(userChoices["Carrier"] != "None"):
                if(currentFlight[CARRIER_COLUMN] == userChoices["Carrier"]):
                    matchList[1] = True

            if(userChoices["Origin City"] != "None"):
                if(currentFlight[ORIGIN_COLUMN] == userChoices["Origin City"]):
                    matchList[2] = True

            if(userChoices["Destination City"] != "None"):
                if(currentFlight[DEST_COLUMN] == userChoices["Destination City"]):
                    matchList[3] = True

            if(userChoices["Aircraft"] != "None"):
                if(currentFlight[AIRCRAFT_COLUMN] == userChoices["Aircraft"]):
                    matchList[4] = True

            if(userChoices["State Origin"] != "None"):
                if(currentFlight[OR_STATE_COLUMN] == userChoices["State Origin"]):
                    matchList[5] = True

            if(userChoices["State Destination"] != "None"):
                if(currentFlight[DEST_STATE_COLUMN] == userChoices["State Destination"]):
                    matchList[6] = True

            if(userChoices["Month"] != "None"):
                if(currentFlight[MONTH_COLUMN] == userChoices["Month"]):
                    matchList[7] = True

            if False not in matchList:
                filteredList.append(currentFlight)

    # If there were no options selected
    else:
        return manualFlightList

    # Return the list with the filtered flights
    return filteredList



def find_dist_range(distance):
    if(0 <= distance <= 99):
        return "0 - 99"
    elif(100 <= distance <= 199):
        return "100 - 199"
    elif(200 <= distance <= 299):
        return "200 - 299"
    elif(300 <= distance <= 399):
        return "300 - 399"
    elif(400 <= distance <= 499):
        return "400 - 499"
    elif(500 <= distance <= 999):
        return "500 - 999"
    elif(1000 <= distance <= 1499):
        return "1000 - 1499"
    elif(1500 <= distance <= 1999):
        return "1500 - 1999"
    elif(2000 <= distance <= 2499):
        return "2000 - 2499"
    else:
        return ">2500"
