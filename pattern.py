# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 13:19:18 2019

@author: Abdul Rehman
"""
'''
for i in range(0,20):
    print(" "*(20-i),end="")
    print("* "*i,end="")
    print()
   # print(" *"*i)
for i in range(20,-1,-1):
    print(" "*(20-i),end="")
    print("* "*i,end="")
   # print(" *"*i)   
print("Done")
'''

for i in range(0,5):
    print("*"*(5-i),end="")
    print("  "*i,end="")
    print("*"*(5-i))
for i in range(5,-1,-1):
    print("*"*(5-i),end="")
    print("  "*i,end="")
    print("*"*(5-i)) 
print("Done")