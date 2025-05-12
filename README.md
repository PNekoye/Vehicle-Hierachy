# Vehicle Class Hierarchy

This project implements a comprehensive vehicle class hierarchy to demonstrate key Object-Oriented Programming (OOP) concepts including classes, inheritance, polymorphism, and encapsulation.

## Project Overview

The program creates a base Vehicle class with several specialized vehicle subclasses (Car, Boat, and Airplane). Each vehicle type inherits common attributes and behaviors while implementing specialized functionality and demonstrating polymorphism through the `move()` method.

## Key Features

### OOP Concepts Demonstrated

- **Classes and Objects**: Structured representation of vehicles with attributes and behaviors
- **Inheritance**: Specialized vehicle types inheriting from a base Vehicle class
- **Polymorphism**: Common method names with different implementations across subclasses
- **Encapsulation**: Private attributes with getter/setter methods
- **Constructors**: Specialized initialization for each vehicle type
- **Method Overriding**: Subclasses implementing their own versions of methods

### Class Hierarchy

1. **Vehicle** (Base class)
   - Attributes: make, model, year, color, running status, speed
   - Methods: start, stop, move (polymorphic), getters/setters

2. **Car** (Inherits from Vehicle)
   - Additional attributes: number of doors, transmission type, parking status
   - Additional methods: park, unpark
   - Overrides: move (drives on road)

3. **Boat** (Inherits from Vehicle)
   - Additional attributes: boat type, length, anchor status
   - Additional methods: anchor, raise_anchor
   - Overrides: move (sails on water)

4. **Airplane** (Inherits from Vehicle)
   - Additional attributes: wingspan, max altitude, current altitude, ground status
   - Additional methods: take_off, land, change_altitude
   - Overrides: move (flies through air)

## Code Structure

The code is organized into:
- A base Vehicle class with core functionality
- Three specialized vehicle subclasses
- A demonstration function showing polymorphism
- A main function to test the classes

## Running the Program

To run the program, simply execute:

```
python vehicle_classes.py
```

## Sample Output

```
=== DEMONSTRATING POLYMORPHISM ===

2022 Toyota Corolla (red) - not running
The red 2022 Toyota Corolla has started.
The Toyota Corolla is no longer parked.
Speed set to 50
The red Toyota Corolla is driving on the road at 50 mph.

2023 Yamaha 242X (white) - not running
The white 2023 Yamaha 242X has started.
The Yamaha 242X has raised its anchor.
Speed set to 50
The white speedboat is sailing on the water at 50 knots.

2020 Cessna 172 (blue) - not running
The blue 2020 Cessna 172 has started.
The Cessna 172 has taken off and is now at 1000 feet.
Speed set to 50
The blue Cessna 172 is flying through the air at 50 mph and at an altitude of 1000 feet.

=== ADDITIONAL FUNCTIONALITY DEMONSTRATIONS ===

Car-specific actions:
The Toyota Corolla is now parked.
Vehicle has been repainted to blue
Car now has 4 doors and a automatic transmission.

Boat-specific actions:
The Yamaha 242X has dropped its anchor.
Boat is a 24.2 foot speedboat.

Airplane-specific actions:
Changed altitude to 5000 feet.
Airplane has a wingspan of 36.1 feet and a max altitude of 14000 feet.
The Cessna 172 has landed safely.

Final states:
- 2022 Toyota Corolla (blue) - running
- 2023 Yamaha 242X (white) - running
- 2020 Cessna 172 (blue) - running
```

## Assignment Requirements Fulfilled

### Assignment 1: Design Your Own Class
- Created a Vehicle class with attributes and methods
- Used constructors to initialize each object with unique values
- Added multiple inheritance layers (Vehicle → Car/Boat/Airplane)
- Implemented encapsulation with private attributes and getter/setter methods

### Activity 2: Polymorphism Challenge
- Created a program with different vehicle classes that all implement a `move()` method
- Each vehicle class defines `move()` differently:
  - Car.move() shows driving on road
  - Boat.move() shows sailing on water
  - Airplane.move() shows flying through air

## Extensions

Possible extensions to this project:
- Add more vehicle types (motorcycle, helicopter, submarine)
- Implement fuel consumption and refueling
- Add passengers and cargo functionality
- Create a vehicle rental or management system
- Add graphical representation of vehicles
