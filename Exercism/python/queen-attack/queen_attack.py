class Queen(object):
    def __init__(self, row, column):
        if row not in range(0, 8):
            raise ValueError("Wrong row")
        elif column not in range(0, 8):
            raise ValueError("Wrong column")

        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Position of both queens cannot be the same")

        if self.column == another_queen.column:
            return True
        elif self.row == another_queen.row:
            return True
        elif self.row - self.column == another_queen.row - another_queen.column or \
                self.row + self.column == another_queen.row + another_queen.column:
            return True
        else:
            return False
