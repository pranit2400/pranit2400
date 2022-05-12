# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 13:30:15 2022

@author: Pranit Dongare
"""

"""
output:-

* * * * * 
  * * * * 
    * * * 
      * * 
        * 
"""
for i in range(0,5):
    for j in range(i-1,4):
        print("*",end=" ")
    print()
    for k in range(0,i+1):
        print(" ",end=" ")
print()