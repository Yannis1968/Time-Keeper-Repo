import csv
from athlete import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from popupMessage import *

participantsList = []
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
with open(file_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            ath = Athlete(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            participantsList.append(ath)
            line_count += 1


popupmessage("   All " + str(len(participantsList)) + " names have been saved")
