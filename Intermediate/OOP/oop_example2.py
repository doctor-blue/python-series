class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Init pet')

    def show(self):
        print(f"I am {self.name} and I am {self.age}")

    def speak(self):
        print(f"I do'nt know what I say")


class Cat(Pet):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f"{self.name} meow")

    def show(self):
        super().show()
        print(f"I am {self.name} and I am {self.age} year old and I am {self.color}")


class Dog(Pet):
    def speak(self):
        print(f"{self.name} bark")


class Fish(Pet):
    pass


p = Pet("Tim", 5)
p.show()

cat = Cat("Bill", 6, "Orange")
cat.show()

dog = Dog("Jill", 4)
dog.show()

cat.speak()
