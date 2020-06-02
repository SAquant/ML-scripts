# -*- coding: utf-8 -*-
"""
Created on Tue May 21 06:38:12 2019

@author: mbongiseni

The program serves as review of variables in python
"""

#videos
new_video = input("How many new videos would you like? :")
old_video = input("How many old videos would you like? :")
cost = int(new_video)*3 + int(old_video)*2
print('the total cost will be: $',cost, 'thank you!')

#for loop
multiple =5
print("the following are multiples of 5")

for count in range(1,7):
    r= multiple*count
    print(count, ":", r)
    