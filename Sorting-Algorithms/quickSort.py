# 1. Pick a Pivot:
#     -> It can be any random element. Can be first/last/middle/any random element.
# 2. Put Pivot at its correct Position/Index


# nums =[4,1,7,6,3,2,8]
# let's say pivot is 4, then put 4 at its correct position and put greater than 4 to its right side and everything lower than 4 to its left side.
# At the end we will get [1,3,2,4,7,6,8]

# Now repeat the same process for the subarray lower than 4 and the subarray greater than 4.

# So merge sort uses an extra array to sort but quick sort is inplace that is it uses the original array and changes it.

count = 0
def partition(arr, low, high):
    global count
    pivot = arr[low]
    i = low
    j = high
    
    
    while(i<j):
        while(arr[i]<=pivot and i<=high - 1):
            i += 1
            
        while(arr[j]>pivot and j>=low + 1):
            j -= 1
        
        if(i<j):
            arr[i],arr[j] = arr[j], arr[i]
    
    count +=1       
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr, low, high):
    global count
    if low<high:
        count +=1        
        pivotIndex = partition(arr, low, high)
        quick_sort(arr, low, pivotIndex-1)
        quick_sort(arr, pivotIndex+1, high)
    

arr =[1,2,3,4,5,6]
quick_sort(arr, 0, len(arr)-1)
print(arr)
print(count)


# Time: O(nlogn) in worst case when the array will be sorted or when the complete array will have the same element, then time is O(n^2) because it will do n(n-1)/2 comparisions.
# Space: O(1)

