import tkinter as tk

mainWindow = tk.Tk()

v = tk.IntVar()
v.set(1)

tk.Label(mainWindow, text = "Choose an option", justify = tk.LEFT, padx = 20).pack()

tk.Radiobutton(mainWindow, text = "Automatic", padx = 20, variable = v, value = 1).pack(anchor = tk.W)
tk.Radiobutton(mainWindow, text = "Manual", padx = 20, variable = v, value = 2).pack(anchor = tk.W)

mainWindow.mainloop()
