#https://www.hackerrank.com/challenges/between-two-sets/problem
import os
import sys
import math


def gcd(a, b):
    if (a == b):
        return a
    elif not a:
        return b
    elif not b:
        return a
    # base case if a and b are equal

    # if a is greater
    elif (a > b):
        return gcd(a - b, b)

    return gcd(a, b - a)


def gcd_array(arr):
    if arr.__len__() < 2:
        return arr.__getitem__(0);
    gcd_var = int(math.gcd(arr[0], arr[1]))
    for e in range(2, arr.__len__()):
        gcd_var = math.gcd(gcd_var, arr.__getitem__(e))
    return gcd_var


# Function to return LCM of two numbers
def lcm(a, b):
    gcd = math.gcd(int(a), b)
    return (a * b) / gcd


def lcm_array(arr):
    if arr.__len__() < 2:
        return arr.__getitem__(0);

    lcm_var = int(lcm(arr[0], arr[1]))
    for i in range(2, arr.__len__()):
        lcm_var = lcm(lcm_var, arr.__getitem__(i))

    return lcm_var


#
# Complete the getTotalX function below.
#
def getTotalX(a, b):
    lcm = lcm_array(a)
    gcd = gcd_array(b)

    if gcd % lcm != 0:
        return 0
    res = 0
    counter = 1
    while (lcm * counter) <= gcd:
        if gcd % (lcm * counter) == 0:
            res += 1
        counter += 1
    return res

if __name__ == '__main__':


    total = getTotalX([100 ,99 ,98 ,97 ,96 ,95 ,94 ,93 ,92 ,91], [1, 2, 3, 4 ,5 ,6 ,7 ,8, 9 ,10])
    print(int(total))


