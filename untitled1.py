# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:38:55 2018

@author: arnob
"""

def Avg(a, b, c, d):
    sumA=0
    sumB=0
    
    listA = {11,22,33,44,55,66,77,88}
    listB = {44,55,66,77,88,99,22,11}
    
    P = len(listA)
    Q = len(listB)
    
    for sumA in listA:
        sumA = sumA+listA
        
        
    for sumB in listB:
        sumB = sumB+listB
    
    Avg=(sumA+sumB)/( P + Q )
    
    print()