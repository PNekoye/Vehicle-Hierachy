"""
Vehicle Class Hierarchy
======================

This program implements a vehicle class hierarchy with inheritance and polymorphism.
It demonstrates OOP concepts including:
- Classes and Objects
- Constructors and Attributes
- Methods and Behaviors
- Inheritance
- Polymorphism
- Encapsulation
"""

class Vehicle:
    """Base class for all vehicles"""
    
    def __init__(self, make, model, year, color):
        """
        Initialize a Vehicle object
        
        Args:
            make (str): The manufacturer of the vehicle
            model (str): The model name/number
            year (int): The year the vehicle was manufactured
            color (str): The color of the vehicle
        """
        self.__make = make  # Encapsulated with private attribute
        self.__model = model  # Encapsulated with private attribute
        self.__year = year  # Encapsulated with private attribute
        self.__color = color  # Encapsulated with private attribute
        self.__is_running = False
        self.__speed = 0
        
    # Getters (for encapsulation)
    def get_make(self):
        """Get the vehicle's make"""
        return self.__make
        
    def get_model(self):
        """Get the vehicle's model"""
        return self.__model
        
    def get_year(self):
        """Get the vehicle's year"""
        return self.__year
        
    def get_color(self):
        """Get the vehicle's color"""
        return self.__color
        
    def get_speed(self):
        """Get the vehicle's current speed"""
        return self.__speed
        
    def is_running(self):
        """Check if the vehicle is running"""
        return self.__is_running
    
    # Setters (for encapsulation)
    def set_color(self, color):
        """
        Set the vehicle's color
        
        Args:
            color (str): The new color
        """
        self.__color = color
        print(f"Vehicle has been repainted to {color}")
    
    def set_speed(self, speed):
        """
        Set the vehicle's speed
        
        Args:
            speed (int): The new speed
        """
        if self.__is_running:
            self.__speed = speed
            print(f"Speed set to {speed}")
        else:
            print("Cannot set speed. Vehicle is not running.")
    
    # Methods
    def start(self):
        """Start the vehicle"""
        if not self.__is_running:
            self.__is_running = True
            print(f"The {self.__color} {self.__year} {self.__make} {self.__model} has started.")
        else:
            print("Vehicle is already running.")
    
    def stop(self):
        """Stop the vehicle"""
        if self.__is_running:
            self.__is_running = False
            self.__speed = 0
            print(f"The {self.__make} {self.__model} has stopped.")
        else:
            print("Vehicle is already stopped.")
    
    def move(self):
        """
        Move the vehicle (to be overridden by subclasses)
        This is the polymorphic method
        """
        if self.__is_running:
            print("The vehicle is moving in some way.")
        else:
            print("Cannot move. Vehicle is not running.")
    
    def __str__(self):
        """Return a string representation of the vehicle"""
        status = "running" if self.__is_running else "not running"
        return f"{self.__year} {self.__make} {self.__model} ({self.__color}) - {status}"


class Car(Vehicle):
    """Car class that inherits from Vehicle"""
    
    def __init__(self, make, model, year, color, num_doors, transmission_type):
        """
        Initialize a Car object
        
        Args:
            make (str): The manufacturer of the car
            model (str): The model name/number
            year (int): The year the car was manufactured
            color (str): The color of the car
            num_doors (int): Number of doors
            transmission_type (str): Type of transmission (automatic/manual)
        """
        # Call the parent class constructor
        super().__init__(make, model, year, color)
        
        # Add car-specific attributes
        self.__num_doors = num_doors
        self.__transmission_type = transmission_type
        self.__is_parked = True
    
    # Getters
    def get_num_doors(self):
        """Get the number of doors"""
        return self.__num_doors
    
    def get_transmission_type(self):
        """Get the transmission type"""
        return self.__transmission_type
    
    def is_parked(self):
        """Check if the car is parked"""
        return self.__is_parked
    
    # Car-specific methods
    def park(self):
        """Park the car"""
        if not self.__is_parked:
            self.__is_parked = True
            print(f"The {self.get_make()} {self.get_model()} is now parked.")
        else:
            print("The car is already parked.")
    
    def unpark(self):
        """Take the car out of park"""
        if self.__is_parked:
            self.__is_parked = False
            print(f"The {self.get_make()} {self.get_model()} is no longer parked.")
        else:
            print("The car is already in drive.")
    
    # Override the move method (polymorphism)
    def move(self):
        """Move the car by driving"""
        if not self.is_running():
            print("Cannot drive. Car is not running.")
            return
            
        if self.__is_parked:
            print("Cannot drive. Car is in park.")
            return
            
        print(f"The {self.get_color()} {self.get_make()} {self.get_model()} is driving on the road at {self.get_speed()} mph.")


class Boat(Vehicle):
    """Boat class that inherits from Vehicle"""
    
    def __init__(self, make, model, year, color, boat_type, length):
        """
        Initialize a Boat object
        
        Args:
            make (str): The manufacturer of the boat
            model (str): The model name/number
            year (int): The year the boat was manufactured
            color (str): The color of the boat
            boat_type (str): Type of boat (sailboat, speedboat, etc.)
            length (float): Length of the boat in feet
        """
        # Call the parent class constructor
        super().__init__(make, model, year, color)
        
        # Add boat-specific attributes
        self.__boat_type = boat_type
        self.__length = length
        self.__is_anchored = True
    
    # Getters
    def get_boat_type(self):
        """Get the boat type"""
        return self.__boat_type
    
    def get_length(self):
        """Get the boat length"""
        return self.__length
    
    def is_anchored(self):
        """Check if the boat is anchored"""
        return self.__is_anchored
    
    # Boat-specific methods
    def anchor(self):
        """Drop the anchor"""
        if not self.__is_anchored:
            self.__is_anchored = True
            print(f"The {self.get_make()} {self.get_model()} has dropped its anchor.")
        else:
            print("The boat is already anchored.")
    
    def raise_anchor(self):
        """Raise the anchor"""
        if self.__is_anchored:
            self.__is_anchored = False
            print(f"The {self.get_make()} {self.get_model()} has raised its anchor.")
        else:
            print("The anchor is already raised.")
    
    # Override the move method (polymorphism)
    def move(self):
        """Move the boat by sailing"""
        if not self.is_running():
            print("Cannot sail. Boat is not running.")
            return
            
        if self.__is_anchored:
            print("Cannot sail. Boat is anchored.")
            return
            
        print(f"The {self.get_color()} {self.get_boat_type()} is sailing on the water at {self.get_speed()} knots.")


class Airplane(Vehicle):
    """Airplane class that inherits from Vehicle"""
    
    def __init__(self, make, model, year, color, wingspan, max_altitude):
        """
        Initialize an Airplane object
        
        Args:
            make (str): The manufacturer of the airplane
            model (str): The model name/number
            year (int): The year the airplane was manufactured
            color (str): The color of the airplane
            wingspan (float): The wingspan in feet
            max_altitude (int): Maximum flying altitude in feet
        """
        # Call the parent class constructor
        super().__init__(make, model, year, color)
        
        # Add airplane-specific attributes
        self.__wingspan = wingspan
        self.__max_altitude = max_altitude
        self.__altitude = 0
        self.__is_grounded = True
    
    # Getters
    def get_wingspan(self):
        """Get the wingspan"""
        return self.__wingspan
    
    def get_max_altitude(self):
        """Get the maximum altitude"""
        return self.__max_altitude
    
    def get_altitude(self):
        """Get the current altitude"""
        return self.__altitude
    
    def is_grounded(self):
        """Check if the airplane is on the ground"""
        return self.__is_grounded
    
    # Airplane-specific methods
    def take_off(self):
        """Take off from the ground"""
        if self.is_running() and self.__is_grounded:
            self.__is_grounded = False
            self.__altitude = 1000  # Starting altitude after takeoff
            print(f"The {self.get_make()} {self.get_model()} has taken off and is now at {self.__altitude} feet.")
        elif not self.is_running():
            print("Cannot take off. Airplane engine is not running.")
        else:
            print("Already in the air.")
    
    def land(self):
        """Land the airplane"""
        if not self.__is_grounded:
            self.__is_grounded = True
            self.__altitude = 0
            print(f"The {self.get_make()} {self.get_model()} has landed safely.")
        else:
            print("Already on the ground.")
    
    def change_altitude(self, altitude):
        """
        Change the airplane's altitude
        
        Args:
            altitude (int): The new altitude in feet
        """
        if self.__is_grounded:
            print("Cannot change altitude while on the ground.")
            return
            
        if altitude > self.__max_altitude:
            print(f"Cannot exceed maximum altitude of {self.__max_altitude} feet.")
            return
            
        self.__altitude = altitude
        print(f"Changed altitude to {altitude} feet.")
    
    # Override the move method (polymorphism)
    def move(self):
        """Move the airplane by flying"""
        if not self.is_running():
            print("Cannot fly. Airplane engine is not running.")
            return
            
        if self.__is_grounded:
            print("Cannot fly. Airplane is on the ground.")
            return
            
        print(f"The {self.get_color()} {self.get_make()} {self.get_model()} is flying through the air at {self.get_speed()} mph and at an altitude of {self.__altitude} feet.")


def demonstrate_polymorphism(vehicles):
    """
    Demonstrate polymorphism by calling the same method on different objects
    
    Args:
        vehicles (list): A list of Vehicle objects
    """
    print("\n=== DEMONSTRATING POLYMORPHISM ===")
    for vehicle in vehicles:
        print(f"\n{vehicle}")
        vehicle.start()
        
        # For car
        if isinstance(vehicle, Car):
            vehicle.unpark()
            
        # For boat
        if isinstance(vehicle, Boat):
            vehicle.raise_anchor()
        
        # For airplane
        if isinstance(vehicle, Airplane):
            vehicle.take_off()
        
        vehicle.set_speed(50)
        vehicle.move()  # This is where polymorphism happens


def main():
    """Main function to test the vehicle classes"""
    # Create vehicle objects
    my_car = Car("Toyota", "Corolla", 2022, "red", 4, "automatic")
    my_boat = Boat("Yamaha", "242X", 2023, "white", "speedboat", 24.2)
    my_airplane = Airplane("Cessna", "172", 2020, "blue", 36.1, 14000)
    
    # Create a list of vehicles for polymorphism demonstration
    vehicles = [my_car, my_boat, my_airplane]
    
    # Demonstrate polymorphism
    demonstrate_polymorphism(vehicles)
    
    print("\n=== ADDITIONAL FUNCTIONALITY DEMONSTRATIONS ===")
    
    # Demonstrate car-specific functionality
    print("\nCar-specific actions:")
    my_car.park()
    my_car.set_color("blue")
    print(f"Car now has {my_car.get_num_doors()} doors and a {my_car.get_transmission_type()} transmission.")
    
    # Demonstrate boat-specific functionality
    print("\nBoat-specific actions:")
    my_boat.anchor()
    print(f"Boat is a {my_boat.get_length()} foot {my_boat.get_boat_type()}.")
    
    # Demonstrate airplane-specific functionality
    print("\nAirplane-specific actions:")
    my_airplane.change_altitude(5000)
    print(f"Airplane has a wingspan of {my_airplane.get_wingspan()} feet and a max altitude of {my_airplane.get_max_altitude()} feet.")
    my_airplane.land()
    
    print("\nFinal states:")
    for vehicle in vehicles:
        print(f"- {vehicle}")


if __name__ == "__main__":
    main()
