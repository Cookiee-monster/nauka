class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix_as_a_list = []
        self.filling_the_list()

    def filling_the_list(self):
        for line in self.matrix_string.split("\n"):
            self.temp_list = line.split(" ")
            self.row_list = []
            for elem in self.temp_list:
                self.row_list.append(int(elem))
            self.matrix_as_a_list.append(self.row_list)

    def row(self, index):
        return self.matrix_as_a_list[index-1]

    def column(self, index):
        self.column_result_list = []
        for self.line in self.matrix_as_a_list:
            self.column_result_list.append(self.line[index - 1])
        return self.column_result_list