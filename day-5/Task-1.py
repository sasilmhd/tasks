class Animal:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def speak(self):
        return  "Animal Sound"
class Dog(Animal):
    def speak(self):
        return "Bow Bow"
class Cat(Animal):
    def speak(self):
        return "Meow"
dog1=Dog("Bolt","Light Brown")
cat1=Cat("Ginger","orange")
print(dog1.speak())
print(cat1.speak())