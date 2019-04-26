import tkinter as tk                    # Main GUI capabilities
from tkinter import font                # For changing fonts in widgets
from tkinter import ttk                 # Various other tkinter widgets (mainly combobox)
from modules import dataretrieval as dr # Custom data retrieval functions
from modules import results             # Creating the results from the user input


################################################################################
#   CLASS NAME: OptionsCombobox
#   DESCRIPTION: Custom combobox to display options for Manual mode.
################################################################################
class OptionsCombobox():
    def __init__(self, frame, values, row, column):
        self._frame = frame      # The frame to in which to populate
        self._values = values    # Options within the box
        self._row = row          # Row for grid
        self._column = column    # Column for grid
        self._state = 'disabled' # State of the box
        self._default = "None"   # Default value
        self._create_box()       # Creating the box itself
        self._display_box()      # Placing in grid in window
        self.disable()           # Disable the box
        self.enable()            # Enable the box
        self.get_current()       # Get the current value
        self.get_values()        # Get all values
        self.reset()             # Revert to default value

    def _create_box(self):
        self._box = ttk.Combobox(self._frame, values = self._values, state = self._state)
        self._box.set(self._default)

    def _display_box(self):
        self._box.grid(row = self._row, column = self._column)
        self._box.config(width = 13, justify = tk.LEFT)

    def disable(self):
        self._box.config(state = 'disabled')

    def enable(self):
        self._box.config(state = 'readonly')

    def get_current(self):
        return self._box.get()

    # Set the current value to be the value in position at val - 1
    def set_current(self, val):
        self._box.set(self._box["values"][val - 1])

    def get_values(self):
        return self._box["values"]

    def reset(self):
        self._box.set(self._default)


def fnf_popup():
    win = tk.Tk()
    win.title("File Error")

    fnfLabel = tk.Label(win, text = "The data file was not found.\n Please ensure the file 'ProjectData.csv' is present in the data folder.")
    fnfLabel.grid()

    fnfButton = tk.Button(text = "OK", command = win.destroy)
    fnfButton.grid()

    return win


################################################################################
#   FUNCTION NAME: create_auto_panel
#   DESCRIPTION: Creates the tabs for the best options for criteria, then calls display_best for each
#   PARAMETERS: resultsFrame       (tk.Frame): The frame in which to display results
#               listOfBests        (List[List[Tuple(String, List)]]): The list of best options for each
#                                  criterion and their respective names, average ranks, and average scores
#               flightsForCriteria (List[Dict[String: List]])
#   RETURN VALUES: none
################################################################################
def create_auto_panel(resultsFrame, listOfBests, flightsForCriteria):
    criteriaTabs = ttk.Notebook(resultsFrame) # The pages used to tab through the criteria

    critDistance = ttk.Frame(criteriaTabs,
        width = 1750,
        height = 676)   # 1st page

    critCarrier = ttk.Frame(criteriaTabs,
        width = 1750,
        height = 676)   # 2nd page

    critOriginCity = ttk.Frame(criteriaTabs,
        width = 1750,
        height = 676)   # 3rd page

    critDestCity = ttk.Frame(criteriaTabs,
        width = 1750,
        height = 676)   # 4th page

    critAircraft = ttk.Frame(criteriaTabs,
        width = 1750,
        height = 676)   # 5th page

    critOriginState = ttk.Frame(criteriaTabs,
        width = 1750,
        height = 676)   # 6th page

    critDestState = ttk.Frame(criteriaTabs,
        width = 1750,
        height = 676)   # 7th page

    critMonth = ttk.Frame(criteriaTabs,
        width = 1750,
        height = 676)   # 8th page

    critMonthCarrier = ttk.Frame(criteriaTabs,
        width = 1750,
        height = 676)   # 9th page

    critDistanceAircraft = ttk.Frame(criteriaTabs,
        width = 1750,
        height = 676)   # 10th page

    critCarrierOrState = ttk.Frame(criteriaTabs,
        width = 1750,
        height = 676)   # 11th page



    ############################################################################
    # Creating the tabs themselves by adding them to the notebook

    criteriaTabs.add(critDistance,         text = "        Distance        ")
    criteriaTabs.add(critCarrier,          text = "        Carrier         ")
    criteriaTabs.add(critOriginCity,       text = "       Origin City      ")
    criteriaTabs.add(critDestCity,         text = "    Destination City    ")
    criteriaTabs.add(critAircraft,         text = "        Aircraft        ")
    criteriaTabs.add(critOriginState,      text = "      Origin State      ")
    criteriaTabs.add(critDestState,        text = "   Destination State    ")
    criteriaTabs.add(critMonth,            text = "         Month          ")
    criteriaTabs.add(critMonthCarrier,     text = "     Month + Carrier    ")
    criteriaTabs.add(critDistanceAircraft, text = "  Distance + Aircraft   ")
    criteriaTabs.add(critCarrierOrState,   text = " Origin State + Carrier ")
    criteriaTabs.grid(row = 0, column = 0)


    # Displaying the best options for each criteria
    display_best(critDistance, listOfBests, 0, flightsForCriteria)
    display_best(critCarrier, listOfBests, 1, flightsForCriteria)
    display_best(critOriginCity, listOfBests, 2, flightsForCriteria)
    display_best(critDestCity, listOfBests, 3, flightsForCriteria)
    display_best(critAircraft, listOfBests, 4, flightsForCriteria)
    display_best(critOriginState, listOfBests, 5, flightsForCriteria)
    display_best(critDestState, listOfBests, 6, flightsForCriteria)
    display_best(critMonth, listOfBests, 7, flightsForCriteria)
    display_best(critMonthCarrier, listOfBests, 8, flightsForCriteria)
    display_best(critDistanceAircraft, listOfBests, 9, flightsForCriteria)
    display_best(critCarrierOrState, listOfBests, 10, flightsForCriteria)


################################################################################
#   FUNCTION NAME: display_best
#   DESCRIPTION: Shows the best (and all) options for a specified criterion
#   PARAMETERS: resultsFrame       (tk.Frame): The frame in which to display results
#               listOfBests        (List[List[Tuple(String, List)]]): The list of best options for each
#                                  criterion and their respective names, average ranks, and average scores
#               desiredCriterion   (Integer): The desired criterion expressed as an integer
#               flightsForCriteria (List[Dict[String: List]])
#   RETURN VALUES: none
################################################################################
def display_best(resultsFrame, listOfBests, desiredCriterion, flightsForCriteria):
    # listOfBests outline:
    # List[List[Tuple(String, [List])]
    # [criterion[option(name,[rank, percentage])]]

    # Casting the integer of the desired criterion to a string
    critDict = {}
    critDict[0] =  "distance (in miles)"
    critDict[1] =  "carrier"
    critDict[2] =  "origin city"
    critDict[3] =  "destination city"
    critDict[4] =  "aircraft"
    critDict[5] =  "origin state"
    critDict[6] =  "destination state"
    critDict[7] =  "month"
    critDict[8] =  "carrier from best months"
    critDict[9] =  "distance from best aircraft"
    critDict[10] = "origin state from best carrier"
    
    bestOption = tk.StringVar()                             # The output of the best option
    bestOptionName = listOfBests[desiredCriterion][0][0]    # The best option name from the list of overall best criterion
    bestOptionRank = listOfBests[desiredCriterion][0][1][0] # The best option rank
    bestOptionPerc = listOfBests[desiredCriterion][0][1][1] # The best option percentage

    # Outputting the best option and its score and percentage at the top of the window
    bestOption.set("Best " + critDict[desiredCriterion] + ": " + bestOptionName +
        "\nAverage score: " + str(bestOptionRank) + " points" +
        "\nAverage percentage: " + str(bestOptionRank) + "%")


    bestOptionFrame = tk.Frame(resultsFrame,
        width = 1750,
        height = 676)
    bestOptionFrame.pack()

    bestOptionLabel = tk.Label(bestOptionFrame,
        textvariable = bestOption,
        width = 75,
        justify = tk.LEFT)
    bestOptionLabel.pack(side = 'top')


    criteriaTree = ttk.Treeview(bestOptionFrame)
    criteriaTree["columns"] = ("1", "2", "3")
    criteriaTree['show'] = 'headings'
    criteriaTree.column("1", width = 200, anchor = 'c')
    criteriaTree.column("2", width = 200, anchor = 'c')
    criteriaTree.column("3", width = 200, anchor = 'c')

    criteriaTree.heading("1", text = "Option")
    criteriaTree.heading("2", text = "Average Score")
    criteriaTree.heading("3", text = "Average Chance of Success")

    criteriaTree.config(height = 12)

    criteriaTree.pack(side = 'left')
    for option in range(len(listOfBests[desiredCriterion])): # For every option in the desired criterion
        criteriaTree.insert("", 'end', values =
            (listOfBests[desiredCriterion][option][0],
             listOfBests[desiredCriterion][option][1][0],
             listOfBests[desiredCriterion][option][1][1]))
        # Insert into the tree: The name for the first column, the score for the second column, and the percentage for the third column

    optionScrollBar = ttk.Scrollbar(bestOptionFrame,
        orient = "vertical",
        command = criteriaTree.yview)
    optionScrollBar.pack(side = 'right', fill = 'y', expand = 1)

    criteriaTree.configure(yscrollcommand = optionScrollBar.set)

    flightTree = ttk.Treeview(resultsFrame)
    configure_treeview(resultsFrame, flightTree)

    # Whenever the user clicks on an option that's displayed in the criteria list
    # Display the flights for that option
    criteriaTree.bind("<ButtonRelease-1>", lambda _: select_item(criteriaTree, flightTree, desiredCriterion, flightsForCriteria))


################################################################################
#   FUNCTION NAME: select_item
#   DESCRIPTION: Displays the flights associated with a specified option
#   PARAMETERS: criteriaTree       (tk.Treeview): The treeview to display the different criteria
#               flightTree         (tk.Treeview): Treeview to display individual flights for an option
#               desiredCriterion   (Integer): The desired criterion expressed as an integer
#               flightsForCriteria (List[Dict[String: List]])
#   RETURN VALUES: none
################################################################################
def select_item(criteriaTree, flightTree, desiredCriterion, flightsForCriteria):
    curItem = criteriaTree.focus() # Getting the current option that the user selected

    # curItem is the current listOfBests option (criteria with score and percentage)
    # currentFlights takes the list of organized criteria with their dicts
    # and gets the dict of the desiredCriterion, and uses the name of the criteria from the tree as the index of the dict
    try:
        currentFlights = flightsForCriteria[desiredCriterion][criteriaTree.item(curItem)["values"][0]]
    except IndexError: # If user clicks something other than an item
        return

    # Remove all previous flights
    flightTree.delete(*flightTree.get_children())

    # Inserting all new flights
    for flight in range(len(currentFlights)):
        flightTree.insert("", 'end', values = currentFlights[flight])


################################################################################
#   FUNCTION NAME: create_manual_panel
#   DESCRIPTION: Creates the manual results from the filtered list of flights. Filtered list is
#                determined by the user choices. Uses tk.Treeview to display the data
#   PARAMETERS: resultsFrame (tk.Frame): The frame in which to display results
#               filteredList (List[List]): The list of flights matching the user choices
#   RETURN VALUES: none
################################################################################
def create_manual_panel(resultsFrame, filteredList):
    helvBig = font.Font(family = 'Helvetica', size = '14')

    if len(filteredList) is 0: # If no flights match the user choices
        clear_results(resultsFrame) # Getting rid of any previous results
        noItemsLabel = tk.Label(resultsFrame,
            text = "There were no flights that match your criteria. Alter your choices and try again.",
            font = helvBig,
            justify = tk.LEFT)
        noItemsLabel.grid(row = 0, column = 0, sticky = 'nsew')
        return

    flightTree = ttk.Treeview(resultsFrame)
    configure_treeview(resultsFrame, flightTree)

    for flight in filteredList: # Adding each flight to the tree view
        flightTree.insert("", 'end', values = flight)


################################################################################
#   FUNCTION NAME: configure_treeview
#   DESCRIPTION: Alters the treeview to format the columns and headers when displaying individual flights
#   PARAMETERS: resultsFrame (tk.Frame): The frame in which to display results
#               flightTree   (tk.Treeview): Treeview to display individual flights for an option
#   RETURN VALUES: none
################################################################################
def configure_treeview(resultsFrame, flightTree):
    flightTree.config(height = 38) # 38 for max height
    flightTree.pack(side = 'left')

    # Creating the scroll bar for the flight tree
    treeScrollBar = ttk.Scrollbar(resultsFrame,
        orient = "vertical",
        command = flightTree.yview)

    treeScrollBar.pack(side = 'right', fill = 'y')

    # Configuring the scroll funtion the flight tree to control the scroll bar
    flightTree.configure(yscrollcommand = treeScrollBar.set)


    flightTree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14")
    flightTree['show'] = 'headings'

    # Adding all columns
    flightTree.column("1", width = 114, anchor = 'c')
    flightTree.column("2", width = 114, anchor = 'c')
    flightTree.column("3", width = 114, anchor = 'c')
    flightTree.column("4", width = 114, anchor = 'c')
    flightTree.column("5", width = 114, anchor = 'c')
    flightTree.column("6", width = 114, anchor = 'c')
    flightTree.column("7", width = 114, anchor = 'c')
    flightTree.column("8", width = 114, anchor = 'c')
    flightTree.column("9", width = 114, anchor = 'c')
    flightTree.column("10", width = 114, anchor = 'c')
    flightTree.column("11", width = 114, anchor = 'c')
    flightTree.column("12", width = 114, anchor = 'c')
    flightTree.column("13", width = 114, anchor = 'c')
    flightTree.column("14", width = 114, anchor = 'c')

    # Adding all headings
    flightTree.heading("1", text = "Points")
    flightTree.heading("2", text = "% of Success")
    flightTree.heading("3", text = "Scheduled")
    flightTree.heading("4", text = "Performed")
    flightTree.heading("5", text = "Seats")
    flightTree.heading("6", text = "Passengers")
    flightTree.heading("7", text = "Distance (mi.)")
    flightTree.heading("8", text = "Carrier")
    flightTree.heading("9", text = "Origin")
    flightTree.heading("10", text = "Destination")
    flightTree.heading("11", text = "Aircraft")
    flightTree.heading("12", text = "Origin State")
    flightTree.heading("13", text = "Dest State")
    flightTree.heading("14", text = "Month")


################################################################################
#   FUNCTION NAME: configure_treeview
#   DESCRIPTION: Removes all widgets from the results frame
#   PARAMETERS: resultsFrame (tk.Frame): The frame in which to display results
#   RETURN VALUES: none
################################################################################
def clear_results(resultsFrame):
    for child in resultsFrame.winfo_children():
        child.pack_forget()


################################################################################
#   FUNCTION NAME: to_main_menu
#   DESCRIPTION: Clears the screen and displays the main menu
#   PARAMETERS: resultsFrame (tk.Frame): The frame in which to display results
#   RETURN VALUES: none
################################################################################
def to_main_menu(resultsFrame):
    clear_results(resultsFrame)
    create_main_label(resultsFrame)


################################################################################
#   FUNCTION NAME: create_main_label
#   DESCRIPTION: Displays the main menu text, which explains the program and its instructions
#   PARAMETERS: resultsFrame (tk.Frame): The frame in which to display results
#   RETURN VALUES: none
################################################################################
def create_main_label(resultsFrame):
    helvBig = font.Font(family = 'Helvetica', size = '14')
    mainLabel = tk.Label(resultsFrame, text =
        """
        Welcome to Flight Picker.\n
        There are two modes to choose from: Automatic and Manual.\n
        Automatic will choose the best flights based on predetermined criteria.
        Use the tabs to cycle between the criteria. Select a specific item in the criteria list to view its flights.\n
        Manual will allow you to filter out the best flights for any criteria and combination of criteria.
        If different options are selected, use the 'Find Flights' button to update the results window.\n
        -------------------------------------------------------------------------------------------------------------------------------------\n
        Choose a mode to the left and click 'Find Flights' to generate the results.\n
        Use the 'Main Menu' choice to return to this screen.\n
        Click 'Update Data' to refresh the options for Manual mode if they have changed within
        the application or within the data file.\n""",
        justify = tk.LEFT,
        font = helvBig)

    mainLabel.grid(row = 0, column = 0, sticky = 'nsew')
