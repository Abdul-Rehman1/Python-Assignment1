# -*- coding: utf-8 -*-
"""
Created on Sun May 19 21:34:10 2019

@author: Abdul Rehman
"""

# Largest element in list

class Numberss:
    def max_number(self,number):
        max=0
        for item in number : 
            if item>max :
                max=item
        return(max)