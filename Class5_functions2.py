# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:39:26 2019

@author: jooho
"""

def sum(start, end):
    total = 0
    for i in range(start, end+1):
        total += i
    return total
    
def sum_even(start, end):
    total=0
    for i in range(start, end+1):
        if i % 2 ==0: total += i
    return total
    