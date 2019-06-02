class Solution:
    def threeSum(self, nums ):
        sorted_nums = sorted(nums)
        length = len(sorted_nums)
        #used = []
        res = []
        for index in range(0, length-2):

            #used.append(sorted_nums[index])
            start = index+1
            end = length-1
            while start < end:
                t_sum = sorted_nums[index] + sorted_nums[start] + sorted_nums[end]
                if t_sum ==0:
                    t_arr = [sorted_nums[index], sorted_nums[start], sorted_nums[end]]
                    if t_arr not in res:
                        res.append(t_arr)
                    start +=1
                    end -=1
                elif t_sum>0:
                    end -=1
                else:
                    start +=1
        return res


if __name__ == '__main__':
    print(Solution().threeSum([-1,0,1,2,-1,-4]))