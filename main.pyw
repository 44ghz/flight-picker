import tkinter as tk                    # Main GUI capabilities
import random                           # For random options
from tkinter import font                # For changing fonts in widgets
from tkinter import ttk                 # Various other tkinter widgets (mainly combobox)
from tkinter import PhotoImage          # For taskbar icon
from modules import tkfunctions as tf   # Custom TKinter functions
from modules import dataretrieval as dr # Custom data retrieval functions
from modules import options as op       # To create the Options panel
from modules import results             # Creating the results from the user input
from ttkthemes import themed_tk         # For window theme


################################################################################
#   FUNCTION NAME: get_flights
#   DESCRIPTION: Takes the mode provided by the user, any options they may have selected,
#                and the Frame to which the results are output. Then, provides these details
#                to find_flights to find the correct flights and display the results
#   PARAMETERS: mode         (Integer): The mode selected by the user, 1 for Automatic, 2 for Manual
#               resultsFrame (tk.Frame): The frame in which to display results
#               flightList   (List[List]): The list of lists which consist of flight data
#               comboBoxList (List[OptionsCombobox]): The list of comboboxes that correspond to user options
#   RETURN VALUES: none
################################################################################
def get_flights(mode, resultsFrame, flightList, comboBoxList): # The command to use when finding flights
    tf.clear_results(resultsFrame) # Getting rid of any possible results or notifications

    userChoices = get_user_choices(comboBoxList)

    # Passing data to find_flights, which will get the correct flight data and display it
    results.find_flights(mode, resultsFrame, flightList, userChoices)


################################################################################
#   FUNCTION NAME: reset_choices
#   DESCRIPTION: Resets all options for manual mode back to "None"
#   PARAMETERS: comboBoxList (List[OptionsCombobox]): The list of comboboxes that correspond to user options
#   RETURN VALUES: none
################################################################################
def reset_choices(comboBoxList):
    for combobox in comboBoxList: # Resetting all comboboxes
        combobox.reset()


################################################################################
#   FUNCTION NAME: random_choices
#   DESCRIPTION: Selects random values for the Distance, Carrier, and Month criteria
#   PARAMETERS: comboBoxList (List[OptionsCombobox]): The list of comboboxes that correspond to user options
#   RETURN VALUES: none
################################################################################
def random_choices(comboBoxList):
    for comboBox in range(2): # For the first two boxes
        # Get a random number between 1 and the maximum amount of options for that criterion
        # 0 is omitted because the 0th position in the boxes belongs to "None"
        randomOption = random.randint(1, len(comboBoxList[comboBox].get_values()))
        comboBoxList[comboBox].set_current(randomOption)

    randomOption = random.randint(1, len(comboBoxList[7].get_values()))
    comboBoxList[7].set_current(randomOption)


################################################################################
#   FUNCTION NAME: get_user_choices
#   DESCRIPTION: Gets the values from the options boxes and compiles them into a dict to be returned
#   PARAMETERS: comboBoxList (List[OptionsCombobox]): The list of comboboxes that correspond to user options
#   RETURN VALUES: optionsDict (Dict[String: String]): The dict containing the choices for each criterion
################################################################################
def get_user_choices(comboBoxList):
    optionsDict = {}

    # Getting the value for every box and assigning it to its corresponding criterion
    optionsDict["Distance"] = comboBoxList[0].get_current()
    optionsDict["Carrier"] = comboBoxList[1].get_current()
    optionsDict["Origin City"] = comboBoxList[2].get_current()
    optionsDict["Destination City"] = comboBoxList[3].get_current()
    optionsDict["Aircraft"] = comboBoxList[4].get_current()
    optionsDict["State Origin"] = comboBoxList[5].get_current()
    optionsDict["State Destination"] = comboBoxList[6].get_current()
    optionsDict["Month"] = comboBoxList[7].get_current()

    return optionsDict


################################################################################

dr.data_exists()   # Touching the data files to make sure they exist

# Converting the DataFrame to a list representation, then ranking the flights by their score
flightList = results.rank_flights()

mainWindow = tf.common_theme()    # The main window of display
mainWindow.title("Flight Picker") # The title of the GUI window
mainWindow.geometry("1750x785")   # Scale of the window
mainWindow.resizable(0, 0)        # Cannot resize window (x, y)

mainWindow.grid_rowconfigure(0, weight = 2)
mainWindow.grid_columnconfigure(0, weight = 0)  # Left Panel
mainWindow.grid_columnconfigure(1, weight = 0)  # Separator
mainWindow.grid_columnconfigure(2, weight = 0)  # Statistics and results

leftFrame = tk.Frame(mainWindow, # Frame for mode selection and options
    width = 135,
    height = 785)
leftFrame.grid(row = 0, column = 0)
leftFrame.grid_rowconfigure(0, weight = 0)
leftFrame.grid_rowconfigure(1, weight = 0)
leftFrame.grid_rowconfigure(2, weight = 0)
leftFrame.grid_rowconfigure(3, weight = 0)


################################################################################
# Frame for selecting between automatic and manual mode

modeFrame = tk.Frame(leftFrame, # Frame for mode selection (manual vs automatic)
    width = 135,
    height = 95)
modeFrame.grid(row = 0, column = 0)
modeFrame.grid_propagate(0)

modeCanvas = tk.Canvas(modeFrame, width = 135, height = 35)
modeCanvas.create_text(8, 18, text = "Mode", anchor = tk.W)
modeCanvas.create_line(9, 26, 48, 26) # Creating line underneath Mode text
modeCanvas.grid(row = 0, column = 0)

mode = tk.IntVar() # the current mode being used (set to Automatic)
mode.set(1)


################################################################################
# Choices between automatic and manual mode

 # Radio button for Automatic Mode
choiceAuto = tk.Radiobutton(modeFrame, text = "Automatic",
    variable = mode,
    value = 1,
    command = lambda: op.disable_options(comboBoxList, resetOptionsButton, randomOptionsButton))
choiceAuto.grid(row = 1, column = 0, sticky = 'w')

# Radio button for Manual Mode
choiceMan = tk.Radiobutton(modeFrame, text = "Manual",
    variable = mode,
    value = 2,
    command = lambda: op.enable_options(comboBoxList, resetOptionsButton, randomOptionsButton))
choiceMan.grid(row = 2, column = 0, sticky = 'w')


################################################################################
# The separator between Mode Selection and Options

horizSeparator = tk.Frame(leftFrame,
    width = 135,
    height = 2,
    relief = 'groove',
    borderwidth = 5)
horizSeparator.grid(row = 1, column = 0)


################################################################################
# Frame in the left column, but under Mode Selection

optionsFrame = tk.Frame(leftFrame,
    width = 135,
    height = 785)
optionsFrame.grid(row = 2, column = 0)
optionsFrame.grid_propagate(0)

optionsCanvas = tk.Canvas(optionsFrame,
    width = 60,
    height = 35)
optionsCanvas.create_text(8, 18, text = "Options", anchor = tk.W)
optionsCanvas.create_line(9, 26, 60, 26) # Creating line underneath Options text
optionsCanvas.grid(row = 0, column = 0, sticky = 'w')

comboBoxList = op.create_options(optionsFrame) # Creating the options to use for manual selection


################################################################################
# Frame for options Reset and Random buttons

buttonFrame = tk.Frame(optionsFrame)
buttonFrame.grid(row = 0, column = 0, sticky = 'e')

reset = PhotoImage(file = 'reset.gif')
# helvSmall = font.Font(family = 'Helvetica', size = '9')
resetOptionsButton = tk.Button(buttonFrame,
    width = 20,
    height = 20,
    image = reset,
    command = lambda: reset_choices(comboBoxList))
resetOptionsButton.grid(row = 0, column = 0, sticky = 'e')

randomImage = PhotoImage(file = 'random.gif')
randomOptionsButton = tk.Button(buttonFrame,
    width = 20,
    height = 20,
    image = randomImage,
    command = lambda: random_choices(comboBoxList))
randomOptionsButton.grid(row = 0, column = 1, sticky = 'e')

# Disabling options by default since mode starts off as Automatic
op.disable_options(comboBoxList, resetOptionsButton, randomOptionsButton)


################################################################################
# Frame for vertical separator between options and statistics

verticalSeparator = tk.Frame(mainWindow,
    bg = 'white',
    width = 2,
    height = 785,
    relief = 'groove',
    borderwidth = 5)
verticalSeparator.grid(row = 0, column = 1, sticky = 'w')

################################################################################
# Frame for displaying results and notifications, in addition to the main menu

resultsFrame = tk.Frame(mainWindow,
    width = 1618,
    height = 785)
resultsFrame.grid(row = 0, column = 2, sticky = 'w')
resultsFrame.grid_propagate(0)
resultsFrame.grid_rowconfigure(0, weight = 1)
resultsFrame.grid_columnconfigure(0, weight = 1)

################################################################################
# Buttons underneath the option boxes

# Separator between buttons, to have some padding between them
buttonSeparator = tk.Frame(optionsFrame,
    bg = 'white',
    width = 135,
    height = 2,
    relief = 'groove',
    borderwidth = 5)
buttonSeparator.grid(row = 18, column = 0)

# Find flights button, to use one of the modes
findButton = tk.Button(optionsFrame,
    text = "Find Flights",
    width = 10,
    command = lambda: get_flights(mode, resultsFrame, flightList, comboBoxList))

# Separating the options boxes and the find flights button
buffer = tk.Frame(optionsFrame,
    height = 10,
    width = 10)
buffer.grid(row = 19, column = 0)

findButton.grid(row = 20, column = 0)


# To return to the main menu
mainMenuButton = tk.Button(optionsFrame,
    text = "Main Menu",
    width = 10,
    command = lambda: tf.to_main_menu(resultsFrame))

# Separating the find flights and main menu buttons
buffer2 = tk.Frame(optionsFrame,
    height = 8,
    width = 135)
buffer2.grid(row = 21, column = 0)

mainMenuButton.grid(row = 22, column = 0)


# Updating the data files for options
updateButton = tk.Button(optionsFrame,
    text = "Update Data",
    width = 10,
    command = lambda: op.update_options_lists())

# Separating the main menu and update buttons
buffer3 = tk.Frame(optionsFrame,
height = 8,
width = 135)
buffer3.grid(row = 23, column = 0)

updateButton.grid(row = 24, column = 0)


# Close the program
exitButton = tk.Button(optionsFrame,
    text = "Exit",
    width = 10,
    command = mainWindow.destroy)

# Separating the update and exit buttons
buffer4 = tk.Frame(optionsFrame,
    height = 8,
    width = 135)
buffer4.grid(row = 25, column = 0)

exitButton.grid(row = 26, column = 0)


tf.create_main_label(resultsFrame) # Creating the main menu text

mainWindow.mainloop() # Allowing the window to exist
