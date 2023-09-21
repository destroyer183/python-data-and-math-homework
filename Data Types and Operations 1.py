from cProfile import label
from cgitb import text
import tkinter as tk
import math
import statistics

root = tk.Tk()

root.title("Data Types and Operations 1")

root.geometry('250x75')

minimum = min(1, 7, -4, -100, 4, 2)

task0 = tk.Label(root, text = "Minimum of 1, 7, -4, -100, 4, and 2:")
task0.place(x = 20, y = 10)

task1 = tk.Label(root, text = minimum)
task1.place(x = 20, y = 30)

root.mainloop()