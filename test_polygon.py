import pytest
from polygon import Polygon

def test_polygon_initialization(): 
    polygon = Polygon("Triangle", [3, 3, 3])
    assert polygon.get_name() == "Triangle"
    assert polygon.get_sides() == [3, 3, 3]

def test_get_name():
    polygon = Polygon("Triangle", [3, 3, 3])
    assert polygon.get_name() == "Triangle"

def test_set_name():
    polygon = Polygon("Triangle", [3, 3, 3])
    polygon.set_name("Triangle")
    assert polygon.get_name() == "Triangle"

def test_get_sides():
    polygon = Polygon("Triangle", [3, 3, 3])
    assert polygon.get_sides() == [3, 3, 3]

def test_set_sides():
    polygon = Polygon("Triangle", [3, 3, 3])
    polygon.set_sides([3, 3, 3])
    assert polygon.get_sides() == [3, 3, 3]

def test_equality():
    polygon_1 = Polygon("Square", [3, 3, 3, 3])
    polygon_2 = Polygon("Square", [3, 3, 3, 3])
    assert polygon_1 == polygon_2

def test_inequality():
    polygon_1 = Polygon("Square", [3, 3, 3, 3])
    polygon_2 = Polygon("Triangle", [3, 3, 3, 3])
    assert polygon_1 != polygon_2 

def test_polygon_str():
    polygon = Polygon("Triangle", [3, 3, 3])
    polygon.set_name("Triangle")
    polygon.set_sides([3, 3, 3])
    assert str(polygon) == "Triangle with sides: [3, 3, 3]"

def test_calculate_circumference_triangle():
    triangle = Polygon("Triangle", [3, 3, 3])
    assert triangle.calculate_circumference() == pytest.approx(9)

def test_calculate_circumference_square():
    square = Polygon("Square", [4.0, 4.0, 4.0, 4.0])
    assert square.calculate_circumference() == pytest.approx(16.0)