# Function to do bubble sort
def zinZagSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(0, len(arr)-1):
        temp = True
        for j in range (0, len(arr)-i-1):
            if(arr[j]>arr[j+1] and temp):
                arr[j],arr[j+1]=arr[j+1],arr[j]
            temp = not temp

        print(arr)
    # Driver code to test above


arr = [12, 11, 10, 6, 5]
zinZagSort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])