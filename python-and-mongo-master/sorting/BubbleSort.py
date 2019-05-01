# Function to do bubble sort
def bubbleSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(0, len(arr)-1):

        for j in range (0, len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print(arr)
    # Driver code to test above


arr = [12, 11, 10, 6, 5]
bubbleSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])