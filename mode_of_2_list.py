# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 21:59:15 2018

@author: arnob
"""

def Mod(listA,listB):
    
    k= sorted(listA)
    l= sorted(listB)
    M=[]
    N=[]
    maximumA=0
    maximumB=0
    
    for i in range(len(k)):
        count=0
        for j in range(i,len(k)):
           if k[i]==k[j]:  
              count=count+1
        if  count>1:
            if count>maximumA:
                 M.append(k[i])
                 maximumA=count
            if M[0]!='':
                M.pop(0)
                M.insert(0,k[i])
            elif count==maximumA:
                M.append(k[i])
        if i==len(k)-1:
            print('The mode of listA is = ', M)
    if maximumA==0:
        print('there is no mode in listA')
     
    
    
    for m in range(len(l)):
        count=0
        for n in range(len(l)):
           if l[m]==l[n]:  
              count=count+1
        if  count>1:
            if count>maximumB:
                 N.append(l[m])
                 maximumB=count
            if N[0]!='':
                N.pop(0)
                N.insert(0,l[m])
            elif count==maximumB:
                N.append(l[m])
        if m==len(l)-1:
            print('The mode of listB is = ', N)
    if maximumB==0:
        print('there is no mode in listB')
     
        
               