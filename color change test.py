from operator import index
from optparse import Option
from textwrap import fill
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import bs4 as bs
from bs4 import BeautifulSoup as bs
import requests
from setuptools import Command
from sqlalchemy import false
import pandas as pd
import time
import json

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("250x300-1200-400")
        #self.frame = tk.Frame(self.root)
        #self.frame.pack()

        # input field stored
        self.input_a = tk.StringVar()

        # input field
        input_color_changer = tk.OptionMenu(self.root, *Colours)
        input_color_changer.grid(row=0, column=0)

        button = tk.Button(self.root, text="Run", command=self.color_changer)
        button.grid(row=1, column=2)

        self.root.mainloop()


    def color_changer(self, input_color_changer): # PEP8: lower_case_names for methods/functions/variables
        input_color_changer2 = input_color_changer.get()

        if input_color_changer2 == "Black":
            print("BLACK") # CHANGE COLOR OF FRAME TO BLACK
            self.root['bg'] = 'black'
        if input_color_changer2 == "Blue":
            print("BLACK") # CHANGE COLOR OF FRAME TO BLACK
            self.root['bg'] = 'blue'
        if input_color_changer2 == "Green":
            print("BLACK") # CHANGE COLOR OF FRAME TO BLACK
            self.root['bg'] = 'Green'
        if input_color_changer2 == "Red":
            print("BLACK") # CHANGE COLOR OF FRAME TO BLACK
            self.root['bg'] = 'red'
        if input_color_changer2 == "White":
            print("BLACK") # CHANGE COLOR OF FRAME TO BLACK
            self.root['bg'] = 'white'
        if input_color_changer2 == "Yellow":
            print("BLACK") # CHANGE COLOR OF FRAME TO BLACK
            self.root['bg'] = 'yellow'
        if input_color_changer2 == "Magenta":
            print("BLACK") # CHANGE COLOR OF FRAME TO BLACK
            self.root['bg'] = 'magenta'


Colours =[
    
    "Blue",
    "Green",
    "Red",
    "White",
    "Yellow",
    "Magenta"

]



Main()