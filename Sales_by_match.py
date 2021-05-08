import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    dict_unique={}
    count=0
    for index in ar:
        dict_unique[index]=dict_unique.get(index,0)+1
 
    for key,value in dict_unique.items():
        count+=value//2
    return count
            

if __name__ == '__main__':
   

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

    