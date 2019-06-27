# Globals for the bearings
# Change the values as you see fit

NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def simulate(self, orders):
        self.orders = orders
        for order in self.orders:
            if order == "R":
                self.turn_right()
            elif order == "L":
                self.turn_left()
            elif order == "A":
                self.advance()

    def advance(self):
        self.coordinates = (self.coordinates[0] + self.bearing[0], self.coordinates[1] + self.bearing[1])

    def turn_right(self):
        if self.bearing[1] == 1:
            self.bearing = EAST
        elif self.bearing[0] == 1:
            self.bearing = SOUTH
        elif self.bearing[1] == -1:
            self.bearing = WEST
        else:
            self.bearing = NORTH

    def turn_left(self):
        if self.bearing[1] == 1:
            self.bearing = WEST
        elif self.bearing[0] == 1:
            self.bearing = NORTH
        elif self.bearing[1] == -1:
            self.bearing = EAST
        else:
            self.bearing = SOUTH
