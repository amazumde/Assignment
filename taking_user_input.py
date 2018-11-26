# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:27:43 2018

@author: arnob
"""

listA=[]

listB=[]

number = int(input("Enter the lenth of both list value must be GREATER than 0 = "))

if number > 0 :

  print ("Enter listA values ")

  for i in range(number) :
      try:
          dataA = float(input())
          listA.append(dataA)
      except:
          continue

  print ("Enter listB values ")

  for k in range(number) :
      try:
          dataB = float(input())
          listB.append(dataB)
      except:
          continue
    
  print('listA=',listA)
  print('listB=',listB)
    
  from mean_of_2_list import Avg

  I = Avg(listA, listB)
  print (I)
  


  from median_of_2_list import Med

  J = Med(listA, listB)
  print (J)
  
  from mode_of_2_list import Mod
  
  K= Mod(listA, listB)
  print(K)
    
  from manhattan_distance_of_2_list import man
  L= man(listA, listB)
  print (L)
else :
   print('please enter a valid number. Must be Greater than 0')