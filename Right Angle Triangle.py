# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:20:22 2022

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
for i in range(0,5):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
