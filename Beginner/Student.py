from Human import Human

class Student(Human):

    def __init__(self, name, major, gpa, is_on_probation):
        super().__init__()
        self.name=name
        self.major=major
        self.gpa=gpa
        self.is_on_probation=is_on_probation
    
    def say_hi(self):
        if self.gpa>4:
            print("Đạt")
        else:
            print("Trượt")
    
