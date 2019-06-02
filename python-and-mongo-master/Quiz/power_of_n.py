class Solution:
    def myPow(self, x: float, n: int):
        if n == 0: return 1
        if n == -1: return 1/x
        if n == 1 : return x
        temp = self.myPow(x, int(n/2))
        if n%2==0:
            return temp * temp
        else:
            if n>0:
                return x*temp*temp
            else:
                return (1/x)*temp*temp



if __name__ == '__main__':
    print(Solution().myPow(2, -3))

    #x, y = 2, -4
    #print('%.6f' % (power(x, y)))