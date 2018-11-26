# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 20:22:56 2018

@author: arnob
"""

def Med(listA, listB):
    
    #for listA
    list_1= sorted(listA)
    list_2= sorted(listB)
    
    if len(list_1) == 0:
       print('No values in the 1st list')
    
    elif len(list_1) % 2 == 1:
        #median is the middle element
        medianA = list_1[len(list_1) // 2]
        print ('Median of the 1st list is = ', medianA )
    else :
        medianA = (list_1[len(list_1) // 2] + list_1[len(list_1) // 2 -1]) / 2 
        print('Median of the 1st list is = ', medianA )
   
     #for listB
     
     
    if len(list_2) == 0:
       print('No values in the 2nd list')
    
    elif len(list_2) % 2 == 1:
        #median is the middle element
        medianB = list_2[len(list_2) // 2]
        print ('Median of the 2nd list is = ', medianB )
    else :
        medianB = (list_2[len(list_2) // 2] + list_2[len(list_2) // 2 -1]) / 2 
        print('Median of the 2nd list is = ', medianB )
        
        
    