class Solution:
    def reverse_words(self, s: str):
        #word = False
        word =''
        res = ''
        res = ''
        for index, char in enumerate((s)):
            if char == ' ':
                if word =='':
                    continue
                else :
                    res = word if res == '' else word + ' ' + res
                    word = ''
            else :
                word = word+char
        if word is not '':
            res = word if res == '' else word + ' ' + res
        return res

if __name__ == '__main__':
    print(Solution().reverse_words("  I am    sucker  d  "))