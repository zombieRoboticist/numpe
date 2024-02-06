# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 14:47:13 2022

@author: Niko
"""
from math import pi;
diameter = 2.0;
radius = diameter/2;
height = .75;
tWidth = .75;
triangleArea= height*tWidth/2;
circleArea= (radius**2)*pi/2;
rectangleArea=height*diameter;
area= triangleArea+circleArea+rectangleArea;
print(area);