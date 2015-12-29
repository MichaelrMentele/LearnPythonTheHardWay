# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 21:18:54 2015

@author: mike
"""

#!/bin/python

import sys
import math
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

t = int(raw_input().strip())

for a0 in xrange(t):
    r = raw_input().split()
    
    count = 0
    r = map(int, r)
    for num in range(r[0],r[1] + 1):
        if math.sqrt(num) % 1 == 0:
            count += 1
    print count