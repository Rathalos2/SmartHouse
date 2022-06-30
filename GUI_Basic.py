from operator import index
from optparse import Option
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

import bs4 as bs
from bs4 import BeautifulSoup as bs
import requests
from setuptools import Command
from sqlalchemy import false
import pandas as pd
import time
import json





root=tk.Tk()

root.title("Smart Home")
root.geometry("600x640")



f1 = tk.Frame(root, bg="#383B38", highlightbackground= "#146D21", highlightthickness=5, width=600, height=150, bd=15)
f2 = tk.Frame(root, bg="#383B38", highlightbackground="#146D21", highlightthickness=5, bd=15, width=600, height=150)
f3 = tk.Frame(root, bg="#383B38", highlightbackground="#146D21", highlightthickness=5, bd=10, width=600, height=340)

def do_layout():
    f1.grid(column=0, row= 0)
    f1.grid_propagate(False)
    f2.grid(column=0, row= 1)
    f2.grid_propagate(False)
    f3.grid(column=0, row= 2)
    f3.grid_propagate(False)

TV1= [
    "Online : 01:04:21"
    "Offline : 21:04:21"
    "Duration : 20 hours"
]

TV2= [
    "Online : 07:04:21"
    "Offline : 12:04:21"
    "Duration : 5 hours"
]

TV3= [
    "Online : 12:04:21"
    "Offline : 16:04:21"
    "Duration : 4 hours"
]


def do_labels():
    options1 = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
    ]


    options2 = [
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23"

    ]


    options3 = [
    "00",
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59"
    ]

  
    def showTV1():
        labelTV1.config(text="2 sata, 38 minuta i 12 sekundi")

    def showTV2():
        labelTV2.config(text="4 sata, 59 minuta i 25 sekundi")

    def showTV3():
        labelTV3.config(text="8 sata, 21 minuta i 43 sekundi")

    def showTVAll():
        labelTVAll.config(text="27 sati, 21 minuta i 43 sekundi")


    def TV1STATS():
        rule_window = Toplevel(root)
        rule_window.title("TV STATS")
        the_rules = Label(rule_window, text= TV1, foreground="black")
        the_rules.grid(row=0, column=0, columnspan=3)
    
    def TV2STATS():
        rule_window = Toplevel(root)
        rule_window.title("TV STATS")
        the_rules = Label(rule_window, text= TV2, foreground="black")
        the_rules.grid(row=0, column=0, columnspan=3)

    def TV3STATS():
        rule_window = Toplevel(root)
        rule_window.title("TV STATS")
        the_rules = Label(rule_window, text= TV3, foreground="black")
        the_rules.grid(row=0, column=0, columnspan=3)

    clicked1 = tk.StringVar(root)
    clicked2 = tk.StringVar(root)
    clicked3 = tk.StringVar(root)
    clicked4 = tk.StringVar(root)
    clicked5 = tk.StringVar(root)
    clicked6 = tk.StringVar(root)


    label1 = tk.Label(f1, text="TV1")
    label1.grid(row=0,column=0)
    button1=tk.Button(f1, text="ugasi")
    button1.grid(row=0,column=2)
    button4=tk.Button(f1, text="upali")
    button4.grid(row=0,column=3)
    buttonTV1=tk.Button(f1, text="Vrijeme koristenja", command = showTV1)
    buttonTV1.grid(row=0,column=4)
    labelTV1 = tk.Label(f1, text=" ")
    labelTV1.grid(row = 0, column=5)



    label2 = tk.Label(f1, text="TV2")
    label2.grid(row=1,column=0)
    button2=tk.Button(f1, text="ugasi")
    button2.grid(row=1,column=2)
    button5=tk.Button(f1, text="upali")
    button5.grid(row=1,column=3)

    buttonTV2=tk.Button(f1, text="Vrijeme koristenja", command = showTV2)
    buttonTV2.grid(row=1,column=4)
    labelTV2 = tk.Label(f1, text=" ")
    labelTV2.grid(row = 1, column=5)
    
    label3 = tk.Label(f1, text="TV3")
    label3.grid(row=2,column=0)
    button3=tk.Button(f1, text="ugasi")
    button3.grid(row=2,column=2)
    button6=tk.Button(f1, text="upali")
    button6.grid(row=2,column=3)
    buttonTV3=tk.Button(f1, text="Vrijeme koristenja", command = showTV3)
    buttonTV3.grid(row=2,column=4)
    labelTV3 = tk.Label(f1, text=" ")
    labelTV3.grid(row = 2, column=5)


    label4 = tk.Label(f1, text="Cijeli Sustav")
    label4.grid(row=8,column=0)
    button3=tk.Button(f1, text="ugasi")
    button3.grid(row=8,column=2)
    button6=tk.Button(f1, text="upali")
    button6.grid(row=8,column=3)
    buttonTVAll=tk.Button(f1, text="Vrijeme koristenja", command = showTVAll)
    buttonTVAll.grid(row=8,column=4)
    labelTVAll = tk.Label(f1, text=" ")
    labelTVAll.grid(row = 8, column=5)


    label5 = tk.Label(f2, text="Perilica ")
    label5.grid(row=0,column=0)
    button7=tk.Button(f2, text="ugasi odmah")
    button7.grid(row=0,column=1)
    button8=tk.Button(f2, text="upali odmah")
    button8.grid(row=0,column=2)


    label6 = tk.Label(f2, text="Postavi vrijeme početka ")
    label6.grid(row=2,column=0)


    drop1= tk.OptionMenu(f2,  clicked1, *options1)
    drop1.grid(row=2, column=1)
    
    drop2= tk.OptionMenu(f2,  clicked2, *options2)
    drop2.grid(row=2, column=2)
    
    drop3= tk.OptionMenu(f2,  clicked3, *options3)
    drop3.grid(row=2, column=3)
    
    

    label7 = tk.Label(f2, text="Postavi vrijeme završetka ")
    label7.grid(row=3,column=0)
    drop4= tk.OptionMenu(f2, clicked4, *options1)
    drop4.grid(row=3, column=1)
    drop5= tk.OptionMenu(f2, clicked5,  *options2)
    drop5.grid(row=3, column=2)
    drop6= tk.OptionMenu(f2, clicked6,  *options3)
    drop6.grid(row=3, column=3)
    button9=tk.Button(f2, text="Spremi postavke")
    button9.grid(row=4,column=1)

    labelStats1 = tk.Label(f3, text="TV1 STATS")
    labelStats1.grid(row=1,column=0)
    buttonStats1=tk.Button(f3, text="Get Stats", command=TV1STATS)
    buttonStats1.grid(row=1,column=2)

    labelStats2 = tk.Label(f3, text="TV2 STATS")
    labelStats2.grid(row=2,column=0)
    buttonStats2=tk.Button(f3, text="Get Stats", command=TV2STATS)
    buttonStats2.grid(row=2,column=2)

    labelStats3 = tk.Label(f3, text="TV3 STATS")
    labelStats3.grid(row=3,column=0)
    buttonStats3=tk.Button(f3, text="Get Stats", command=TV3STATS)
    buttonStats3.grid(row=3,column=2)


do_layout()
do_labels()

root.mainloop()

    
    
    
    
   