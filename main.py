
from tkinter import *  # used for making GUI application
from tkinter import ttk  # Themd TKinter is used for making GUI application
import random # used for generating random numbers
import time  # used for getting current time and date
import datetime # used for getting current time and date
from tkinter import messagebox  # used for showing message box in GUI application
import mysql.connector # used for connecting to MySQL database



class Hospital:
    def __init__(self,root):
        self.root = root 
        self.root.title("Hospital Management System") # set title of the window
        self.root.geometry("1350x700+0+0") # set size of the window


        lbltitle = Label(self.root , text = "Hospital Managment System" , font=("times new roman" , 50 , "bold") , bg = "black" , fg = "gold" , bd = 4 , relief = RIDGE)
        lbltitle.pack(side = TOP , fill = X)


root = Tk()
obj = Hospital(root)
root.mainloop()