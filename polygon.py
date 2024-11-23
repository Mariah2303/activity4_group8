class Polygon:
    """
    A class for polygons with attributes for a name, sides, and methods for
    calculations and comparisons.
    """
    def __init__ (self, name, sides):
        self.name = name
        self.sides = sides

# Getter and setter for name
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    
#Getter and setter for sides
    def get_sides(self):
        return self.sides
    def set_sides(self, sides):
        self.sides = sides

# Implements Equality and Inequality Methods
    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.name == other.name and self.sides == other.sides
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
# string representation for the class
    def __str__(self):
        return f"{self.name} with sides: {self.sides}"
    
# calculates the circumference for the polygon
    def calculate_circumference(self):
        sum = 0
        for side in self.sides:
            sum += side
        return sum 
    