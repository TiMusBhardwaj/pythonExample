class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:

        start = 0
        count = 0
        index = 0
        sec_count = 0
        frequency = ''
        for x in S:
            #frequency = ''
            if x.isdigit():
                frequency = x
            else:
                count+=1
                sec_count +=1
                if count == K:
                    return x

            if frequency is not None and frequency is not '':
                frequency_int = int(frequency) - 1
                if (count + sec_count) * frequency_int >= K:
                    rep_index = (K) % (sec_count+count)
                    if rep_index == 0:
                        return S[start + sec_count - 1]
                    else:
                        return S[start + rep_index - 1]
                else:

                    count = (count + sec_count) * frequency_int
                frequency = ''
                sec_count = 0
                start = index+1
            index +=1
        return ''




if __name__ == '__main__':
    print(Solution().decodeAtIndex("ha22",5))
