

def findSubstring(s, words):

    words_dict = {}
    for word in words:
        words_dict[word] = 1 if words_dict.get(word) is None else words_dict[word]+1



    res =[]
    length = len(words[0])
    for i in  range(0, length):
        count = 0
        start_res = i
        res_dict = {}
        x=i
        while x<=len(s)-length:
            word_x = s[x: x + length]
            if words_dict.get(word_x) is None:
                count = 0
                start_res = x+length
                res_dict = {}
                x += length
                continue

            res_dict[word_x] = 1 if res_dict.get(word_x) is None else res_dict[word_x] + 1
            count += 1

            if res_dict.get(word_x) > words_dict.get(word_x):
                while (res_dict.get(word_x) > words_dict.get(word_x)):
                    word_st = s[start_res: start_res + length]
                    res_dict[word_st] = res_dict.get(word_st)-1
                    count -=1
                    start_res = start_res + length

            if count == len(words):
                res.append(start_res)
                #res_dict ={}
                word_st = s[start_res: start_res + length]
                res_dict[word_st] = res_dict.get(word_st) - 1
                start_res += length
                count -=1
            x+=length
    return res

if __name__ == '__main__':
    s ="abababab"
    words=["ab","ba"]
    print(findSubstring(s, words))




