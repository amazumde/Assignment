# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:38:55 2018

@author: arnob
"""

def Avg(listA, listB):
    sumA=0
    sumB=0
    
    P= len(listA)
    Q= len(listB)
    print ('P=',P)
    for i in range(P):
        sumA = sumA+listA[i]
    
    print ('sumA=',sumA)  
    
    print ('Q=', Q)
    for j in range(Q):
        sumB = sumB + listB[j]
    
    print ('sumB=',sumB)
    
    Average =(sumA+sumB)/( P+Q )
    
    print ("The mean of the two list is", Average)