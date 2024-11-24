import pytest
from polygon import Polygon

# Tests if object is correctly initialized with values for name and sides.
def test_polygon_initialization(): 
    polygon = Polygon("Triangle", [3, 3, 3])
    assert polygon.get_name() == "Triangle"
    assert polygon.get_sides() == [3, 3, 3]

# Tests the getter for the name
def test_get_name():
    polygon = Polygon("Triangle", [3, 3, 3])
    assert polygon.get_name() == "Triangle"

# Tests the setter for the name
def test_set_name():
    polygon = Polygon("Triangle", [3, 3, 3])
    polygon.set_name("Triangle")
    assert polygon.get_name() == "Triangle"

# Tests the getter for the sides
def test_get_sides():
    polygon = Polygon("Triangle", [3, 3, 3])
    assert polygon.get_sides() == [3, 3, 3]

# Tests the setter for the sides
def test_set_sides():
    polygon = Polygon("Triangle", [3, 3, 3])
    polygon.set_sides([3, 3, 3])
    assert polygon.get_sides() == [3, 3, 3]

# Tests if two polygons with identical attributes are equal.
def test_equality():
    polygon_1 = Polygon("Square", [3, 3, 3, 3])
    polygon_2 = Polygon("Square", [3, 3, 3, 3])
    assert polygon_1 == polygon_2

# Tests if polygons with different attributes are not equal.
def test_inequality():
    polygon_1 = Polygon("Square", [3, 3, 3, 3])
    polygon_2 = Polygon("Triangle", [3, 3, 3, 3])
    assert polygon_1 != polygon_2 

# Tests the string representation of a polygon
def test_polygon_str():
    polygon = Polygon("Triangle", [3, 3, 3])
    polygon.set_name("Triangle")
    polygon.set_sides([3, 3, 3])
    assert str(polygon) == "Triangle with sides: [3, 3, 3]"

# Tests circumference calculation for a triangle
def test_calculate_circumference_triangle():
    triangle = Polygon("Triangle", [3, 3, 3])
    assert triangle.calculate_circumference() == pytest.approx(9)

# Test circumference calculation for a square with list of floats
def test_calculate_circumference_square():
    square = Polygon("Square", [4.0, 4.0, 4.0, 4.0])
    assert square.calculate_circumference() == pytest.approx(16.0)