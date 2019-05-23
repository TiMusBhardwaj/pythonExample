def longestValidParentheses(s: str) -> int:
    stack = []
    res_stack = [0]
    for c in s:
        if c == ')' and stack.__len__() ==0:
            continue
        elif c == '(':
            stack.append(c)
        else:
            temp_count = 0
            match = False
            while stack.__len__() > 0:

                t = stack.pop().__str__()
                if t == ')':
                    stack.append(')')
                    stack.append(')')
                    break
                elif t == '+':
                    temp_count +=1
                elif t == '(':
                    match = True
                    break
            while temp_count > 0:
                temp_count -= 1
                stack.append('+')
            if match:
                stack.append('+')
            else :
                stack.append(')')

    curr_count = 0
    res = 0
    for s in stack:
        if s == '+':
            curr_count += 1
        else:
            res = max(res, curr_count)
            curr_count = 0


    return max(res, curr_count) * 2

print(longestValidParentheses(")()())()()("))
