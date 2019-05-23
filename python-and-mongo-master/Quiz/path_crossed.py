#https://leetcode.com/problems/self-crossing/


def isSelfCrossing( x):

    if x.__len__() < 4:
        return False
    i=0

    if x[i] >= x[i+2] or x[3] < x[1]:
        return inner_loop(i,x)
    elif x [i+1] == x[i+3] and x[0] +x[4] >= x[2]:
        return True
    elif x [i+1] == x[i+3] and x[0] +x[4] < x[2]:
        return inner_loop(i+2,x)
    else:
        return outer(i,x)
    return False

def outer(i,x):
    while i+4 < x.__len__():
        if x[i+2] < x[i+4]:
            i+=1
            continue
        elif x[i+2] >x[i+4] and x[i+4] +x[i+0] >=x[i+2]:
            return inner_or_connect(i,x)
        elif x[i+2] >x[i+4] and x[i+4] +x[i+0] <x[i+2]:
            return inner_loop(i+2, x)
    return False

def inner_or_connect(i,x):
    if i+ 5 < x.__len__() and x[5] + x[1] >= x[2]:
        return True
    else:
        return inner_loop(i+2, x)


def inner_loop(i, x):
    while i + 3 < x.__len__():
        if x[i + 3] >= x[i + 1] and x[i + 2] <= x[i]:
            return True
        i += 1
    return False

if __name__ == '__main__':
     print(isSelfCrossing([1,1,2,2,1,1]))