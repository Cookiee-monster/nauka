def equilateral(sides):
    if if_triangle(sides):
        if len(set(sides)) == 1:
            return True
        else:
            return False
    else:
        return False


def isosceles(sides):
    if if_triangle(sides):
        if len(set(sides)) in [1, 2]:
            return True
        else:
            return False
    else:
        return False


def scalene(sides):
    if if_triangle(sides):
        if len(set(sides)) == 3:
            return True
        else:
            return False
    else:
        return False


def if_triangle(sides):
    for side in sides:
        if side <= 0:
            return False
        if side > sum(sides) - side:
            return False
    return True
