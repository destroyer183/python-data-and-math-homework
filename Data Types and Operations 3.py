from cProfile import label
from cgitb import text
from re import A
import tkinter as tk
import math
import statistics

root = tk.Tk()

root.title("Data Types and Operations 2")

root.geometry('700x250')





a = 0
b = 0
g = 0
h = 0
w = 0
x = 0
y = 0
z = 0





task1 = tk.Label(root, text = "Task 1:  x = ")
task1.place(x = 20, y = 10)

task11 = tk.Label(root, text = "x*x*x = ")
task11.place(x = 20, y = 35)

task12 = tk.Label(root, text = "x type = ")
task12.place(x = 20, y = 60)

task13 = tk.Text(root, height = 1, width = 3, bg = "white")
task13.place(x=100, y=10, anchor='n')

task14 = tk.Text(root, height = 1, width = 5, bg = "white")
task14.place(x = 85, y = 35, anchor='n')

task15 = tk.Text(root, height = 1, width = 5, bg = "white")
task15.place(x = 90, y = 60, anchor='n')

def calculate1(var6):
    global x
    x = float(var6)
    task1result = (x * x * x)
    task1result = round(task1result, 2)
    task14.delete(1.0, tk.END)
    task14.insert(tk.END, task1result)
    task15.delete(1.0, tk.END)
    if type(task1result) == float:
        task15.insert(tk.END, "float")

task1button = tk.Button(root, text ="Calculate", command = lambda:calculate1(var6 = task13.get(1.0, tk.END)))
task1button.place(x = 125, y = 5, height = 25, width = 75)





task2 = tk.Label(root, text = "Task 2:  g = ")
task2.place(x = 250, y = 10)

task21 = tk.Label(root, text = "h = ")
task21.place(x = 250, y = 35)

task22 = tk.Label(root, text = "g + h = h: ")
task22.place(x = 250, y = 60)

task26 = tk.Label(root, text = "h type = ")
task26.place(x = 250, y = 85)

task28 = tk.Label(root, text = "g - 3 = g:")
task28.place(x = 250, y = 110)

task211 = tk.Label(root, text = "g type = ")
task211.place(x = 250, y = 135)

task231 = tk.Label(root, text = "h + g = h:")
task231.place(x = 250, y = 160)

task251 = tk.Label(root, text = "h type = ")
task251.place(x = 250, y = 185)

task23 = tk.Text(root, height = 1, width = 3, bg = "white")
task23.place(x=330, y=10, anchor='n')

task24 = tk.Text(root, height = 1, width = 3, bg = "white")
task24.place(x = 290, y = 35, anchor='n')

task25 = tk.Text(root, height = 1, width = 5, bg = "white")
task25.place(x = 330, y = 60, anchor='n')

task27 = tk.Text(root, height = 1, width = 5, bg = "white")
task27.place(x = 320, y = 85, anchor='n')

task29 = tk.Text(root, height = 1, width = 5, bg = "white")
task29.place(x = 325, y = 110, anchor='n')

task221 = tk.Text(root, height = 1, width = 5, bg = "white")
task221.place(x = 320, y = 135, anchor='n')

task241 = tk.Text(root, height = 1, width = 5, bg = "white")
task241.place(x = 330, y = 160, anchor='n')

task261 = tk.Text(root, height = 1, width = 5, bg = "white")
task261.place(x = 320, y = 185, anchor='n')

def calculate2(var3, var4):
    global g, h
    g = float(var3)
    h = float(var4)
    task2result = (g + h)
    task2result = round(task2result, 2)
    task25.delete(1.0, tk.END)
    task25.insert(tk.END, task2result)
    task27.delete(1.0, tk.END)
    if type(task2result) == float:
        task27.insert(tk.END, "float")
    task21result = (g - 3)
    task21result = round(task21result, 2)
    task29.delete(1.0, tk.END)
    task29.insert(tk.END, task21result)
    task221.delete(1.0, tk.END)
    if type(task21result) == float:
        task221.insert(tk.END, "float")
    task22result = (h + g)
    task22result = round(task22result, 2)
    task241.delete(1.0, tk.END)
    task241.insert(tk.END, task22result)
    task261.delete(1.0, tk.END)
    if type(task22result) == float:
        task261.insert(tk.END, "float")

task2button = tk.Button(root, text ="Calculate", command = lambda:calculate2(var3 = task23.get(1.0, tk.END), var4 = task24.get(1.0, tk.END)))
task2button.place(x = 355, y = 5, height = 25, width = 75)





task3 = tk.Label(root, text = "Task 3:  z = ")
task3.place(x = 480, y = 10)

task31 = tk.Label(root, text = "z + 2 = z:")
task31.place(x = 480, y = 35)

task32 = tk.Label(root, text = "z type = ")
task32.place(x = 480, y = 60)

task33 = tk.Text(root, height = 1, width = 3, bg = "white")
task33.place(x=560, y=10, anchor='n')

task34 = tk.Text(root, height = 1, width = 5, bg = "white")
task34.place(x = 560, y = 35, anchor='n')

task35 = tk.Text(root, height = 1, width = 5, bg = "white")
task35.place(x = 550, y = 60, anchor='n')

def calculate3(var6):
    global x
    x = float(var6)
    task3result = (x + 2)
    task3result = round(task3result, 2)
    task34.delete(1.0, tk.END)
    task34.insert(tk.END, task3result)
    task35.delete(1.0, tk.END)
    if type(task3result) == float:
        task35.insert(tk.END, "float")

task3button = tk.Button(root, text ="Calculate", command = lambda:calculate3(var6 = task33.get(1.0, tk.END)))
task3button.place(x = 585, y = 5, height = 25, width = 75)





task4 = tk.Label(root, text = "Task 4:  a = ")
task4.place(x = 20, y = 90)

task41 = tk.Label(root, text = "b = ")
task41.place(x = 20, y = 115)

task42 = tk.Label(root, text = "a / b = c:")
task42.place(x = 20, y = 140)

task46 = tk.Label(root, text = "a / b = d:")
task46.place(x = 20, y = 165)

task48 = tk.Label(root, text = "a % b = e:")
task48.place(x = 20, y = 190)

task411 = tk.Label(root, text = "c, d, e, type =")
task411.place(x = 20, y = 215)

task43 = tk.Text(root, height = 1, width = 3, bg = "white")
task43.place(x=100, y=90, anchor='n')

task44 = tk.Text(root, height = 1, width = 3, bg = "white")
task44.place(x = 60, y = 115, anchor='n')

task45 = tk.Text(root, height = 1, width = 5, bg = "white")
task45.place(x = 100, y = 140, anchor='n')

task47 = tk.Text(root, height = 1, width = 5, bg = "white")
task47.place(x = 100, y = 165, anchor='n')

task49 = tk.Text(root, height = 1, width = 5, bg = "white")
task49.place(x = 105, y = 190, anchor='n')

task421 = tk.Text(root, height = 1, width = 20, bg = "white")
task421.place(x = 180, y = 215, anchor='n')

def calculate4(var1, var2):
    global a, b
    a = float(var1)
    b = float(var2)
    task4result = (a / b)
    task4result = round(task4result, 2)
    task45.delete(1.0, tk.END)
    task45.insert(tk.END, task4result)
    task41result = (a / b)
    task41result = round(task41result, 2)
    task47.delete(1.0, tk.END)
    task47.insert(tk.END, task41result)
    task42result = (a % b)
    task42result = round(task42result, 2)
    task49.delete(1.0, tk.END)
    task49.insert(tk.END, task42result)
    task421.delete(1.0, tk.END)
    if type(task4result) and type(task41result) and type(task42result) == float:
        task421.insert(tk.END, "float, float, float")

task4button = tk.Button(root, text ="Calculate", command = lambda:calculate4(var1 = task43.get(1.0, tk.END), var2 = task44.get(1.0, tk.END)))
task4button.place(x = 125, y = 85, height = 25, width = 75)





task5 = tk.Label(root, text = "Task 5:  x = Hello")
task5.place(x = 480, y = 90)

task51 = tk.Label(root, text = "y = ")
task51.place(x = 480, y = 115)

task52 = tk.Label(root, text = "x + y = z:")
task52.place(x = 480, y = 140)

task53 = tk.Label(root, text = "z type = ")
task53.place(x = 480, y = 165)

task54 = tk.Label(root, text = "x * 3 = w:")
task54.place(x = 480, y = 190)

task55 = tk.Label(root, text = "w type =")
task55.place(x = 480, y = 215)

task56 = tk.Text(root, height = 1, width = 3, bg = "white")
task56.place(x = 520, y = 115, anchor='n')

task57 = tk.Text(root, height = 1, width = 5, bg = "white")
task57.place(x = 555, y = 140, anchor='n')

task58 = tk.Text(root, height = 1, width = 5, bg = "white")
task58.place(x = 550, y = 165, anchor='n')

task59 = tk.Text(root, height = 1, width = 15, bg = "white")
task59.place(x = 600, y = 190, anchor='n')

task511 = tk.Text(root, height = 1, width = 5, bg = "white")
task511.place(x = 552, y = 215, anchor='n')

def calculate5(var7):
    global x, y, z
    x = "Hello"
    y = str(var7)
    z = str
    task5result = (x + str(y))
    task57.delete(1.0, tk.END)
    task57.insert(tk.END, task5result)
    task58.delete(1.0, tk.END)
    if type(task5result) == str:
        task58.insert(tk.END, "str")
    task51result = (x * 3)
    task59.delete(1.0, tk.END)
    task59.insert(tk.END, task51result)
    task511.delete(1.0, tk.END)
    if type(task51result) == str:
        task511.insert(tk.END, "str")

task5button = tk.Button(root, text ="Calculate", command = lambda:calculate5(var7 = task56.get(1.0, tk.END)))
task5button.place(x = 585, y = 85, height = 25, width = 75)

root.mainloop()