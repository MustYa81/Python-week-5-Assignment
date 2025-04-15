class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement the move() method")

class Dog(Animal):
    def move(self):
        print("The dog runs on four legs ")

class Bird(Animal):
    def move(self):
        print("The bird flies with wings")

class Fish(Animal):
    def move(self):
        print("The fish swims in the water ")

# Test polymorphism
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
