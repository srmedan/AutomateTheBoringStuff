class Car():
    """A simple attempt to model a car"""

    def __init__(self, make, model, year):
        """Initialize car attributes"""
        self.make = make
        self.model = model
        self.year = year

        #Fuel capacity and level in liters.
        self.fuel_capacity = 15
        self.fuel_level = 0

        #Capacity of seats in car
        self.persons_capacity = 5
        self.persons_current = 1

    def fill_tank(self):
        """Fill gas tank to capaciy."""
        self.fuel_level = self.fuel_capacity
        print('Fuel tank is full.')

    def honk(self):
        """ Honks the horn."""
        print("HONK! HONK! HONK!")

    def add_person(self):
        self.persons_current = self.persons_current + 1
        if self.persons_current >= self.persons_capacity:
            print("The car is full! There are currenly so many people in the car" + self.persons_current)

Car.add_person()