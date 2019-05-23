
def shortestSubarray( A, K) :

    start =-1
    res = -1
    first = True
    temp_sum = 0
    dip = 0
    for index in range(0, len(A)):
        if A[index] < 0:
            dip = dip + A[index]
        temp_sum += A[index]
        if temp_sum < 0:
            temp_sum =0
            start =index
            dip =0

        if temp_sum >= K :
            while True:
                if temp_sum - A[start+1] >= K +dip:
                    if A[start+1] < 0:
                        dip = dip - A[start+1]
                    start +=1
                    temp_sum -= A[start]
                elif dip !=0:
                    while temp_sum < K:
                        temp_sum += A[start]
                        if A[start] < 0:
                            dip = dip + A[start]
                        start = start-1
                    break
                else:

                    break
            if first:
                res = index - start
                first = not first
            else:
                res = min(res, index - start)

    return res




def shortestSubarray_timeConsuming( A, K) :

    start = 0
    res = -1
    first = True

    for index in range(0, len(A)):
        temp_sum = 0
        temp_sum = A[index]
        temp_index = index
        while temp_index != start:
            if temp_sum >= K:
                break
            else :
                temp_index -=1
                temp_sum +=A[temp_index]
        if temp_sum >= K:
            if first:
                res = index - temp_index +1
                first = not first
            else:
                res = min(res, index - temp_index +1)
            start = temp_index +1
    return res


if __name__ == '__main__':
    print(shortestSubarray(A = [12,17,26,72,93,95,-46,66,-38,-18,83,95,75,8,93,7,25,16,67,-19], K = 413))

def shortestSubarray_onlyPositives( A, K) :

    start =-1
    res = -1
    first = True
    temp_sum = 0
    for index in range(0, len(A)):
        temp_sum += A[index]
        if temp_sum < 0:
            temp_sum =0
            start =index

        if temp_sum >= K :
            while True:
                if temp_sum - A[start+1] >= K:
                    start +=1
                    temp_sum -= A[start]
                else:
                    #res = min(res , handleNegatives)
                    break
            if first:
                res = index - start
                first = not first
            else:
                res = min(res, index - start)

    return res