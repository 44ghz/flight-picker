import tkinter as tk                    # Main GUI capabilities
import operator                         # For sorting dicts
from modules import options as op       # To create the Options panel
from modules import tkfunctions as tf   # Custom TKinter functions
from modules import dataretrieval as dr # Custom data retrieval functions


################################################################################
#   FUNCTION NAME: rank_flights
#   DESCRIPTION: Takes in a list of flights (each consisting of a list) and prepends
#                the score and chance of success to each one. Chance of success is
#                determined by the number of flights performed divided by the number of
#                flights scheduled. The score is determined by taking the weight of a row
#                (seats divided by flights performed) and multiplying it by the chance of success
#   PARAMETERS: none
#   RETURN VALUES: flightList (List[List[String]]): The list of flights with their scores and percentages added
################################################################################
# Should only be called once to prevent altering the list a second time
def rank_flights():
    # Opening the .csv and converting to DataFrame
    flightData = dr.open_data('ProjectData.csv')
    flightList = dr.convert_df(flightData)

    SCHEDULED_COLUMN = 0 # The columns that correspond to the rows
    DEPARTURES_COLUMN = 1
    SEATS_COLUMN = 2

    # To prevent calling the function more than once
    if len(flightList[0]) > 14:
        return

    # Iterator is called flight, however each row may consist of multiple flights
    for flight in flightList: # For every row in the list
        # The chance for a successful flight
        success = flight[DEPARTURES_COLUMN] / flight[SCHEDULED_COLUMN]

        # The weight of a row, which brings it down to the equivalent of a single flight
        # (in the case that a row has incorporated multiple flights)
        weight = flight[SEATS_COLUMN] / flight[DEPARTURES_COLUMN]

        # If there are more flights performed than scheduled, reduce the percentage
        # down to 100%, as not to skew the results
        if(flight[DEPARTURES_COLUMN] > flight[SCHEDULED_COLUMN]):
            success = 1.0

        # Score is determined by multiplying the weight by the percentage
        score = weight * success

        success = round(success * 100, 2) # Rounding the percentages to 2 decimal places

        flight.insert(0, success) # Prepending the percentage
        flight.insert(0, score)   # Prepending the score (becomes the 0th column for the row)

    # Sorting the list of flights (rows) by the score for each index. In descending order
    flightList = sorted(flightList, key = operator.itemgetter(0), reverse = True)

    SCORE_COLUMN = 0
    # Rounding the score of each flight after it has been sorted
    for flight in flightList:
        flight[SCORE_COLUMN] = round(flight[SCORE_COLUMN], 2)

    return flightList


################################################################################
#   FUNCTION NAME: find_flights
#   DESCRIPTION: Helper function that directs the user mode choice to one of two modes
#   PARAMETERS: mode         (int): The mode the user selects
#               resultsFrame (tk.Frame): The frame in which to display results
#               flightList   (List[List]): The list of lists which consist of flight data
#               userChoices  (Dict[String: String]): The dict of choices the user selected from the options
#   RETURN VALUES: none
################################################################################
def find_flights(mode, resultsFrame, flightList, userChoices):
    if(mode.get() == 1): # If the user selects automatic mode
        automatic(resultsFrame, flightList)
    else: # If the user selected manual mode
        manual(resultsFrame, flightList, userChoices)


################################################################################
#   FUNCTION NAME: automatic
#   DESCRIPTION: Takes the list of flights and categorizes them to each of the criterion provided by the
#                specs. Then, takes the categories and finds the best options in each criterion.
#                Finally, adds the best options to a list that encompasses all criteria.
#                Passes that list to a function to display those results.
#   PARAMETERS: resultsFrame (tk.Frame): The frame in which to display results
#               flightList   (List[List]): The list of lists which consist of flight data
#   RETURN VALUES: none
################################################################################
def automatic(resultsFrame, flightList):
    DIST_COLUMN = 6 # The columns that correspond to the row
    CARRIER_COLUMN = 7
    ORIGIN_COLUMN = 8
    DEST_COLUMN = 9
    AIRCRAFT_COLUMN = 10
    OR_STATE_COLUMN = 11
    DEST_STATE_COLUMN = 12
    MONTH_COLUMN = 13

    # Dicts that take each individual option for each criterion
    # Used to categorize each of the flights
    flightsForDistance = {}
    flightsForCarrier = {}
    flightsForOriginCity = {}
    flightsForDestCity = {}
    flightsForAircraft = {}
    flightsForOriginState = {}
    flightsForDestState = {}
    flightsForMonth = {}

    optionsList = op.get_options_lists() # Getting the unique options for each criterion


    # Taking each unique option from the options lists and creating the key values for each dictionary
    # Each value for the keys will be a list, which will then have lists inside (flights)
    for distance in optionsList[0]:
        flightsForDistance[distance] = []

    for carrier in optionsList[1]:
        flightsForCarrier[carrier] = []

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


    for flight in flightList: # For every flight in the list, categorize it to each dict
        # Convert the distance from the flight to a range supported by the criterion
        # Cast to a string
        flightsForDistance[str(find_dist_range(flight[DIST_COLUMN]))].append(flight)

        # Everything else goes normally:
        # take the current flight and append it to the dict value to which its option corresponds
        # (example: a flight taking place in March would go in the entry for March in flightsForMonth)
        flightsForCarrier[flight[CARRIER_COLUMN]].append(flight)
        flightsForOriginCity[flight[ORIGIN_COLUMN]].append(flight)
        flightsForDestCity[flight[DEST_COLUMN]].append(flight)
        flightsForAircraft[flight[AIRCRAFT_COLUMN]].append(flight)
        flightsForOriginState[flight[OR_STATE_COLUMN]].append(flight)
        flightsForDestState[flight[DEST_STATE_COLUMN]].append(flight)
        flightsForMonth[flight[MONTH_COLUMN]].append(flight)


    flightsForCriteria = [] # Used to display the individual flights for each option

    # Example: if the user selects September in the automatic section, display the flights that take place in September
    flightsForCriteria.append(flightsForDistance)
    flightsForCriteria.append(flightsForCarrier)
    flightsForCriteria.append(flightsForOriginCity)
    flightsForCriteria.append(flightsForDestCity)
    flightsForCriteria.append(flightsForAircraft)
    flightsForCriteria.append(flightsForOriginState)
    flightsForCriteria.append(flightsForDestState)
    flightsForCriteria.append(flightsForMonth)

    # Getting the best options for each criterion, passing in the list of flights for each criterion
    # Includes all options for each criterion, but ordered by best average score for each option
    ranksForDistance =         find_best_auto(flightsForDistance)
    ranksForCarrier =          find_best_auto(flightsForCarrier)
    ranksForOriginCity =       find_best_auto(flightsForOriginCity)
    ranksForDestCity =         find_best_auto(flightsForDestCity)
    ranksForAircraft =         find_best_auto(flightsForAircraft)
    ranksForOriginState =      find_best_auto(flightsForOriginState)
    ranksForDestState =        find_best_auto(flightsForDestState)
    ranksForMonth =            find_best_auto(flightsForMonth)


    comboMonthCarrier =     find_best_auto(flightsForMonth, MONTH_COLUMN, CARRIER_COLUMN)
    comboDistanceAircraft = find_best_auto(flightsForDistance, DIST_COLUMN, AIRCRAFT_COLUMN)
    comboCarrierOrState =   find_best_auto(flightsForCarrier, CARRIER_COLUMN, OR_STATE_COLUMN)

    ranksForMonthCarrier =     comboMonthCarrier[0]
    ranksForDistanceAircraft = comboDistanceAircraft[0]
    ranksForCarrierOrState =   comboCarrierOrState[0]

    flightsForMonthCarrier =     comboMonthCarrier[1]
    flightsForDistanceAircraft = comboDistanceAircraft[1]
    flightsForCarrierOrState =   comboCarrierOrState[1]

    flightsForCriteria.append(flightsForMonthCarrier)
    flightsForCriteria.append(flightsForDistanceAircraft)
    flightsForCriteria.append(flightsForCarrierOrState)

    listOfBests = [] # The overall list of best criteria

    # Adding these lists to another list, which is used to display in the window
    listOfBests.append(ranksForDistance)
    listOfBests.append(ranksForCarrier)
    listOfBests.append(ranksForOriginCity)
    listOfBests.append(ranksForDestCity)
    listOfBests.append(ranksForAircraft)
    listOfBests.append(ranksForOriginState)
    listOfBests.append(ranksForDestState)
    listOfBests.append(ranksForMonth)
    listOfBests.append(ranksForMonthCarrier)
    listOfBests.append(ranksForDistanceAircraft)
    listOfBests.append(ranksForCarrierOrState)

    tf.create_auto_panel(resultsFrame, listOfBests, flightsForCriteria) # Create the tabs to display data


################################################################################
#   FUNCTION NAME: find_best_auto
#   DESCRIPTION: Takes a dict and sorts the options for each criterion by their average score. This is calculated by
#                averaging the score of each of the flights associated with each option. This function is meant to
#                run on a single criterion at a time, and operating on that criterion's options.
#   PARAMETERS: critDict     (List[Dict[String: List]]): The list of categorized flights (dicts)
#               firstColumn  (Integer): Optional column for more flights (for combinations)
#               secondColumn (Integer): Optional column for more flights (for combinations)
#   RETURN VALUES: critInfo (List[Tuple(String, List)]): The sorted options for the passed criterion
################################################################################
def find_best_auto(critDict, firstColumn = None, secondColumn = None):
    SCORE_COLUMN = 0 # The columns containing the score and percentage of a flight
    PERCENTAGE_COLUMN = 1

    # The dict containing the options for the criterion, which is to be sorted after their average scores and percentages are calculated
    critInfo = {}

    # Each option in each criterion has a list of flights associated with it
    # Take the score for each flight in the list and add it to the total
    # Take the total score and divide it by the number of rows to find average score
    # Do the same thing with percentage
    for option in critDict:
        comboList = []
        totalScore = 0
        totalPercentage = 0
        currOption = critDict[option] # The current option being evaluated

        for flight in range(len(currOption)): # Finding every score and percentage for every flight in that option
            totalScore += currOption[flight][SCORE_COLUMN]
            totalPercentage += currOption[flight][PERCENTAGE_COLUMN]

        try:
            averageScore = round((totalScore / len(currOption)), 2)           # Finding the average score for that option
            averagePercentage = round((totalPercentage / len(currOption)), 2) # Finding the average percentage for that option
        except ZeroDivisionError:
            continue

        comboList.append(averageScore)
        comboList.append(averagePercentage)

        critInfo[option] = comboList

    critInfo = sorted(critInfo.items(), key = operator.itemgetter(1), reverse = True) # Sorting the dict by score
    # In the process, the dict becomes a list of tuples

    if firstColumn is None and secondColumn is None: # If the user didn't supply additional commands
        return critInfo
    else:
        # Take the critDict and get the values from the key that matches that of the first of the best tuple
        # Get the flights from that and add to a new list, then run back through this function

        bestOptionName  = critInfo[0][0]# Getting the name of the best criterion
        bestOptionFlights = critInfo[0] # Get the best list of flights for the first criterion

        filteredFlights = critDict[bestOptionName] # The list of flights for the smaller flight pool

        secondDict = {}

        for flight in filteredFlights: # Making every key value a list
            secondDict[flight[secondColumn]] = []

        for flight in filteredFlights: # Categorizing each flight in the smaller pool
            secondDict[flight[secondColumn]].append(flight)

        returnList = []

        # Send the newly filtered dictionary through the same function to
        # get the best options for the smaller flight pool
        returnList.append(find_best_auto(secondDict))
        returnList.append(secondDict)

        return returnList

################################################################################
#   FUNCTION NAME: manual
#   DESCRIPTION: Takes the list of flights and the user input of choices and filters out
#                the matching flights using filter_flights.
#   PARAMETERS: resultsFrame (tk.Frame): The frame in which to display results
#               flightList   (List[List]): The list of lists which consist of flight data
#               userChoices  (Dict[String: String]): The dict of choices the user selected from the options
#   RETURN VALUES: none
################################################################################
def manual(resultsFrame, flightList, userChoices):
    # Creating the filtered flight list using the overall list, along with the user choices
    manualFlightList = filter_flights(flightList, userChoices)

    # Creating the display with the new list
    tf.create_manual_panel(resultsFrame, manualFlightList)


################################################################################
#   FUNCTION NAME: filter_flights
#   DESCRIPTION: Takes the list of flights
#   PARAMETERS: flightList   (List[List]): The list of lists which consist of flight data
#               userChoices  (Dict[String: String]): The dict of choices the user selected from the options
#   RETURN VALUES: flightList   (List[List]): The list of lists which consist of flight data
#                  OR
#                  filteredList (List[List]): The list of flights matching user choices
################################################################################
def filter_flights(flightList, userChoices):
    DIST_COLUMN = 6 # The columns that correspond to the rows' columns
    CARRIER_COLUMN = 7
    ORIGIN_COLUMN = 8
    DEST_COLUMN = 9
    AIRCRAFT_COLUMN = 10
    OR_STATE_COLUMN = 11
    DEST_STATE_COLUMN = 12
    MONTH_COLUMN = 13

    emptyChoices = True # Flag that indicates whether the user selected any options
    matchCounter = 0    # How many options must the flight match from the selected user options
    matchList = []      # A flag list that decides whether the flight matches the options it needs to
    filteredList = []   # The flights that actually match the user options

    for criterion, choice in userChoices.items(): # For every option available
        matchList.append(False)             # Adding each opportunity for an option to be selected
        if(choice != "None"):               # If the user selected something for that criterion
            matchList[matchCounter] = False # Make sure the flight matching defaults to False
            emptyChoices = False            # The user selected an option for something

        matchCounter += 1

    if(emptyChoices is False): # If the user actually changed an option
        for flight in flightList:
            matchCounter = 0 # Resetting the iterator for the lsit

            # Resetting the match list for every flight
            for criterion, choice in userChoices.items(): # For every option available
                matchList[matchCounter] = True      # Assuming the current choice is "None"
                if(choice != "None"):               # But if it's not
                    matchList[matchCounter] = False # We don't know if the flight matches up yet

                matchCounter += 1

            # For every criterion, we check to see if the user has selected something other than "None"
            # If they have, the current flight is checked to see if it matches. If it does, the matchList is updated
            ####################################################################
            if(userChoices["Distance"] != "None"):
                convertedDistance = find_dist_range(flight[DIST_COLUMN])

                if(convertedDistance == userChoices["Distance"]):
                    matchList[0] = True


            if(userChoices["Carrier"] != "None"):
                if(flight[CARRIER_COLUMN] == userChoices["Carrier"]):
                    matchList[1] = True


            if(userChoices["Origin City"] != "None"):
                if(flight[ORIGIN_COLUMN] == userChoices["Origin City"]):
                    matchList[2] = True


            if(userChoices["Destination City"] != "None"):
                if(flight[DEST_COLUMN] == userChoices["Destination City"]):
                    matchList[3] = True


            if(userChoices["Aircraft"] != "None"):
                if(flight[AIRCRAFT_COLUMN] == userChoices["Aircraft"]):
                    matchList[4] = True


            if(userChoices["State Origin"] != "None"):
                if(flight[OR_STATE_COLUMN] == userChoices["State Origin"]):
                    matchList[5] = True


            if(userChoices["State Destination"] != "None"):
                if(flight[DEST_STATE_COLUMN] == userChoices["State Destination"]):
                    matchList[6] = True


            if(userChoices["Month"] != "None"):
                if(flight[MONTH_COLUMN] == userChoices["Month"]):
                    matchList[7] = True


            if False not in matchList: # If every user chosen criterion matches that of the current flight's
                filteredList.append(flight) # Add it to the list of filtered flights

    # If there were no options selected, give all the flights back
    else:
        return flightList

    # Return the list with the filtered flights
    return filteredList


################################################################################
#   FUNCTION NAME: find_dist_range
#   DESCRIPTION: Takes in a flight's distance and converts it to a specific range per specs
#   PARAMETERS: distance (Integer)
#   RETURN VALUES: String: Returns a string with the corresponding range
################################################################################
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
