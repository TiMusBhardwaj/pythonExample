class Solution:

    def __init__(self):
        self.map = {}


    def isMatch(self, s: str, p: str) -> bool:

        if self.map.get(s + "_" + p):
            return self.map.get(s + "_" + p)

        if len(s) == 0 and len(p) == 0:
            return True
        if len(p) == 0 and len(s) > 0:
            return False

        if p[0] == '*':
            if p[len(p)-1] is not "*":
                return self.isMatch(s[::-1], p[::-1])
            count = 0
            while count + 1 < len(p) and p[count + 1] == '*':
                count += 1
            p = p[count:]
            ans = (len (p) >0 and self.isMatch(s, p[1:])) or ( len(s) > 0 and self.isMatch(s[1:], p))
            self.map[s+"_"+p] = ans
            return ans
        elif len(s)>0 and  (p[0] == '?' or p[0] == s[0]):
            ans = self.isMatch(s[1:], p[1:])
            self.map[s + "_" + p] = ans
            return ans
        else:
            self.map[s + "_" + p] = False
            return False




if __name__ == '__main__':
    ans = Solution().isMatch("bbaaaabaaaaabbabbabbabbababaabababaabbabaaabbaababababbabaabbabbbbbbaaaaaabaabbbbbabbbbabbabababaaaaa",
"******aa*bbb*aa*a*bb*ab***bbba*a*babaab*b*aa*a****")
    print(ans)