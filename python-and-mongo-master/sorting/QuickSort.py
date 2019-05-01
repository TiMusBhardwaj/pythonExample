# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
# def partition(arr, low, high):
#     i = (low - 1)  # index of smaller element
#     print("index of i " + i.__str__())
#     pivot = arr[high]  # pivot
#
#     for j in range(low, high):
#
#         # If current element is smaller than or
#         # equal to pivot
#         if arr[j] <= pivot:
#             # increment index of smaller element
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return (i + 1)


def partition2(arr, low, high):

    i= low
    j= high
    pivot = arr[high]  # pivot
    pivotIndex = high
    test = 'left'
    while i!=j:
        if(test == 'left'):
            if(arr[i] > pivot):
                arr[i],arr[pivotIndex] = arr[pivotIndex],arr[i]
                test = 'right'
                pivotIndex = i
            i+=1
            #j -=1
        elif(test == 'right'):
            if(arr[j] < pivot):
                arr[j], arr[pivotIndex] = arr[pivotIndex], arr[j]
                pivotIndex = j
                test = 'left'
            #i+=1
            j-=1
    return i

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition2(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    # Driver code to test above


arr = [10, 2, 8, 9, 8,1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),

