# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:42:32 2022

@author: Niko
"""
a= [2,3];
b=1000000;
for i in range (5,b,2):
    temp = True;
    for j in range(0,len(a)):
        if i%a[j]==0:
            temp = False;
            break;
    if temp:
        a.append(i);
print(a);