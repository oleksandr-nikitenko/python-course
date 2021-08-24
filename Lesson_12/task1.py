"""
Method overloading.
Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat, and make their
own implementation of the method talk be different. For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be
to print ‘meow’.
Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method
on input parameter.
"""
from abc import abstractmethod


class Animal:
    @abstractmethod
    def talk(self):
        pass
    
    
class Cat(Animal):
    
    def __init__(self):
        self.name = 'cat'
    
    def talk(self) -> str:
        return 'meow'


class Dog(Animal):
    
    def __init__(self):
        self.name = 'dog'
    
    def talk(self) -> str:
        return 'woof woof'


def simple_function(animal: Animal):
    print(f'The {animal.name} says: {animal.talk()}.')


cat = Cat()
dog = Dog()
simple_function(cat)
simple_function(dog)
