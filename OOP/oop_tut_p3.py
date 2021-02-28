class Person:
    num_of_people = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.add_person()
    
    @classmethod
    def get_num_of_people(cls):
        return cls.num_of_people

    
    @classmethod
    def add_person(cls):
        cls.num_of_people +=1
    
    @staticmethod
    def add5(x):
        return x+5
    


# p1 = Person("Tim",15)
# p2 = Person("Jim",21)
# print(p1.num_of_people)
# # print(Person.num_of_people)
# print("==============")
# Person.num_of_people = 20
# print(p1.num_of_people)
# print(p2.num_of_people)
# print(Person.num_of_people)

# p1 = Person("Tim",15)
# print(Person.get_num_of_people())
# p2 = Person("Jim",21)
# print(Person.get_num_of_people())

print(Person.add5(10))