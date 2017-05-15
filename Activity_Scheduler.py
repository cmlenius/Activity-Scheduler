from openpyxl import load_workbook
from camper import Camper
from gui import Window
from tkinter import *

my_dict = { 0: "Archery",
            1: "Arts&Crafts",
            2: "Canoeing",
            3: "Drama",
            4: "Kayaking",
            5: "Photography",
            6: "Rowing",
            7: "Sailing",
            8: "Sports",
            9: "Swimming",
            10: "Wilderness",
            11: "Windsurfing",
            12: "Woodworking",
            13: "Fishing",
            14: "Other"}

short_form = {  "Archery": "Arch",
                "Arts&Crafts": "Arts",
                "Canoeing": "Ca",
                "Drama": "Dr",
                "Kayaking": "Kay",
                "Photography": "Pho",
                "Rowing": "Row",
                "Sailing": "Sail",
                "Sports": "Spr",
                "Swimming": "Swim",
                "Wilderness": "Wild",
                "Windsurfing": "Wind",
                "Woodworking": "Wood",
                "Fishing": "Fish",
                "Other": "Other"}

activity_cap = {"Archery": 15,
                "Arts&Crafts": 10,
                "Canoeing": 14,
                "Drama": 10,
                "Kayaking": 11,
                "Photography": 10,
                "Rowing": 5,
                "Sailing": 8,
                "Sports": 30,
                "Swimming": 12,
                "Wilderness": 15,
                "Windsurfing": 10,
                "Woodworking": 10,
                "Fishing": 8,
                "Other": 100 }

# activity = (am, pm, am_cap, pm_cap, name)
arts = ([],[],0,0, "Arts&Crafts")
drama = ([],[],0,0, "Drama")
photography = ([],[],0,0, "Photography")
canoeing = ([],[],0,0, "Canoeing")
kayaking = ([],[],0,0, "Kayaking")
fishing = ([],[],0,0, "Fishing")
sailing = ([],[],0,0, "Sailing")
archery = ([],[],0,0, "Archery")
sports = ([],[],0,0, "Sports")
swimming = ([],[],0,0, "Swimming")
wilderness = ([],[],0,0, "Wilderness")
rowing = ([],[],0,0, "Rowing")
windsurfing = ([],[],0,0, "Windsurfing")
woodworking = ([],[],0,0, "Woodworking")
other = ([],[],0,0, "Other")

activity_list = [archery, arts, canoeing, drama, kayaking, photography, rowing, sailing, sports, swimming, wilderness, windsurfing, woodworking, fishing, other]
cabin_list = ["Fox", "Beaver", "Raccoon", "Squirrel", "Chipmunk", "Swallow", "Oriole", "Cardinal", "Finch", "Vireo", "Chickadee"]
cabins = [[],[],[],[],[],[],[],[],[],[],[]]
campers = []
missing = []

def resetActivities():
    campers[:] = []
    missing[:] = []
    for cabin in cabins:
        cabin[:] = []
    for activity in activity_list:
        activity = list(activity)
        activity[0][:] = []
        activity[1][:] = []
        activity[2] = 0
        activity[3] = 0
        activity = tuple(activity)

# CHOOSE ACTIVITIES
def create_activity_list():
    for camper in campers:
        add_activity(camper, camper.act_1)
    for camper in campers:
        add_activity(camper, camper.act_2)

def place_camper(camper, i, time):
    activity = my_dict[i]
    if(time == "am"):
        activity_list[i][0].append(camper.name)
        camper.add_am(activity)
    else:
        activity_list[i][1].append(camper.name)
        camper.add_pm(activity)

def add_activity(camper, activity):
    for i in range(15):
        if activity == my_dict[i]:
            if camper.am == False and len(activity_list[i][0]) < activity_list[i][2]:
                place_camper(camper, i, "am")
            elif camper.pm == False and len(activity_list[i][1]) < activity_list[i][3]:
                place_camper(camper, i, "pm")
            else:
                add_activity3(camper, camper.act_3)

def add_activity3(camper, activity):
    if camper.am == camper.act_3 or camper.pm == camper.act_3:
        return
    for i in range(15):
        if activity == my_dict[i]:
            if camper.am == False and len(activity_list[i][0]) < activity_list[i][2]:
                place_camper(camper, i, "am")
                camper.third = True
            elif camper.pm == False and len(activity_list[i][1]) < activity_list[i][3]:
                place_camper(camper, i, "pm")
                camper.third = True


# OPTIMIZE
def swap_and_add(camper, swap, add, time):
    # time = swap to that time
    if time == "am":
        activity_list[swap][1].remove(camper.name)
        activity_list[swap][0].append(camper.name)
        activity_list[add][1].append(camper.name)
        camper.add_am(my_dict[swap])
        camper.add_pm(my_dict[add])
    else:
        activity_list[swap][0].remove(camper.name)
        activity_list[swap][1].append(camper.name)
        activity_list[add][0].append(camper.name)
        camper.add_am(my_dict[add])
        camper.add_pm(my_dict[swap])
    #print("Fixed: " + camper.name)

def check_missing(camper):
    a = 0
    b = 0
    c = 0
    for i in range(14):
        if my_dict[i] == camper.act_1:
            a = i
        if my_dict[i] == camper.act_2:
            b = i
        if my_dict[i] == camper.act_3:
            c = i

    # check when camper has activity
    if camper.am == False:
        # check which activity camper has
        if camper.pm == camper.act_1:
            # check if space in AM and space for new activity in PM
            if len(activity_list[b][0]) < activity_list[b][2]:
                activity_list[b][0].append(camper.name)
                camper.add_am(my_dict[b])
            elif len(activity_list[c][0]) < activity_list[c][2]:
                activity_list[c][0].append(camper.name)
                camper.add_am(my_dict[c])
            elif len(activity_list[a][0]) < activity_list[a][2] and len(activity_list[b][1]) < activity_list[b][3]:
                swap_and_add(camper,a,b,"am")
            elif len(activity_list[a][0]) < activity_list[a][2] and len(activity_list[c][1]) < activity_list[c][3]:
                swap_and_add(camper,a,c,"am")
        elif camper.pm == camper.act_2:
            if len(activity_list[a][0]) < activity_list[a][2]:
                activity_list[a][0].append(camper.name)
                camper.add_am(my_dict[a])
            elif len(activity_list[c][0]) < activity_list[c][2]:
                activity_list[c][0].append(camper.name)
                camper.add_am(my_dict[c])
            elif len(activity_list[b][0]) < activity_list[b][2] and len(activity_list[c][1]) < activity_list[c][3]:
                swap_and_add(camper,b,c,"am")
    else:
        if camper.am == camper.act_1:
            # check if space in PM and space for new activity in AM
            if len(activity_list[b][1]) < activity_list[b][3]:
                activity_list[b][1].append(camper.name)
                camper.add_pm(my_dict[b])
            elif len(activity_list[c][1]) < activity_list[c][3]:
                activity_list[c][1].append(camper.name)
                camper.add_pm(my_dict[c])
            elif len(activity_list[a][1]) < activity_list[a][3] and len(activity_list[b][0]) < activity_list[b][2]:
                swap_and_add(camper,a,b,"pm")
            elif len(activity_list[a][1]) < activity_list[a][3] and len(activity_list[c][0]) < activity_list[c][2]:
                swap_and_add(camper,a,c,"pm")
        elif camper.am == camper.act_2:
            if len(activity_list[a][1]) < activity_list[a][3]:
                activity_list[a][1].append(camper.name)
                camper.add_pm(my_dict[a])
            elif len(activity_list[c][1]) < activity_list[c][3]:
                activity_list[c][1].append(camper.name)
                camper.add_pm(my_dict[c])
            elif len(activity_list[b][1]) < activity_list[b][3] and len(activity_list[c][0]) < activity_list[c][2]:
                swap_and_add(camper,b,c,"pm")

def check_thirds(camper):
    a = 0
    b = 0
    c = 0
    for i in range(14):
        if my_dict[i] == camper.act_1:
            a = i
        if my_dict[i] == camper.act_2:
            b = i
        if my_dict[i] == camper.act_3:
            c = i

    # if first choice is AM and third choice is PM
    if camper.am == camper.act_1 and camper.pm == camper.act_3:
        if len(activity_list[b][1]) < activity_list[b][3]:
            activity_list[c][1].remove(camper.name)
            activity_list[b][1].append(camper.name)
            camper.add_pm(my_dict[b])
            camper.third = False
# if room in first choice PM and second choice AM then switch first choice to PM and add second choice
        elif len(activity_list[a][1]) < activity_list[a][3] and len(activity_list[b][0]) < activity_list[b][2]:
            activity_list[a][0].remove(camper.name)
            activity_list[c][1].remove(camper.name)
            activity_list[a][1].append(camper.name)
            activity_list[b][0].append(camper.name)
            camper.add_am(my_dict[b])
            camper.add_pm(my_dict[a])
            camper.third = False
    # if first choice is PM and thrid choice is AM
    elif camper.am == camper.act_3 and camper.pm == camper.act_1:
        if len(activity_list[b][0]) < activity_list[b][2]:
            activity_list[c][0].remove(camper.name)
            activity_list[b][0].append(camper.name)
            camper.add_am(my_dict[b])
            camper.third = False
        # if room in first choice AM and second choice PM then switch first choice to AM and add second choice
        if len(activity_list[a][0]) < activity_list[a][2] and len(activity_list[b][1]) < activity_list[b][3]:
            activity_list[a][1].remove(camper.name)
            activity_list[c][0].remove(camper.name)
            activity_list[a][0].append(camper.name)
            activity_list[b][1].append(camper.name)
            camper.add_am(my_dict[a])
            camper.add_pm(my_dict[b])
            camper.third = False
            #print("Fixed: " + camper.name)

# schedule function
def schedule(default):
    my_dict_r = {v: k for k, v in my_dict.items()}
    activity_numbers = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    # GET INPUT from .xlsx file
    wb = load_workbook(filename='Activity Signup.xlsx')
    ws = wb['Sheet1']
    skip_first = True
    for row in ws.rows:
        if skip_first:
            skip_first = False
        elif row[1].value != None:
            campers.append(Camper(row[0].value, row[1].value, row[2].value, row[3].value, row[4].value, False, False, False))
            activity_numbers[my_dict_r[row[2].value]] += 1
            activity_numbers[my_dict_r[row[3].value]] += 1

    # CREATE ACTIVITY SIZES
    if(default == 1):
        k = 0
        am_pm = True
        for activity in activity_list:
            activity_list[k] = list(activity_list[k])
            num = activity_numbers[k]
            cap = activity_cap[activity[4]]
            am = 0
            pm = 0
            if num > 3:
                if num > 1 + cap:
                    am = cap
                    pm = cap
                elif am_pm:
                    am = cap
                    am_pm = False
                else:
                    pm = cap
                    am_pm = True
            activity_list[k][2] = am
            activity_list[k][3] = pm
            activity_list[k] = tuple(activity_list[k])
            k += 1

    # CHOOSE ACTIVITIES
    create_activity_list()

    # See if fixes can be made
    for camper in campers:
        if camper.am == False or camper.pm == False:
            check_missing(camper)
    for camper in campers:
        if camper.third == True:
            check_thirds(camper)

    # Second time in case first fix creates new openings
    for camper in campers:
        if camper.am == False or camper.pm == False:
            check_missing(camper)
    for camper in campers:
        if camper.third == True:
            check_thirds(camper)

    # Cabins
    for camper in campers:
        for i in range(11):
            if camper.cabin == cabin_list[i]:
                string = "%s: " % (camper.name)
                if camper.am == False:
                    string += "   /"
                else:
                    string += "%s/" %(short_form[camper.am])
                if camper.pm == False:
                    string += "    "
                else:
                    string += "%s" %(short_form[camper.pm])
                cabins[i].append(string)

    # OUTPUT to txt file
    file = open("ACTIVITY LIST.txt", "w")
    i = 0
    for activity in activity_list:
        #AM
        if len(activity[0]) != 0:
            file.write("Activity: ")
            file.write(my_dict[i])
            file.write(" AM - %d\n" % len(activity[0]))
            for name in activity[0]:
                file.write("   ")
                file.write(name)
                file.write("\n")
            file.write("\n")

        #PM
        if len(activity[1]) != 0:
            file.write("Activity: ")
            file.write(my_dict[i])
            file.write(" PM - %d\n" % len(activity[1]))
            for name in activity[1]:
                file.write("   ")
                file.write(name)
                file.write("\n")
            file.write("\n")
        i += 1
    file.close()
    file = open("CABIN LIST.txt", "w")
    i = 0
    for cabin in cabin_list:
        file.write(cabin)
        file.write(" - %d\n" % len(cabins[i]))
        for camper in cabins[i]:
            file.write(camper)
            file.write("\n")
        file.write("\n")
        i += 1
    file.close()

    for camper in campers:
        if camper.am == False or camper.pm == False:
            missing.append(camper)


def buttonClick(app):
    resetActivities()
    for i in range(15):
        activity_list[i] = list(activity_list[i])
        activity_list[i][2] = int(app.variables[0][i].get())
        activity_list[i][3] = int(app.variables[1][i].get())
        activity_list[i] = tuple(activity_list[i])
    schedule(app.variables[2].get())
    app.listbox.delete(0,END)
    app.listbox.insert(END, "The following campers are missing an activity!")
    app.listbox.insert(END, "")
    for camper in missing:
        string = "%s " % (camper.name)
        if camper.am == False:
            string += "MISSING / "
        else:
            string += "%s / " % (camper.am)
        if camper.pm == False:
            string += "MISSING"
        else:
            string += "%s" %(camper.pm)
        app.listbox.insert(END, string)

def quit(win):
    win.quit()

def main():
    # GUI setup
    win = Tk()
    win.title("Activity Scheduler")
    app = Window(win,[],[],[],False)
    app.buttons[0].configure(command=lambda: buttonClick(app))
    app.buttons[1].configure(command=lambda: quit(win))

    win.mainloop()


if __name__ == "__main__":main() # Maia Barnes
