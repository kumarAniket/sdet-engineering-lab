class Dog:

    species = 'mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    def bark(self, age):
        print("Woof!! My name is {} and I'm a {} and I'm {} years old".format(self.name, self.breed, age))



my_dog = Dog(breed="Dachshund",name="Scooby")
my_dog.bark(10)

class Circle:
    pi=3.14

    def __init__(self,radius=1):
        self.radius=radius
        self.area = radius*radius*Circle.pi

    def get_circumference(self):
        return self.pi*self.radius*2

my_circle = Circle(30)
print("Circumference --> {}".format(my_circle.get_circumference()))
print("Area --> {}".format(my_circle.area))

print()
# Inheritance
class Animal:
    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I'm an animal")
    def eat(self):
        print("I'm eating")

class DogInheritance(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("Woof!!")

    def who_am_i(self):
        print("I'm a dog")

my_dog = DogInheritance()
my_dog.who_am_i()
my_dog.eat()
my_dog.bark()

print()
# Polymorphism
class Lion:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says roar!"


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"

niko=Lion("niko")
bailey=Cat("bailey")

print(niko.speak())

def pet_speak(pet):
    print(pet.speak())

pet_speak(bailey)
print()
# Abstract Class & Inheritance
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

class Snake(Animal):
    def speak(self):
        return self.name + " says hiss!!"

class Pig(Animal):
    def speak(self):
        return self.name + " says oink!!"

askaban = Snake("Askaban")
piggy = Pig("Piggy")

print(askaban.speak())
print(piggy.speak())

print()
# Special Functions
my_list = [1,2,3]
print("List Length --> {}".format(len(my_list)))

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book object is deleted")

b = Book('Python Rocks', 'Aniket', 275)
print(f"{str(b)} with a total of {len(b)} pages")

del b