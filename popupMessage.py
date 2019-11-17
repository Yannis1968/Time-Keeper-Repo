import tkinter as tk
from tkinter import ttk


class Popup:
    pass


LARGE_FONT = ("Verdana", 10)


def popupmessage(msg):
    popup = tk.Tk()

    width_of_popup = 400
    height_of_popup = 200
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width_of_popup / 2)
    y_coordinate = (screen_height / 2) - (height_of_popup / 2)

    popup.geometry("%dx%d+%d+%d" % (width_of_popup, height_of_popup, x_coordinate, y_coordinate))
    popup.wm_title("Success")
    popup.wm_iconbitmap('watch.ico')
    label = ttk.Label(popup, text=msg, font=LARGE_FONT, justify=tk.CENTER)
    label.pack(side="top",  pady=60, padx=40)
    b1 = ttk.Button(popup, text="Done", command=popup.destroy)
    b1.pack()
    popup.mainloop()