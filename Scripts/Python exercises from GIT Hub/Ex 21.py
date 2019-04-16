#! Python 3
# Question£º
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT
# with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from current position
# after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

import math as m

def input_robot_movements(direction):
    return int(input("Input the number of steps in {} direction:  ".format(direction)))

def distance(start_point, end_point):
    dist = m.sqrt((end_point[0]-start_point[0]) ** 2 + (end_point[1]-start_point[1]) ** 2)
    return print("The distance to the endpoint {} is {}".format(end_point, dist))

start_point = [0,0]
possible_directions  = ["UP", "DOWN", "LEFT", "RIGHT"]
list_of_steps = {}
while possible_directions:
    direction = possible_directions.pop(0)
    list_of_steps[direction] = input_robot_movements(direction)

end_point = [list_of_steps["UP"]-list_of_steps["DOWN"], list_of_steps["RIGHT"]-list_of_steps["LEFT"]]
distance(start_point, end_point)
