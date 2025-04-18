class Converter:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit.lower()  # Ensure the unit is in lowercase for consistency
        
        # Conversion factors relative to meters
        self.conversion_factors = {
            'inches': 0.0254,
            'feet': 0.3048,
            'yards': 0.9144,
            'miles': 1609.34,
            'kilometers': 1000,
            'meters': 1,
            'centimeters': 0.01,
            'millimeters': 0.001
        }
        
        # Check if the given unit is valid
        if self.unit not in self.conversion_factors:
            raise ValueError(f"Invalid unit '{unit}'. Valid units are: inches, feet, yards, miles, kilometers, meters, centimeters, millimeters.")

    def _convert_to_meters(self):
        # Convert the given length to meters based on the input unit
        return self.length * self.conversion_factors[self.unit]
    
    def convert(self, target_unit):
        target_unit = target_unit.lower()
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Invalid target unit '{target_unit}'. Valid units are: inches, feet, yards, miles, kilometers, meters, centimeters, millimeters.")
        
        # Convert the length to meters first
        length_in_meters = self._convert_to_meters()
        
        # Convert the length in meters to the target unit
        return length_in_meters / self.conversion_factors[target_unit]


# Input from user
def get_input():
    try:
        length = float(input("Enter the length: "))
        unit = input("Enter the unit (inches, feet, yards, miles, kilometers, meters, centimeters, millimeters): ").lower()
        if unit not in ['inches', 'feet', 'yards', 'miles', 'kilometers', 'meters', 'centimeters', 'millimeters']:
            print("Invalid unit. Please choose from inches, feet, yards, miles, kilometers, meters, centimeters, or millimeters.")
            return get_input()  # Recursively ask for input if invalid unit
        
        return length, unit
    except ValueError:
        print("Invalid input. Please enter a valid length.")
        return get_input()

# Example usage:
length, unit = get_input()  # Get length and unit from the user
c = Converter(length, unit)

# Take target unit from user to convert to
target_unit = input("Enter the target unit to convert to (inches, feet, yards, miles, kilometers, meters, centimeters, millimeters): ").lower()
result = c.convert(target_unit)
print(f"{length} {unit} is equal to {result} {target_unit}.")
