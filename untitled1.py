# -*- coding: utf-8 -*-
"""
Created on Sun May  8 00:34:07 2022

@author: sarper
"""

def rev(x):
    x.reverse()
     
    for i in x:
        if type(i)==list:
            rev(i)
    return x

l = [[1, 2], [3, 4], [5, 6, 7]]

print(rev(l))