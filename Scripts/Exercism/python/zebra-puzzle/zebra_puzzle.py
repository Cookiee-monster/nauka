class House():
    def __init__(self, color="", nationality="", pet="", drink="", smoke=""):
        self.color = color
        self.nationality = nationality
        self.pet = pet
        self.drink = drink
        self.smoke = smoke


yellow_house = House(color="yellow", smoke="Kools", nationality="Norwegian", drink="water",pet="fox")
blue_house = House(color="blue", pet="horse", nationality="Ukrainian", drink="tea", smoke="Chesterfields")
red_house = House(drink="milk", color="red", nationality="English", pet="snail", smoke="Old Gold")
ivory_house = House(color="ivory", nationality="Spanish", pet="dog", drink="orange juice", smoke="Lucky Strike")
green_house = House(color="green", drink="coffee", nationality="Japanese", pet="zebra", smoke="Parliaments")


houses = [yellow_house, blue_house, red_house, ivory_house, green_house]


def drinks_water():
    for h in houses:
        if h.drink == "water":
            return h.nationality


def owns_zebra():
    for h in houses:
        if h.pet == "zebra":
            return h.nationality
