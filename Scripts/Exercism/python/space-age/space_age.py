class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth = self.seconds / 31557600

    def on_earth(self):
        return round(self.earth, 2)

    def on_mercury(self):
        self.mercury = round(self.earth, 2) / 0.2408467
        return round(self.mercury, 2)

    def on_venus(self):
        self.venus = self.earth / 0.61519726
        return round(self.venus, 2)

    def on_mars(self):
        self.mars = round(self.earth, 2) / 1.8808158
        return round(self.mars, 2)

    def on_jupiter(self):
        self.jupiter = round(self.earth, 2) / 11.862615
        return round(self.jupiter, 2)

    def on_saturn(self):
        self.saturn = round(self.earth, 2) / 29.447498
        return round(self.saturn, 2)

    def on_uranus(self):
        self.uranus = round(self.earth, 2) / 84.016846
        return round(self.uranus, 2)

    def on_neptune(self):
        self.neptune = round(self.earth, 2) / 164.79132
        return round(self.neptune, 2)
