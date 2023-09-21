from ast import Delete
from cProfile import label
from cgitb import text
import tkinter as tk
import math
import statistics

root = tk.Tk()

root.title("Data Types and Operations 2")

root.geometry('600x225')

var1 = 3.2
var2 = 4
var3 = 1.5
var4 = 3

varSubmit = tk.Button(root, text ="Submit", command = lambda:Submitvar(a = v11.get(1.0, tk.END), b = v21.get(1.0, tk.END), c = v31.get(1.0, tk.END), x = v41.get(1.0, tk.END)))
varSubmit.place(x=325, y=5, height = 25, width = 75)

varDefault = tk.Button(root, text ="Default", command = lambda:Defaultvar())
varDefault.place(x = 425, y = 5, height = 25, width = 75)

def Submitvar(a, b, c, x):
    global var1, var2, var3, var4
    var1 = float(a)
    var2 = float(b)
    var3 = float(c)
    var4 = float(x)

def Defaultvar():
    var1 = 3.2
    var2 = 4
    var3 = 1.5
    var4 = 3
    v11.delete(1.0, tk.END)
    v21.delete(1.0, tk.END)
    v31.delete(1.0, tk.END)
    v41.delete(1.0, tk.END)
    v11.insert(tk.END, var1)
    v21.insert(tk.END, var2)
    v31.insert(tk.END, var3)
    v41.insert(tk.END, var4)

v1 = tk.Label(root, text = "a = ")
v2 = tk.Label(root, text = "b = ")
v3 = tk.Label(root, text = "c = ")
v4 = tk.Label(root, text = "x = ")

v1.place(x = 80, y = 10)
v2.place(x = 135, y = 10)
v3.place(x = 190, y = 10)
v4.place(x = 245, y = 10)

v11 = tk.Text(root, height = 1, width = 3, bg = "white")
v21 = tk.Text(root, height = 1, width = 3, bg = "white")
v31 = tk.Text(root, height = 1, width = 3, bg = "white")
v41 = tk.Text(root, height = 1, width = 3, bg = "white")

v11.place(x = 115, y = 10, anchor='n')
v21.place(x = 170, y = 10, anchor='n')
v31.place(x = 225, y = 10, anchor='n')
v41.place(x = 280, y = 10, anchor='n')

v11.insert(tk.END, "3.2")
v21.insert(tk.END, "4")
v31.insert(tk.END, "1.5")
v41.insert(tk.END, "3")





task1 = tk.Label(root, text = "Task 1:  b^2 - 4ac  = ")
task1.place(x = 20, y = 50)

def calculate1():
    v11.destroy()
    global task1
    task1result = (var2 * var2) - ((4 * var1) * var3)
    task1result = round(task1result, 2)
    task1.configure(text="")
    task1 = tk.Label(root, text = "Task 1:  b^2 - 4ac  = " + str(task1result))
    task1.place(x = 20, y = 50)

task1button = tk.Button(root, text ="Calculate", command = lambda:calculate1())
task1button.place(x = 210, y = 45, height = 25, width = 75)






task2 = tk.Label(root, text = "Task 2:  a + c - b^2  = ")
task2.place(x = 295, y = 50)

def calculate2():
    task2result = (var1 + var3 - (var2 * var4))
    task2result = round(task2result, 0)
    task2 = tk.Label(root, text = "Task 2:  a + c - b^2  = " + str(task2result))
    task2.place(x = 295, y = 50)

task2button = tk.Button(root, text ="Calculate", command = lambda:calculate2())
task2button.place(x = 500, y = 45, height = 25, width = 75)





task3 = tk.Label(root, text = "Task 3:  a + b / c + x  = ")
task3.place(x = 20, y = 85)

def calculate3():
    task3result = ((var1 + var2) / (var3 + var4))
    task3result = round(task3result, 2)
    task3 = tk.Label(root, text = "Task 3:  a + b / c + x  = " + str(task3result))
    task3.place(x = 20, y = 85)

task3button = tk.Button(root, text ="Calculate", command = lambda:calculate3())
task3button.place(x = 210, y = 80, height = 25, width = 75)





task4 = tk.Label(root, text = "Task 4:  1 / (1 + x^2)  = ")
task4.place(x = 295, y = 85)

def calculate4():
    task4result = (1 / (1 + (var4 ** 2)))
    task4result = float(task4result)
    task4 = tk.Label(root, text = "Task 4:  1 / 1 + x^2  = " + str(task4result))
    task4.place(x = 295, y = 85)

task4button = tk.Button(root, text ="Calculate", command = lambda:calculate4())
task4button.place(x = 500, y = 80, height = 25, width = 75)





task5 = tk.Label(root, text = "Task 5:  -x(b - 5c)  = ")
task5.place(x = 20, y = 120)

def calculate5():
    task5result = (-var4 * (var2 - (5 * var3)))
    task5result = int(task5result)
    task5 = tk.Label(root, text = "Task 5:  -x(b - 5c)  = " + str(task5result))
    task5.place(x = 20, y = 120)

task5button = tk.Button(root, text ="Calculate", command = lambda:calculate5())
task5button.place(x = 210, y = 115, height = 25, width = 75)





task6 = tk.Label(root, text = "Task 6:  ac/4  = ")
task6.place(x = 295, y = 120)

def calculate6():
    task6result = ((var1 * var3) / 4)
    task6result = round(task6result, 1)
    task6 = tk.Label(root, text = "Task 6:  ac/4  = " + str(task6result))
    task6.place(x = 295, y = 120)

task6button = tk.Button(root, text ="Calculate", command = lambda:calculate6())
task6button.place(x = 500, y = 115, height = 25, width = 75)





task7 = tk.Label(root, text = "Task 7:  ac / x  = ")
task7.place(x = 20, y = 155)

def calculate7():
    task7result = ((var1 * var3) / var4)
    task7result = round(task7result, 1)
    task7 = tk.Label(root, text = "Task 7:  ac / x  = " + str(task7result))
    task7.place(x = 20, y = 155)

task7button = tk.Button(root, text ="Calculate", command = lambda:calculate7())
task7button.place(x = 210, y = 150, height = 25, width = 75)





task8 = tk.Label(root, text = "Task 8:  x % c  = ")
task8.place(x = 295, y = 155)

def calculate8():
    task8result = (var4 % var3)
    task8result = round(task8result, 1)
    task8 = tk.Label(root, text = "Task 8:  x % c  = " + str(task8result))
    task8.place(x = 295, y = 155)

task8button = tk.Button(root, text ="Calculate", command = lambda:calculate8())
task8button.place(x = 500, y = 150, height = 25, width = 75)





task9 = tk.Label(root, text = "Task 9:  (7/c + b%a)x  = ")
task9.place(x = 20, y = 190)

def calculate9():
    task9result = ((7 / var3) + (var2 % var1) * var4)
    task9result = round(task9result)
    task9 = tk.Label(root, text = "Task 9:  (7/c + b%a)x  = " + str(task9result))
    task9.place(x = 20, y = 190)

task9button = tk.Button(root, text ="Calculate", command = lambda:calculate9())
task9button.place(x = 210, y = 185, height = 25, width = 75)





task10 = tk.Label(root, text = "Task 10:  5x(a - c)  / -b  = ")
task10.place(x = 295, y = 190)

def calculate10():
    task10result = (((5 * var4) * (var1 - var3)) / -var2)
    task10result = round(task10result, 1)
    task10 = tk.Label(root, text = "Task 10:  5x(a - c)  / -b  = " + str(task10result))
    task10.place(x = 295, y = 190)

task10button = tk.Button(root, text ="Calculate", command = lambda:calculate10())
task10button.place(x = 500, y = 185, height = 25, width = 75)


root.mainloop()