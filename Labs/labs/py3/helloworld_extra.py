'''Here's a less trivial lab, testing your knowledge of basic Python
object-oriented programming.

(Remember: if a method response has quotes around it, that means the
method returns a string.  If there are no quotes, that means it
printed (i.e., using print()).

>>> fido = Dog("Fido")
>>> fido.description()
'Fido the Dog'
>>> fido.speak()
'Woof!'

>>> fifi = Cat("Fifi")
>>> fifi.description()
'Fifi the Cat'
>>> fifi.speak()
'Meow!'

>>> nemo = Fish("Nemo")
>>> nemo.description()
'Nemo the Fish'
>>> nemo.speak()
''

>>> fifi.emote()
Fifi the Cat says: Meow!
>>> fido.emote()
Fido the Dog says: Woof!
>>> nemo.emote()
Nemo the Fish says: 

'''

# Write your code here:
class Animal:
    
    def __init__(self, name):
        self.name = name
        self.animal_type = ''
        self.speech = ''

    def description(self):
        return f"{self.name} the {self.animal_type}"        

    def speak(self):
        return self.speech

    def emote(self):
        print(f"{self.name} the {self.animal_type} says: {self.speak()}")        

class Dog(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)
        self.dog_init()
        
    def dog_init(self):
        self.animal_type = 'Dog'
        self.speech = 'Woof!'

class Cat(Animal):

    def __init__(self, name):
        Animal.__init__(self, name)
        self.cat_init()
        
    def cat_init(self):
        self.animal_type = 'Cat'
        self.speech = 'Meow!'

class Fish(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.fish_init()
        
    def fish_init(self):
        self.animal_type = 'Fish'
        self.speech = ''

# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
