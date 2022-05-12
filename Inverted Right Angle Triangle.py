# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 18:30:22 2022

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