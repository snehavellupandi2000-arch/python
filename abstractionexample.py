from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass  # Must be defined in child classes


class Dog(Animal):

    def speak(self):
        print("woof")


dog = Dog()
dog.speak()