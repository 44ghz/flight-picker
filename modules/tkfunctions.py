import tkinter as tk
import os
import pandas as pd
from tkinter import font
from tkinter import ttk
from tkinter import filedialog as fd
from modules import dataretrieval as dr

def fnf_popup():
    win = tk.Tk()
    win.title("File Error")

    fnfLabel = tk.Label(win, text = "The data file was not found.\n Please ensure the file 'ProjectData.csv' is present in the data folder.")
    fnfLabel.pack()

    fnfButton = tk.Button(text = "OK", command = win.destroy).pack()

class OptionsCombobox():
    def __init__(self, frame, list, row, column):
        self._frame = frame
        self._list = list
        self._row = row
        self._column = column
        self._state = 'readonly'
        self._default = "None"
        self._createBox()
        self._displayBox()

    def _createBox(self):
        self._box = ttk.Combobox(self._frame, values = self._list, state = self._state)
        self._box.set(self._default)

    def _displayBox(self):
        self._box.grid(row = self._row, column = self._column)
        self._box.config(width = 13, justify = tk.LEFT)
