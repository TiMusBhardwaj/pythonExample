from functools import reduce

def minWindow( s: str, t: str):

    in_length = len(t)
    char_dict = {}
    for word in t:
        char_dict[word] = 1 if char_dict.get(word) is None else char_dict[word] + 1
    start_in = 0
    res_dict={}
    window = ""
    first = True
    count = 0
    for index in range(0, len(s)):
        ch = s[index]
        if char_dict.get(ch) is not None:
            res_dict[ch] = 1 if res_dict.get(ch) is None else res_dict[ch]+1
            if res_dict[ch] <= char_dict[ch]:
                count +=1

            if count == in_length:
                while True :
                    start_ch = s[start_in]
                    if res_dict.get(start_ch) is None :
                        start_in += 1
                    elif res_dict.get(start_ch) > char_dict[start_ch]:
                        start_in +=1
                        res_dict[start_ch] = res_dict[start_ch] - 1
                    else:
                        break
                if first:
                    window = s[start_in:index + 1]
                    first = not first
                else:
                    window = s[start_in:index + 1] if len(s[start_in:index + 1]) < len(window) else window

    return window

if __name__ == '__main__':
    print(minWindow("aab","aab"))


def minWindow(s: str, t: str):
    in_length = len(t)
    char_dict = {}
    for word in t:
        char_dict[word] = 1 if char_dict.get(word) is None else char_dict[word] + 1
    start_in = 0
    res_dict = {}
    window = ""
    first = True
    count = 0
    for index in range(0, len(s)):
        ch = s[index]
        if char_dict.get(ch) is not None:
            res_dict[ch] = 1 if res_dict.get(ch) is None else res_dict[ch] + 1
            # if res_dict[ch] <= char_dict[ch]:
            count += 1
            if res_dict[ch] > char_dict[ch]:
                # count -=1
                while (res_dict[ch] > char_dict[ch]):
                    char_st = s[start_in]
                    if res_dict.get(char_st) is not None and char_st != ch:
                        count -= 1
                        break
                    start_in += 1
                    if res_dict.get(char_st) is not None:
                        res_dict[char_st] = res_dict[char_st] - 1
                        count -= 1
                while (not t.__contains__(s[start_in])):
                    start_in += 1
            if count == in_length:
                while (not t.__contains__(s[start_in])):
                    start_in += 1
                if first:
                    window = s[start_in:index + 1]
                    first = not first
                else:
                    window = s[start_in:index + 1] if len(s[start_in:index + 1]) < len(window) else window
    return window
