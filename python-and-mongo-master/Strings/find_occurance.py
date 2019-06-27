from typing import  List
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        arr = text.split()
        #print(arr)
        res = []
        index = 0
        first_o = False
        second_o = False
        if first != second_o:
            while index < len(arr):
                if first_o and second_o:
                    first_o= False
                    second_o = False
                    res.append(arr[index])
                    #index +=1
                    continue
                if arr[index] == first:
                    first_o = True
                    second_o = False
                    index +=1
                    continue
                if first_o and arr[index] == second:
                    second_o = True
                    index +=1
                    continue
                first_o = False
                second_o = False
                index+=1

        else :
            count =0
            while index < len(arr):
                if count >2:
                    res.append(arr[index])
                    count =0
                    #index += 1
                    continue
                if arr[index] == first:
                    count+=1
                    index += 1
                    continue
                index +=1

        return res
if __name__ == '__main__':
    res = Solution().findOcurrences("we will we will rock you", first = "we", second = "will")
    print(res)
    #print("we will we will rock you".split("we will"))