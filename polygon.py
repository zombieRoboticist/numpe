"""A module for the geometry of polygons"""

from math import sqrt

class Polygon(object):
    """An abstract base class for plane figures with at least 3 sides"""
    _num_sides = 0

    def __init__(self, height, width):
        """initialize a polygon of `height` and `width` dimensions"""
        if height < 0.0 or width < 0.0:
            raise ValueError("height and width must be positive.")
        self._h = height
        self._w = width

    def get_num_sides(self):
        """returns the number of sides the polygon has"""
        return self._num_sides

    def calc_area_perimeter_ratio(self):
        """returns the ratio of the polygon's area to its perimeter"""
        return self.calc_area()/self.calc_perimeter()

class RightTriangle(Polygon):
    """Class that defines a right triangle"""

    def __init__(self, height, width):
        """initialize a polygon of `height` and `width` dimensions

        Inputs: floats describing the width and height of the triangle
        Output: None"""
        Polygon.__init__(self, height, width);
        self._num_sides=3;
        return None;

    def calc_area(self):
        """Calculates the area of the triangle

        Inputs: None
        Output: The area of the triangle as a float"""
        return (0.5*self._h*self._w);

    def calc_perimeter(self):
        """Calculates the perimiter of the triangle

        Inputs: None
        Output: a float that describes the perimeter of the object"""
        return (self._h+self._w+ ((self._h**2)+(self._w**2))**0.5);


class Rectangle(Polygon):
    """Class for creating a rectange"""

    def __init__(self, height, width):
        """initialize a polygon of `height` and `width` dimensions

        Inputs: floats describing the width and height of the rectangle
        Output: None"""
        Polygon.__init__(self, height, width);
        self._num_sides=4;
        return None;

    def calc_area(self):
        """Calculates the area of the Rectangle

        Inputs: None
        Output: The area of the Rectangle as a float"""
        return (self._h*self._w);

    def calc_perimeter(self):
        """Calculates the perimiter of the Rectangle

        Inputs: None
        Output: a float that describes the perimeter of the object"""
        return 2*(self._h+self._w);
            