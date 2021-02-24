class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f'{self.name} bark!')


kate = Dog("Kate",2)
kate.bark()

print(kate.age)

build = Dog("Build",5)
build.bark()