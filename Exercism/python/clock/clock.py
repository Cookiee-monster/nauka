class Clock(object):
    def __init__(self, hour, minute):
        self.time_in_minutes = int(hour) * 60 + int(minute)

    def __repr__(self):

        if self.time_in_minutes >= 0:
            if self.time_in_minutes // 60 > 24:
                self.hour = self.time_in_minutes // 60 % 24
            else:
                self.hour = self.time_in_minutes // 60
            self.minutes = self.time_in_minutes % 60
        else:
            if self.time_in_minutes < -1440:
                self.time_in_minutes = 1440 + self.time_in_minutes % -1440
            else: self.time_in_minutes += 1440
            self.hour = self.time_in_minutes // 60
            self.minutes = self.time_in_minutes % 60
        if self.hour <= 9:
            self.hour = "0" + str(self.hour)
        elif self.hour == 24:
            self.hour = "00"
        if self.minutes <= 9:
            self.minutes = "0" + str(self.minutes)

        return "{}:{}".format(self.hour, self.minutes)

    def __eq__(self, other):
        if self.__repr__() == other:
            return True
        else:
            return False

    def __add__(self, minutes):
        self.time_in_minutes += minutes
        return self.__repr__()
    def __sub__(self, minutes):
        self.time_in_minutes -= minutes
        return self.__repr__()