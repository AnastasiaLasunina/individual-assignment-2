#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 18:02:43 2018

@author: Anastasia
"""
#%%
input_list = [3,2,3,4,67,8,90,5]

def bubble(lst):
    
    y = 0
    while y < len(lst):
        x = 0
        while x< len(lst) - 1:
            if lst[x] > lst[x+1]:
                temp = lst[x]
                lst[x] = lst[x+1]
                lst[x+1]= temp
            x= x + 1
        y = y + 1 
#%%