import tkinter as tk # Main GUI capabilities
import random # For random options
from tkinter import font # For changing fonts in widgets
from tkinter import ttk # Various other tkinter widgets (mainly combobox)
from tkinter import PhotoImage # For taskbar icon
from modules import tkfunctions as tf # Custom TKinter functions
from modules import dataretrieval as dr # Custom data retrieval functions
from modules import options as op # To create the Options panel
from modules import results # Creating the results from the user input
from ttkthemes import themed_tk # For window theme

def callback(mode, resultsFrame, flightList, comboBoxList): # The command to use when finding flights
    tf.clear_results(resultsFrame)

    userChoices = get_user_choices(comboBoxList)

    results.find_flights(mode, resultsFrame, flightList, userChoices)

def reset_choices(comboBoxList):
    for combobox in comboBoxList:
        combobox.reset()


def random_choices(comboBoxList):
    for comboBox in range(2):
        randomOption = random.randint(1, len(comboBoxList[comboBox].get_values()))
        comboBoxList[comboBox].set_current(randomOption)

    randomOption = random.randint(1, len(comboBoxList[7].get_values()))
    comboBoxList[7].set_current(randomOption)


def get_user_choices(comboBoxList):
    optionsDict = {}

    optionsDict["Distance"] = comboBoxList[0].get_current()
    optionsDict["Carrier"] = comboBoxList[1].get_current()
    optionsDict["Origin City"] = comboBoxList[2].get_current()
    optionsDict["Destination City"] = comboBoxList[3].get_current()
    optionsDict["Aircraft"] = comboBoxList[4].get_current()
    optionsDict["State Origin"] = comboBoxList[5].get_current()
    optionsDict["State Destination"] = comboBoxList[6].get_current()
    optionsDict["Month"] = comboBoxList[7].get_current()

    return optionsDict

mainWindow = themed_tk.ThemedTk()
mainWindow.set_theme('black')

# Opening the .csv and converting to DataFrame
flightData = dr.open_data('ProjectData.csv')

# Converting the DataFrame to a list representation, then ranking the flights by their score
flightList = results.rank_flights(dr.convert_df(flightData))

icon = PhotoImage(file = 'plane.gif') # The application icon
mainWindow.iconphoto(True, icon) # Applying the icon to the window
mainWindow.title("Flight Picker") # The title of the GUI window
mainWindow.option_add("*Button.Background", "#e0e0e0") # Changing button colors
mainWindow.option_add("*Button.Foreground", "#444444")
mainWindow.geometry("1695x785") # Scale of the window
mainWindow.resizable(0, 0) # Cannot resize window (x, y)

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

###################################

modeFrame = tk.Frame(leftFrame, # Frame for mode selection (manual vs automatic)
    width = 135,
    height = 95)
modeFrame.grid(row = 0, column = 0)
modeFrame.grid_propagate(0)

modeCanvas = tk.Canvas(modeFrame, width = 135, height = 35)
modeCanvas.create_text(8, 18, text = "Mode", anchor = tk.W)
modeCanvas.create_line(9, 26, 48, 26) # Creating line for underneath Mode
modeCanvas.grid(row = 0, column = 0)

mode = tk.IntVar() # the current mode being used (set to Automatic)
mode.set(1)

###################################

choiceAuto = tk.Radiobutton(modeFrame, text = "Automatic", # Radio button for Automatic Mode
    variable = mode,
    value = 1,
    command = lambda: op.disable_options(comboBoxList, resetOptionsButton, randomOptionsButton))
choiceAuto.grid(row = 1, column = 0, sticky = 'w')

choiceMan = tk.Radiobutton(modeFrame, text = "Manual", # Radio button for Manual Mode
    variable = mode,
    value = 2,
    command = lambda: op.enable_options(comboBoxList, resetOptionsButton, randomOptionsButton))
choiceMan.grid(row = 2, column = 0, sticky = 'w')

###################################

horizSeparator = tk.Frame(leftFrame, # The separator between Mode Selection and Options
    width = 135,
    height = 2,
    relief = 'groove',
    borderwidth = 5)
horizSeparator.grid(row = 1, column = 0)

###################################

optionsFrame = tk.Frame(leftFrame, # Frame in the left column, but under Mode Selection
    width = 135,
    height = 785)
optionsFrame.grid(row = 2, column = 0)
optionsFrame.grid_propagate(0)

optionsCanvas = tk.Canvas(optionsFrame,
    width = 60,
    height = 35)
optionsCanvas.create_text(8, 18, text = "Options", anchor = tk.W)
optionsCanvas.create_line(9, 26, 60, 26) # Creating line for underneath Options
optionsCanvas.grid(row = 0, column = 0, sticky = 'w')

comboBoxList = op.create_options(optionsFrame) # Creating the options to use for manual selection

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

op.disable_options(comboBoxList, resetOptionsButton, randomOptionsButton)
###################################

separator = tk.Frame(mainWindow, # Frame for vertical separator between options and statistics
    bg = 'white',
    width = 2,
    height = 785,
    relief = 'groove',
    borderwidth = 5)
separator.grid(row = 0, column = 1, sticky = 'w')

###################################

resultsFrame = tk.Frame(mainWindow,
    width = 1560,
    height = 785)
resultsFrame.grid(row = 0, column = 2, sticky = 'w')
resultsFrame.grid_propagate(0)
resultsFrame.grid_rowconfigure(0, weight = 1)
resultsFrame.grid_columnconfigure(0, weight = 1)


#Find Flights button
buttonSeparator = tk.Frame(optionsFrame, # Separator between criteria and buttons
    bg = 'white',
    width = 135,
    height = 2,
    relief = 'groove',
    borderwidth = 5)
buttonSeparator.grid(row = 18, column = 0)

findButton = tk.Button(optionsFrame, # To use one of the modes
    text = "Find Flights",
    width = 10,
    command = lambda: callback(mode, resultsFrame, flightList, comboBoxList))

mainMenuButton = tk.Button(optionsFrame,
    text = "Main Menu",
    width = 10,
    command = lambda: tf.to_main_menu(resultsFrame))

updateButton = tk.Button(optionsFrame, # Button to update the .dat files for options
    text = "Update Data",
    width = 10,
    command = lambda: op.update_options_lists(flightData))

exitButton = tk.Button(optionsFrame, # To close the program
    text = "Exit",
    width = 10,
    command = mainWindow.destroy)

buffer = tk.Frame(optionsFrame,
    height = 10,
    width = 10)
buffer.grid(row = 19, column = 0)

findButton.grid(row = 20, column = 0)

buffer2 = tk.Frame(optionsFrame,
    height = 8,
    width = 135)
buffer2.grid(row = 21, column = 0)

mainMenuButton.grid(row = 22, column = 0)

buffer3 = tk.Frame(optionsFrame,
height = 8,
width = 135)
buffer3.grid(row = 23, column = 0)

updateButton.grid(row = 24, column = 0)

buffer4 = tk.Frame(optionsFrame,
    height = 8,
    width = 135)
buffer4.grid(row = 25, column = 0)

exitButton.grid(row = 26, column = 0)

tf.create_main_label(resultsFrame)

mainWindow.mainloop()
