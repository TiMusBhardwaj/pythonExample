class Solution:
    def splitIntoFibonacci(self, input_str: str) :

        length = len(input_str)

        for i in range(0, int(length / 2)):
            if i > 0 and input_str[0] == '0':
                return []
            num1 = int(input_str[0:i + 1])
            j = 1
            while max(i + 1, j) <= length - i - j - 1:

                if j > 1 and input_str[i + 1] == '0':
                    break
                num2 = int(input_str[i + 1:i + j + 1])
                res = is_additive_rec(num1, num2, i + j + 1, input_str)
                if len(res) > 0:
                    res.insert(0, num1)
                    return res
                j += 1
        return []


def is_additive_rec(num1, num2, start, input_str):
    if start == len(input_str):
        return [num2]

    sum = num1 + num2
    sum_str = str(sum)
    if not input_str.startswith(sum_str, start):
        return []
    prev = is_additive_rec(num2, sum, start + len(sum_str), input_str)
    if len(prev) > 0:
        prev.insert(0, num2)

    return prev



