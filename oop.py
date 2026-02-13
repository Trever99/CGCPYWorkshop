#object oriented programming   
# class
# isinstance
# encapsulation
# inheritance
# polymorphism
# abstractions
# methods functions that belong to a class
# objects

class person:
    def __init__(self, name):
        self.name = name
        
    def printhello(self):
        print(f"Hello World {self.name}")
        
class student(person):
    def __init__(self, name, school):
        super().__init__(student, name)
        self.school = school  
        
simba = person("Simba")
trevor = person("trevor") #these are objects of the class person

trevor.printhello()
simba.printhello()

kalo = student("kalo", "CGCU")

kalo.printhello()
