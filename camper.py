class Camper:
    def __init__(self, name, cabin, act_1, act_2, act_3, am, pm, third):
        self.name = name
        self.cabin = cabin
        self.act_1 = act_1
        self.act_2 = act_2
        self.act_3 = act_3
        self.am = am
        self.pm = pm
        self.third = False
        return

    def add_am(self, activity):
        self.am = activity

    def add_pm(self, activity):
        self.pm = activity

    def print_camper(self):
        print("%s (%s): %s, %s, %s, || %s, %s" % (self.name, self.cabin, self.act_1, self.act_2, self.act_3, self.am, self.pm))
        return
