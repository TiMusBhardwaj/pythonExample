
def is_additive(input_str: str):
    length = len(input_str)

    for i in range(0, int(length/2)):
        if i > 0 and input_str[0] == '0':
            return False
        num1 = int(input_str[0:i+1])
        j = 1
        while max(i+1,j) <= length - i-j-1:

            if j > 1 and input_str[i+1] =='0':
                break
            num2 = int(input_str[i+1:i+j+1])
            if is_additive_rec(num1, num2, i+j+1, input_str):
                return True
            j+=1
    return False

def is_additive_rec(num1, num2, start, input_str):
    if start == len(input_str):
        return True

    sum = num1 + num2
    sum_str= str(sum)
    return input_str.startswith(sum_str, start) and is_additive_rec(num2, sum, start+len(sum_str), input_str)

if __name__ == '__main__':
    print(is_additive("199001200"))

