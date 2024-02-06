# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:05:22 2022

@author: Niko
"""

from angles import theta;
from math import sin, cos, pi;



ang = theta*pi/180;
F = 550;
Lac =.6;
Lbc = Lac/(((sin((45*pi/180))*cos((30*pi/180)))/sin(30*pi/180))+cos(45*pi/180));
Lab = Lbc*sin((45*pi/180))/sin((30*pi/180));
#print(Lab)
Ax=(-1)*F*cos(ang);
Cy=F*((-1)*sin(ang)*Lab*cos((30*pi/180))+cos(ang)*Lab*sin((30*pi/180)))/Lac;
Ay=(-1)*Cy-F*sin(ang);
T_BC=(-1)*Cy/sin((45*pi/180));
T_AB =(-1)*Ay/sin((30*pi/180));
T_AC=(-1)*T_BC*cos((45*pi/180));
#print(T_AB)
#print(Ax)