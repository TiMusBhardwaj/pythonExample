
#

def starsAndBars(strToEvaluate, startIndex, endIndex):
    res =0
    for start, end in zip(startIndex,endIndex):
        res +=starsAndBars_helper(strToEvaluate, start, end)
    return res

def starsAndBars_helper(strToEvaluate, startIndex, endIndex):
    res = 0
    temp = 0
    start = False
    if startIndex >= endIndex:
        return 0
    endIndex = endIndex if len(strToEvaluate) >=endIndex else len(strToEvaluate)
    for char, index in enumerate(strToEvaluate[startIndex-1: endIndex]):
        if char == '|':
            if start:
                res +=temp
                temp =0
            else:
                start = True
            continue
        elif start:
            temp +=1
    return res

if __name__ == '__main__':
    starsAndBars('*|*|', [1] ,[3])