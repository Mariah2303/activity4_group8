class Polygon:
    def __init__(self, name: str, sides: list[float]):

        self.name = name
        self.sides = sides

    def get_name(self):
        return self.name

    def get_sides(self):
        return self.sides
    









def main():
    """
    Creates and demonstrates Polygon objects.
    """

    # Create polygon objects
    triangle = Polygon("Triangle", [3, 4, 5])
    square = Polygon("Square", [4, 4, 4, 4])
    hexagon = Polygon("Hexagon", [6, 6, 6, 6, 6, 6])

    # Print object information and circumference
    for polygon in [triangle, square, hexagon]:
        print(f"{polygon}")
        circumference = polygon.calculate_circumference()
        print(f"  Circumference: {circumference:.2f}")


if __name__ == "__main__":
  main()