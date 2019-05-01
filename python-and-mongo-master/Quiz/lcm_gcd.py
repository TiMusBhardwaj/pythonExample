import numpy

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
    res = None
    for e in arr:
        res = gcd(res, e)
    return res


# Function to return LCM of two numbers
def lcm(a, b):
    return (a * b) / gcd(a, b)


def lcm_array(arr):
    if arr.__len__() < 2:
        return arr.__getitem__(0);

    lcm_var = lcm(arr[0], arr[1])
    for i in range(2, arr.__len__()):
        lcm_var = lcm(lcm_var, arr.__getitem__(i))

    return lcm_var


# Driver program to test above function
a = 15
b = 20

print (lcm_array([2,6]))
print (gcd_array([24,36]))
print('LCM of', a, 'and', b, 'is', lcm(a, b))