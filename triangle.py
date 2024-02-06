"""Module for creating Triangle objects"""

class RightTriangle:
	"""Class that defines a right triangle"""

	_num_sides =3;

	def __init__(self, height, width):
		"""Constructor for the RightTriangle class

		Inputs: nonNegative floats height and width describing the height and width of the right triangle respectively
		Output: None
		"""
		if (height < 0):
			raise ValueError ("Height must not be negative");
		elif (width<0):
			raise ValueError ("Width must not be negative");
		else:
			self._h = height;
			self._w = width
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
	def __str__ (self):
		"""Stringifies the object. *Overload funtion: doesnt need to be called*

		Input: None
		Output: a String describing the object"""
		return "Width: "+ str(self._w)+ "., Height: "+str(self._h);


#c1 = RightTriangle(2,3);
#print(c1);