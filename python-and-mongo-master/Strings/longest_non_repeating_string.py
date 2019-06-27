class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0

        ans = 0
        set_alpha=set()
        for index in range(0, len(s)):
            curr_alpha = s[index]
            if curr_alpha in set_alpha:
                ans = max(ans, len(set_alpha))
                while True:
                    if not curr_alpha == s[start]:
                        print(set_alpha)
                        set_alpha.remove(s[start])
                        start+=1
                    else:
                        start +=1
                        break

            else:
                set_alpha.add(s[index])

        return max(ans, len(set_alpha))

    def lengthOfLongestSubstring2(self, str):
        alpha_dict = {}
        start = 0
        result = 0
        for index,char in enumerate(str):
            if alpha_dict.get(char) is not None:
                start = max(alpha_dict.get(char),start)
            alpha_dict[char] = index+1
            result = max(result, index - start+1)

        return result


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring2("abba"))
