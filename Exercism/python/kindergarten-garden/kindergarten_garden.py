class Garden(object):
    def __init__(self, diagram, students="Alice Bob Charlie David Eve Fred Ginny\
                                          Harriet Ileana Joseph Kincaid Larry".split()):
        self.diagram = diagram.split("\n")
        self.students = sorted(students)
        self.plants_dict = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}

    def plants(self, name):
        self.name = name
        self.first_pot = self.students.index(self.name) * 2
        """Index of the proper pot based on the index
           of the student name index multiply by 2"""
        self.plants_per_name = []
        for row in range(0, 2):
            for pot in range(self.first_pot, self.first_pot + 2):
                self.plants_per_name.append(self.plants_dict[self.diagram[row][pot]])
        """appending the name of the plant 
           using the plant dict"""
        print(self.plants_per_name)
        return self.plants_per_name