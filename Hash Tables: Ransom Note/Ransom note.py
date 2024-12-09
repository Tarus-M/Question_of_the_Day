#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    mag_d = {}
    
    # give me one grand today night
    # {give: 0, me: 1, one: -1, grand: 0, today: 1, night: 1}
    for word in magazine:
        if word in mag_d:
            mag_d[word] +=1
        else:
            mag_d[word] = 1
    
    answer = "Yes"
    # give one grand one tomorrow
    
    for word in note:
        if word in mag_d:
            mag_d[word] -=1
            if mag_d[word] < 0:
                answer = "No"
                break
        else:
            answer = "No"
            break
    print(answer)

     

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
