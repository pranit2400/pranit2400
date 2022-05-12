# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 13:07:15 2022

@author: Pranit Dongare
"""
"""
output:-

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""
for i in range(0,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
    for k in range(i,4):
        print(" ",end=" ")
print()