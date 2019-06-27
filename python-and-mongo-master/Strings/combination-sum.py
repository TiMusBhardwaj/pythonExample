class Solution:

    def __init__(self):
        self.res = []

    def combinationSum(self, candidates, target: int):
        self.res = []
        #candidates.sort()
        self.combinationSum_helper(candidates, target, [])
        return self.res


# In this Method no repeation is allowed in result.
    def combinationSum2(self, candidates, target: int):
        self.res = []
        candidates.sort()
        self.combinationSum_helper2(candidates, target, [])
        return self.res

    def combinationSum_helper2(self, candidates, target: int, res_arr):
        if target == 0:
            self.res.append(res_arr)
            return
        elif target <0 :
            return
        for index, can in enumerate(candidates):
            if index ==0 or candidates[index] != candidates[index-1] :
                res_arr_temp = res_arr[:]
                res_arr_temp.append(can)
                self.combinationSum_helper2(candidates[index+1:], target - can, res_arr_temp)



    def combinationSum_helper(self, candidates, target: int, res_arr):
        if target == 0:
            self.res.append(res_arr)
            return
        elif target <0 :
            return
        for index, can in enumerate(candidates):
            res_arr_temp = res_arr[:]
            res_arr_temp.append(can)
            self.combinationSum_helper(candidates[index:], target - can, res_arr_temp)

# https://leetcode.com/problems/combination-sum-iii/
    def combinationSum3(self, k: int, n: int):
        candidates = [1,2,3,4,5,6,7,8,9]
        self.res = []
        #n.sort()
        self.combinationSum_helper3(candidates, k, n, [])
        return self.res

    def combinationSum_helper3(self, candidates, k, target: int, res_arr):
        if target == 0 and k==0:
            self.res.append(res_arr)
            return
        elif target < 0 or k<0:
            return
        for index, can in enumerate(candidates):
            if index == 0 or candidates[index] != candidates[index - 1]:
                res_arr_temp = res_arr[:]
                res_arr_temp.append(can)
                self.combinationSum_helper3(candidates[index + 1:], k-1, target - can, res_arr_temp)


if __name__ == '__main__':
    print(Solution().combinationSum3(3,9))


