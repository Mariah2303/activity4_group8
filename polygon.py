
def calculate_circumference(self):
    sum = 0
    for side in self.sides:
        sum += side
    return sum
    
def main():
    """
    This function is the main function that 
    demonstrates the use of the class and takes no parameters
    """

    #objects
    triangle = Polygon("Triangle", [3, 3, 4])
    square = Polygon("Square", [2, 2, 2, 2])
    hexagon = Polygon("Hexagon", [2, 2, 2, 2, 2, 2])
    
    print(triangle)
    print(f"The circumference is {triangle.calculate_circumference()}")

    print(square)
    print(f"The circumference is {square.calculate_circumference()}")

    print(hexagon)
    print(f"The circumference is {hexagon.calculate_circumference()}")
    
if __name__ == "__main__":
    main()