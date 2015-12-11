__author__ = 'oucb'

__author__ = 'oucb'
## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    def eat_people(self):
        print "I want to know that do you eat people as food, 'yes' or 'no'."
        raw_input("> ")

## Dog is-a object of Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a object of Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name of
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

    def age(self):
        your_age = raw_input("Please input your age: ")
        print 'I know you are %d years old' %your_age

## Employee is-a object of Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):

    def color(self):
        my_color = raw_input("Please input what color do you like on your body:")
        print "You like %s" %my_color

## Salmon is-a object of Fish
class Salmon(Fish):
    pass

## Halibut is-a object of Fish
class Halibut(Fish):
    pass

## rover is-a Dog object named Rover
rover = Dog("Rover")

## satan is-a Cat object named Satan
satan = Cat("Satan")

## mary is-a Person object named Mary
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## frank is-a employee
frank = Employee("Frank", 120000)

## frank has-a pet named rover
frank.pet = rover

## flipper is-a fist
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()

a = Animal()
a.eat_people()
b = Dog('JACK')
b.eat_people()
