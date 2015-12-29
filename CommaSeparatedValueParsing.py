# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 19:48:57 2015

@author: mike

Problem 6: @ https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
"""

#Refactored
import math

C = 50
H = 30
Q = []

#Get csv list, strip it and create an array where each element follows a comma
D = [x for x in raw_input('Enter a CSV list :').rstrip().split(',')]

for item in D:
    Q.append(str(int(math.sqrt(((2*C*int(item))/H)))))

print ','.join(Q)


###Original
'''
import math

C = 50
H = 30
Q = []

D = raw_input('Enter a CSV list :')
D = D.rstrip().split(',')

for idx, num in enumerate(D):
    Q.append(str(int(math.sqrt(((2*C*int(D[idx]))/H)))))

print ','.join(Q)
'''