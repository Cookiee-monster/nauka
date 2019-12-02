class Allergies(object):

    def __init__(self, score):
        self.score = score
        self.score_bin = bin(score)
        self.alergens_list = [
            "eggs",
            "peanuts",
            "shellfish",
            "strawberries",
            "tomatoes",
            "chocolate",
            "pollen",
            "cats"]


    def allergic_to(self, item):
        self.item = item
        try:
            if len(self.score_bin) - 2 < self.alergens_list.index(self.item) + 1:
                return False
            elif self.score_bin[-1 - self.alergens_list.index(self.item)] == str(1):
                return True
            else:
                return False
        except:
            raise ValueError("There is no such an item in the allergen list")


    @property
    def lst(self):
        self.result_list = []
        for bit_position in range(0, min(8, len(self.score_bin) - 2)):
            if self.score_bin[-1 - bit_position] == str(1):
                self.result_list.append(self.alergens_list[bit_position])
        return self.result_list

print(Allergies(255).lst)