import math
import os
import random
import re
import sys



def countingValleys(steps, path):
    sea_level=0
    valley_count=0
   
    for index in path:
        if sea_level==0 and index=="U":
            sea_level=sea_level+1
            continue
        if sea_level < 0 and index=="U":
            sea_level=sea_level+1
            print("what actually the sea level when it is less than 0 and input is U",sea_level)
            if sea_level==0:
                valley_count=valley_count+1
                
            else:
                sea_level=sea_level
        if sea_level >0 and index =="U":
            sea_level=sea_level+1
            continue

        if sea_level==0 and index=="D":
            sea_level=sea_level-1
            continue
        if sea_level < 0 and index=="D":
            sea_level=sea_level-1
            continue
                
        else:
            sea_level=sea_level
                
        if sea_level >0 and index =="D":
            sea_level=sea_level-1
            continue
    print("valey count is ",valley_count)



    
    

if __name__ == '__main__':


    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

   
