
#TODO This still has some issue

def minSubArrayLen( s : int, nums):

    start_in = 0
    temp_sum =0
    res = 0
    first = True
    for index in range (0,len(nums)):
        temp_sum += nums[index]
        if temp_sum >= s:
            if first:
                res = index - start_in +1
                first = not first
            else :
                res = min(res, index - start_in + 1)

            while start_in < len(nums)-1  and temp_sum - nums[start_in] >= s:
                start_in += 1
                res = min(res, index - start_in + 1)
                temp_sum -= nums[start_in]


    return res


if __name__ == '__main__':
    print(minSubArrayLen(7, [2,3,1,2,4,3]))