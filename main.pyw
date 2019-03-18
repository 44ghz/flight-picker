import os # For use with directories
import tkinter as tk # Main GUI capabilities
from tkinter import font # For changing fonts in widgets
from tkinter import ttk # Various other tkinter widgets (mainly combobox)
import pandas as pd # Main statistic and data tabulation capabilities
from modules import tkfunctions as tf # Custom TKinter functions
from modules import dataretrieval as dr # Custom data retrieval functions
from modules import options # To create the Options panel

mainWindow = tk.Tk() # Main tkinter window

mainWindow.title("Project Prototype")
mainWindow.option_add("*Button.Background", "#d1d1d1")
mainWindow.option_add("*Button.Foreground", "#2b2b2b")
mainWindow.geometry("550x570")
mainWindow.resizable(0, 0)

helv = font.Font(family = 'Helvetica', size = '8')
helvBold = font.Font(family = 'Helvetica', size = '11', weight = 'bold')

mainWindow.grid_rowconfigure(0, weight = 2)
mainWindow.grid_columnconfigure(0, weight = 0)  # Left Panel
mainWindow.grid_columnconfigure(1, weight = 1)  # Separator
mainWindow.grid_columnconfigure(2, weight = 10) # Statistics and results

leftFrame = tk.Frame(mainWindow, # Frame for mode selection and options
    bg = 'blue',
    width = 135,
    height = 570)
leftFrame.grid(row = 0, column = 0)
leftFrame.grid_rowconfigure(0, weight = 0)
leftFrame.grid_rowconfigure(1, weight = 0)
leftFrame.grid_rowconfigure(2, weight = 10)

###################################

modeFrame = tk.Frame(leftFrame, # Frame for mode selection (manual vs automatic)
    width = 135,
    height = 85)
modeFrame.grid(row = 0, column = 0)
modeFrame.grid_propagate(0)

modeCanvas = tk.Canvas(modeFrame, width = 135, height = 35)
modeCanvas.create_text(10, 20, text = "Mode", anchor = tk.W)
modeCanvas.create_line(11, 28, 50, 28) # Creating line for underneath Mode
modeCanvas.grid(row = 0, column = 0)


modeDefault = tk.IntVar() # Default option for the mode selection (set to Automatic)
modeDefault.set(1)

choiceAuto = tk.Radiobutton(modeFrame, text = "Automatic", # Radio button for Automatic Mode
    variable = modeDefault,
    value = 1)
choiceAuto.grid(row = 1, column = 0, sticky = 'w')

choiceMan = tk.Radiobutton(modeFrame, text = "Manual", # Radio button for Manual Mode
    variable = modeDefault,
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
    height = 570)
optionsFrame.grid(row = 2, column = 0)
optionsFrame.grid_propagate(0)

optionsCanvas = tk.Canvas(optionsFrame, width = 135, height = 35)
optionsCanvas.create_text(10, 20, text = "Options", anchor = tk.W)
optionsCanvas.create_line(11, 28, 62, 28) # Creating line for underneath Options
optionsCanvas.grid(row = 0, column = 0)

options.create_options(optionsFrame) # Creating the options to use for manual selection

###################################

separator = tk.Frame(mainWindow, # Frame for vertical separator between options and statistics
    bg = 'white',
    width = 2,
    height = 800,
    relief = 'groove',
    borderwidth = 5)
separator.grid(row = 0, column = 1, sticky = 'w')


mainWindow.mainloop()
