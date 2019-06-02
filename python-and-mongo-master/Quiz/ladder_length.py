class Solution:
    def ladderLength(self, begin_word: str, end_word: str, wordList):
        arr =[]
        arr.append((begin_word, 1))

        while arr.__len__() >0:
            word, length = arr.pop(0)
            for dict_word in wordList[:]:
                if is_adjacent(word, dict_word):
                    wordList.remove(dict_word)
                    arr.append((dict_word, length+1))
                    if dict_word == end_word:
                        return length+1
        return 0


def is_adjacent(word, dict_word):
    mismatch = 0
    for char_1, char2 in zip (word, dict_word):
        if char_1 is not char2:
            mismatch +=1
        if mismatch>1:
            return False

    return True if mismatch ==1 else False

if __name__ == '__main__':
    print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))