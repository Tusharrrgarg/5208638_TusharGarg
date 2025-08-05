
import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    # Write your code here
    tsum= sum(arr)
    min_sum=tsum-max(arr)
    max_sum=tsum-min(arr)
    print(min_sum,max_sum)
    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
