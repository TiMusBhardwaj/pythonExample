# Python3 program to find the pair
# with sum
# closest to a given no.

# A sufficiently large value greater
# than any
# element in the input array
MAX_VAL = 1000000000


# Prints the pair with sum closest to x

def printClosest(arr, n, x):
    # To store indexes of result pair
    res_l, res_r = 0, 0

    # Initialize left and right indexes
    # and difference between
    # pair sum and x
    l, r, diff = 0, n - 1, MAX_VAL

    # While there are elements between l and r
    while r > l:
        # Check if this pair is closer than the
        # closest pair so far
        if abs(arr[l] + arr[r] - x) < diff:
            res_l = l
            res_r = r
            diff = abs(arr[l] + arr[r] - x)

        if arr[l] + arr[r] > x:
            # If this pair has more sum, move to
            # smaller values.
            r -= 1
        else:
            # Move to larger values
            l += 1

    print('The closest pair is {} and {}'
          .format(arr[res_l], arr[res_r]))


# Driver code to test above
if __name__ == "__main__":
    arr = [10, 22, 28, 29, 30, 40]
    n = len(arr)
    x = 54
    printClosest(arr, n, x)

# This code is contributed by Tuhin Patra
