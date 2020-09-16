class Dog:
    def __init__(self, name, age=10):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} bark")

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age


# d = Dog("Kate", 15)
# d.bark()
# d2 = Dog("Build")
#
# print(d.age)

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_student):
        self.name = name
        self.max_student = max_student
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_student:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value / len(self.students)


s1 = Student("Tim", 18, 95)
s2 = Student("John", 17, 56)
s3 = Student("Bill", 20, 75)

course = Course('Science', 2)
course.add_student(s1)
course.add_student(s2)
# print(course.students[0].name)
print(course.get_average_grade())
print(course.add_student(s3))
