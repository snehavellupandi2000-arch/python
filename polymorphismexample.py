class Cat:
    def speak(self):
        print("meow")

class Dog:
    def speak(self):
        print("woof")

animals = [Cat() , Dog ()]

for animal in animals:
    animal.speak()