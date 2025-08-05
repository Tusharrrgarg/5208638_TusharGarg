
import math
import os
import random
import re
import sys


def plusMinus(arr):

    pcount=0
    ncount=0
    zcount=0
    for i in arr:
        if (i>0):
            pcount+=1
        elif (i<0):
            ncount+=1
        elif (i==0):
            zcount+=1
    total=len(arr)
    print(pcount/total)
    print(ncount/total)
    print(zcount/total) 
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
