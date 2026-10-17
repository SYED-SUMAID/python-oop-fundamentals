class Animal():
    def eat(self):
        print ("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("dog is barking")

dog = Dog() 

dog.eat()
dog.bark()