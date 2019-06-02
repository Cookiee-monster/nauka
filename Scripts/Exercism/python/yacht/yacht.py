# Score categories
# Change the values as you see fit
YACHT = "Yacht"
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = "Full_house"
FOUR_OF_A_KIND = "Four_of_a_kind"
LITTLE_STRAIGHT = "Little_straight"
BIG_STRAIGHT = "Big_straight"
CHOICE = "Choice"


def score(dice, category):
    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return category * len([x for x in dice if x == category])
    if category == "Yacht":
        if len(set(dice)) == 1:
            return 50
        else:
            return 0
    if category == "Full_house":
        if len(set(dice)) == 2:
            if sorted([dice.count(x) for x in set(dice)]) == [2,3]:
                return sum(dice)
            else:
                return 0
        else:
            return 0
    if category == "Four_of_a_kind":
        if len(set(dice)) == 2:
            if sorted([dice.count(x) for x in set(dice)]) == [1,4]:
                if sorted(dice)[0] != sorted(dice)[1]:
                    return sorted(dice)[1] * 4
                else:
                    return sorted(dice)[0] * 4
            else:
                return 0
        elif len(set(dice)) == 1:
            return dice[0] * 4
        else:
            return 0
    if category == "Little_straight":
        if sorted(set(dice)) == [1, 2, 3, 4, 5]:
            return 30
        else:
            return 0
    if category == "Big_straight":
        if sorted(set(dice)) == [2, 3, 4, 5, 6]:
            return 30
        else:
            return 0
    if category == "Choice":
        return sum(dice)
    pass
