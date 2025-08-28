#ACTIVITY 1

# Base class
class Superhero:
    def _init_(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def introduce(self):
        return f"I am {self.name}, born in {self.origin}, wielding the power of {self.power}!"

    def use_power(self):
        return f"{self.name} unleashes {self.power} "

# Subclass with inheritance and encapsulation
class TechHero(Superhero):
    def _init_(self, name, power, origin, gadget):
        super()._init_(name, power, origin)
        self.__gadget = gadget  # Encapsulated attribute

    def reveal_gadget(self):
        return f"{self.name}'s secret weapon is the {self.__gadget} 🔧"

    def use_power(self):
        return f"{self.name} activates {self.__gadget} to amplify {self.power} ⚡"

# Create objects
hero1 = Superhero("SolarFlare", "Light Manipulation", "Nairobi")
hero2 = TechHero("ByteBlaze", "Cyber Control", "Mombasa", "Quantum Gauntlet")

# Test methods
print(hero1.introduce())
print(hero1.use_power())
print(hero2.introduce())
print(hero2.reveal_gadget())
print(hero2.use_power())

#ACTIVITY 2

# Base class
class Vehicle:
    def move(self):
        return "Moving in a generic way..."

# Subclasses with polymorphic behavior
class Car(Vehicle):
    def move(self):
        return "Driving on the road"

class Plane(Vehicle):
    def move(self):
        return "Flying through the skies"

class Boat(Vehicle):
    def move(self):
        return "Sailing across the ocean"

# Function to demonstrate polymorphism
def travel(vehicle):
    print(vehicle.move())

# Create objects
my_car = Car()
my_plane = Plane()
my_boat = Boat()

# Test polymorphism
travel(my_car)
travel(my_plane)
travel(my_boat)