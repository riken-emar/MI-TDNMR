# -*- coding: utf-8 -*-
"""
 Copyright from: 11.17.2021
 CSRS, RIKEN
 Auther: Shunji Yamada
"""

import os
#import tkinter
#from PIL import Image
#import PIL.Image
#import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
#import subprocess
from demo_of_bayesian_optimization_multiple_y_GUI import *

def dirdialog_clicked_training_data():
    iDir = os.path.abspath(os.path.dirname(__file__))
    fTyp = [("csv file", "*.csv")]
    filename = filedialog.askopenfilename(filetype=fTyp, initialdir = iDir)
    entry1.set(filename)

def dirdialog_clicked_x_for_prediction():
    iDir = os.path.abspath(os.path.dirname(__file__))
    fTyp = [("csv file", "*.csv")]
    filename = filedialog.askopenfilename(filetype=fTyp, initialdir = iDir)
    entry2.set(filename)

def dirdialog_clicked_settings():
    iDir = os.path.abspath(os.path.dirname(__file__))
    fTyp = [("csv file", "*.csv")]
    filename = filedialog.askopenfilename(filetype=fTyp, initialdir = iDir)
    entry3.set(filename)

def dirdialog_clicked_Out():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    entry4.set(iDirPath)

def conductMain():
    text = ""

    filePath1 = entry1.get()
    filePath2 = entry2.get()
    filePath3 = entry3.get()
    dirPathOut = entry4.get()
    if filePath1:
        text += "File path (training_data):\t" + filePath1 + "\n"
    if filePath2:
        text += "File path (x_for_prediction):\t" + filePath2 + "\n"
    if filePath3:
        text += "File path (settings):\t" + filePath3 + "\n"
    if dirPathOut:
        text += "File path (Output):\t" + dirPathOut

    if text:
        #subprocess.run("python demo_of_bayesian_optimization_multiple_y_GUI.py")
        #subprocess.run("python demo_of_bayesian_optimization_multiple_y_GUI.py " + filePath1 +  " " + filePath2 + " " + filePath3 + " " + dirPathOut)
        module1(filePath1, filePath2, filePath3, dirPathOut) 
        #messagebox.showinfo("info", text)
        outList = os.listdir(dirPathOut)
    else:
        messagebox.showerror("error", "Please select path")

if __name__ == "__main__":
    # root
    root = Tk()
    root.title("Bayesian Optimization multiple GUI")
    root.geometry("500x300")


    # Select training_data FilePath
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid(row=0, column=1, sticky=E)

    IDirLabel = ttk.Label(frame1, text="training_data FilePath  >>", padding=(5, 2))
    IDirLabel.pack(side=LEFT)

    entry1 = StringVar()
    IDirEntry = ttk.Entry(frame1, textvariable=entry1, width=30)
    IDirEntry.pack(side=LEFT)

    IDirButton = ttk.Button(frame1, text="Dialog", command=dirdialog_clicked_training_data)
    IDirButton.pack(side=LEFT)



    # Select x_for_prediction FilePath
    frame2 = ttk.Frame(root, padding=10)
    frame2.grid(row=2, column=1, sticky=E)

    IFileLabel = ttk.Label(frame2, text="x_for_prediction FilePath >>", padding=(5, 2))
    IFileLabel.pack(side=LEFT)

    entry2 = StringVar()
    IFileEntry = ttk.Entry(frame2, textvariable=entry2, width=30)
    IFileEntry.pack(side=LEFT)

    IFileButton = ttk.Button(frame2, text="Dialog", command=dirdialog_clicked_x_for_prediction)
    IFileButton.pack(side=LEFT)

    # Select settings FilePath
    framesettings = ttk.Frame(root, padding=10)
    framesettings.grid(row=4, column=1, sticky=E)

    IFileLabel = ttk.Label(framesettings, text="settings FilePath >>", padding=(5, 2))
    IFileLabel.pack(side=LEFT)

    entry3 = StringVar()
    IFileEntry = ttk.Entry(framesettings, textvariable=entry3, width=30)
    IFileEntry.pack(side=LEFT)

    IFileButton = ttk.Button(framesettings, text="Dialog", command=dirdialog_clicked_settings)
    IFileButton.pack(side=LEFT)


    # Select Output Dir
    framesettings = ttk.Frame(root, padding=10)
    framesettings.grid(row=6, column=1, sticky=E)

    IFileLabel = ttk.Label(framesettings, text="Output Dir >>", padding=(5, 2))
    IFileLabel.pack(side=LEFT)

    entry4 = StringVar()
    IFileEntry = ttk.Entry(framesettings, textvariable=entry4, width=30)
    IFileEntry.pack(side=LEFT)

    IFileButton = ttk.Button(framesettings, text="Dialog", command=dirdialog_clicked_Out)
    IFileButton.pack(side=LEFT)

    # Buttons
    frame3 = ttk.Frame(root, padding=10)
    frame3.grid(row=7,column=1,sticky=W)

    button1 = ttk.Button(frame3, text="Submit", command=conductMain)
    button1.pack(fill = "x", padx=30, side = "left")

    #button2 = ttk.Button(frame3, text=("Close"), command=quit)
    #button2.pack(fill = "x", padx=30, side = "left")


    root.mainloop()