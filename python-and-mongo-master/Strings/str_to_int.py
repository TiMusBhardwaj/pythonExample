class Solution:
    def myAtoi(self, str: str) -> int:

        nbr = 0
        #str = str.strip()
        complete = False
        index = 0
        count = 0
        #negative = False
        for x in str[::-1]:
            if complete and not x.isspace():
                nbr = 0
                # str = str.strip()
                complete = False
                index = 0
                count = 0



            index +=1
            if x.isdigit():
                nbr = nbr + pow(10,count) * int(x)
                count +=1
            elif complete and not x.isspace():
                nbr = 0
                # str = str.strip()
                complete = False
                index = 0
                count = 0
            elif count >0:

                if x is '-':
                    nbr = -1 * nbr
                    complete = True
                elif x is '+':
                    complete = True
                elif x.isspace():
                    complete = True
                else:
                    nbr = 0
                    # str = str.strip()
                    complete = False
                    index = 0
                    count = 0



        if nbr <= pow(2, 31) * -1:
            return pow(2, 31)*-1
        if nbr >= pow(2, 31) - 1:
            return pow(2, 31) - 1
        return nbr


if __name__ == '__main__':
    print(Solution().myAtoi("    -88827   5655  U"))