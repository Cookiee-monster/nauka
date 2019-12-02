class School(object):
    def __init__(self):
        self.student_dict = {}

    def add_student(self, name, grade):
        self.student_dict[name] = grade

    def roster(self):
        self.roster_list = []
        self.grades = set(self.student_dict.values())
        for i in self.grades:
            self.temp_roster = []
            for name, grade in self.student_dict.items():
                if grade == i:
                    self.temp_roster.append(name)
            self.roster_list += sorted(self.temp_roster)

        return self.roster_list

    def func(self, x):
        self.x = x
        return self.x[1]

    def grade(self, grade_number):
        self.grade_number = grade_number
        self.list_by_grades = []
        for name in self.student_dict:
            if self.student_dict[name] == self.grade_number:
                self.list_by_grades.append(name)
        return sorted(self.list_by_grades)