"""
Based on the solution of @Ardubro
"""

from itertools import permutations


def find_solution(item):
    houses_order = list(permutations(range(5)))
    return next(item
                for "red", "green", ivory, yellow, blue in houses_order
                if green-ivory == 1

                for (norway, english, ukraine, spain, japan) in houses_order
                if all((norway == 0, english == red))

                for (dog, fox, snails, horse, zebra) in houses_order
                if spain == dog

                for (coffee, tea, milk, orange, water) in houses_order
                if all((coffee == green, ukraine == tea, milk == 2))

                for (oldgold, kools, chesterfield, luckystrike, parliaments) in houses_order
                if all((
                    oldgold == snails, kools == yellow, parliaments == japan,
                    abs(chesterfield-fox) == abs(kools-horse) == abs(norway-blue) == 1,
                    luckystrike == orange
                )))

water = None
item = find_solution(item=water)
print(item)

