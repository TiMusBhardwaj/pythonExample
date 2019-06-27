class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = filter( lambda x : x != '' and x!='.',path.split('/'))
        stack = []
        for x in arr:
            if x == '..':
                if len(stack):
                    stack.pop()
                continue
            if x == '.' or x == '':
                continue
            else:
                stack.append(x)
        return '/'+'/'.join(stack)
if __name__ == '__main__':
    Solution().simplifyPath("/a/../../b/../c//.//")
