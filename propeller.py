import convert as c;
import fluids as f;
import phys as p;
import numpy as np;
from math import pi;

class Propeller:

	a=0; #velocity increment coeficient at propeller (V[1+a], p'+delta p)
	b= 0; #velocity increment coeficient at (V[1+b],p)
	r=0;

	def __init__ ():
		""" initializer """


	def setA(self,a):
		""" sets the values of a and b

		input: self, a (velocity increment coeficient at propeller (V[1+a], p'+delta p))
		output: none"""
		self.a=a
		self.b=2*b
		return

	def setB(self,b):
		""" sets the values of a and b

		input: self, (b velocity increment coeficient at (V[1+b],p))
		output: none"""
		self.b=b
		self.a=b/2
		return

	def ADisk(self):
		""" returns the area of the propeller as a disk

		input: self
		output: area or disk"""
		return pi*self.r**2

	def efficiencyIdeal(self):
		""" returns the efficiency of the propeller

		input: self
		output: ideal efficiency of the propeller"""
		return 1/(1+self.a)

	def thrustIdeal(self,v,z):
		""" computes the energy produced by the thrust of the propeller

		input: self, v (velocity of fluid m/s), z (altitude of propeller m)
		output: thrust (mass flow rate*velocity added to fluid)"""
		return .5*f.mdotIdeal(v,z,self.ADisk())*(self.b*v)**2