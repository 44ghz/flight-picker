import tkinter as tk # Main GUI capabilities
from tkinter import font # For changing fonts in widgets
from tkinter import ttk # Various other tkinter widgets (mainly combobox)
from tkinter import PhotoImage # For taskbar icon
from modules import tkfunctions as tf # Custom TKinter functions
from modules import dataretrieval as dr # Custom data retrieval functions
from modules import options # To create the Options panel
from modules import results
from ttkthemes import themed_tk

def callback(mode, resulstFrame, flightData): # The command to use when finding flights
    results.find_flights(mode, resultsFrame, flightData)

#mainWindow = tk.Tk() # Main tkinter window

mainWindow = themed_tk.ThemedTk()
mainWindow.set_theme('black')

flightData = dr.open_data('ProjectData.csv')

icon = PhotoImage(file = 'plane.gif') # The application icon
#mainWindow.iconphoto(True, icon) # Applying the icon to the window
mainWindow.title("Project Prototype") # The title of the GUI window
mainWindow.option_add("*Button.Background", "#d1d1d1") # Changing button colors
mainWindow.option_add("*Button.Foreground", "#2b2b2b")
mainWindow.geometry("1584x676") # Scale of the window
mainWindow.resizable(0, 0) # Cannot resize window (x, y)

mainWindow.grid_rowconfigure(0, weight = 2)
mainWindow.grid_columnconfigure(0, weight = 0)  # Left Panel
mainWindow.grid_columnconfigure(1, weight = 1)  # Separator
mainWindow.grid_columnconfigure(2, weight = 2)  # Statistics and results

leftFrame = tk.Frame(mainWindow, # Frame for mode selection and options
    width = 135,
    height = 676)
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

choiceAuto = tk.Radiobutton(modeFrame, text = "Automatic", # Radio button for Automatic Mode
    variable = mode,
    value = 1)
choiceAuto.grid(row = 1, column = 0, sticky = 'w')

choiceMan = tk.Radiobutton(modeFrame, text = "Manual", # Radio button for Manual Mode
    variable = mode,
    value = 2)
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
    height = 676)
optionsFrame.grid(row = 2, column = 0)
optionsFrame.grid_propagate(0)
optionsFrame.grid_rowconfigure(17, weight = 0)
optionsFrame.grid_rowconfigure(18, weight = 0)

optionsCanvas = tk.Canvas(optionsFrame, width = 135, height = 35)
optionsCanvas.create_text(8, 18, text = "Options", anchor = tk.W)
optionsCanvas.create_line(9, 26, 60, 26) # Creating line for underneath Options
optionsCanvas.grid(row = 0, column = 0)

options.create_options(optionsFrame, flightData) # Creating the options to use for manual selection

###################################

separator = tk.Frame(mainWindow, # Frame for vertical separator between options and statistics
    bg = 'white',
    width = 2,
    height = 676,
    relief = 'groove',
    borderwidth = 5)
separator.grid(row = 0, column = 1, sticky = 'w')

###################################

resultsFrame = tk.Frame(mainWindow,
    width = 1440,
    height = 676)
resultsFrame.grid(row = 0, column = 2)
resultsFrame.grid_rowconfigure(0, weight = 1)
resultsFrame.grid_columnconfigure(0, weight = 1)

#Find Flights button
findButton = tk.Button(optionsFrame,
    text = "Find Flights",
    command = lambda: callback(mode, resultsFrame, flightData))

buffer = tk.Label(optionsFrame, text = "") # To give some space between the last combo box and the button
buffer.grid(row = 17, column = 0)

findButton.grid(row = 18, column = 0)

mainWindow.mainloop()
