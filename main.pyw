import os # For use with directories
import tkinter as tk # Main GUI capabilities
import pandas as pd # Main statistic and data tabulation capabilities
from modules import tkfunctions as tf # Custom TKinter functions

def openData():
    try:
        os.chdir('data')
        fileValues= pd.read_csv('2018_flight_data.csv')
        return fileValues
    except FileNotFoundError:
        tf.fileNotFoundPopup()

flightData = openData()

mainWindow = tk.Tk()
mainWindow.title("Project Prototype")
mainWindow.option_add("*Button.Background", "#d1d1d1")
mainWindow.option_add("*Button.Foreground", "#2b2b2b")
mainWindow.geometry("500x500")
mainWindow.resizable(0, 0)

frame = tk.Frame(master = mainWindow, bg = '#d1d1d1')
frame.pack(fill="both", expand=True)
frame.pack_propagate(0)

v = tk.IntVar()
v.set(1)

header = tk.Label(mainWindow, text = "Choose an option", justify = tk.LEFT, padx = 20)
header.pack()

choiceAuto = tk.Radiobutton(mainWindow, text = "Automatic",
    padx = 20,
    variable = v,
    value = 1)
choiceAuto.pack(anchor = tk.W)

choiceMan = tk.Radiobutton(mainWindow, text = "Manual",
    padx = 20,
    variable = v,
    value = 2)
choiceMan.pack(anchor = tk.W)

button = tk.Button(mainWindow, text = "Stop", width = 25)#mainWindow.destroy)
button.pack()

mainWindow.mainloop()
