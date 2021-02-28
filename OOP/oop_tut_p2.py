class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Init pet")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age}")

    def speak(self):
        print(f"I don't know what I say!")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color

    def show(self):
        super().show()
        print(f"{self.color} ")


cat = Cat("Bill",4,"Orange")
cat.show();
