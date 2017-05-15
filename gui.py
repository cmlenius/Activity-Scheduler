from tkinter import *
from tkinter import ttk

class Window(Frame):
    def __init__(self, win, entries, variables, buttons, listbox):
        variables = [[],[]]
        entries = [[],[]]
        buttons = []

        # Labels
        la = Label(win, text="AM size").grid(row=0, column=1)
        lb = Label(win, text="PM size").grid(row=0, column=2)
        l0 = Label(win, text="Archery").grid(row=1)
        l1 = Label(win, text="Arts&Crafts").grid(row=2)
        l2 = Label(win, text="Canoeing").grid(row=3)
        l3 = Label(win, text="Drama").grid(row=4)
        l4 = Label(win, text="Kayaking").grid(row=5)
        l5 = Label(win, text="Photography").grid(row=6)
        l6 = Label(win, text="Rowing").grid(row=7)
        l7 = Label(win, text="Sailing").grid(row=8)
        l8 = Label(win, text="Sports").grid(row=9)
        l9 = Label(win, text="Swimming").grid(row=10)
        l10 = Label(win, text="Wilderness").grid(row=11)
        l11 = Label(win, text="Windsurfing").grid(row=12)
        l12 = Label(win, text="Woodworking").grid(row=13)
        l13 = Label(win, text="Fishing").grid(row=14)
        l14 = Label(win, text="Other" ).grid(row=15)

        # String Variables (default = 0)
        for i in range(15):
            variables[0].append(StringVar())
            variables[1].append(StringVar())
            variables[0][i].set(0)
            variables[1][i].set(0)
        variables.append(IntVar())

        # Entries
        for i in range(15):
            entries[0].append(Entry(win, textvariable=variables[0][i]).grid(row=i+1,column=1))
            entries[1].append(Entry(win, textvariable=variables[1][i]).grid(row=i+1,column=2))

        # Buttons
        buttons.append(Button(win, text="Schedule"))
        buttons[0].grid(row=16, column=1)
        buttons.append(Button(win, text="Quit"))
        buttons[1].grid(row=16, column=2)
        #buttons[1].config(command=quit)
        # Checkbutton
        buttons.append(Checkbutton(win, text="Default", variable=variables[2]))
        buttons[2].grid(row=16,column=0)
        variables[2].set(1)

        # Listbox
        lb = Listbox(win, width=50, height=20)
        lb.grid(row=17, column=0, columnspan=3, pady=(10,10))
        lb.insert(END, "Check 'READ_ME.txt' for instructions.")

        self.variables = variables
        self.entries = entries
        self.buttons = buttons
        self.listbox = lb

        return
