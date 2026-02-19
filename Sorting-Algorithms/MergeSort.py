# Merge sort works on divide and merge or divide and conquor.
# Keep on dividing until we get to the last element and then compare them both and then merge.

# [3, 1, 2, 4, 1, 5, 2, 6, 4]
# n = 9

# [3,1,2,4] and [1,5,2,6,4]
#   /   \
#[3,1] [2,4] 
# / \      /\
#[3] [1] [2] [4]

# return merge[1,3] 
# and for [2,4]-> return merge[2,4]
# now for [1,3] and [2,4] -> return merge [1,2,3,4]
# similarly for [1,5,2,6,4]

#for merging, we will use two pointers in the two array and compare them and store in a separate arr.


arr = [3, 1, 2, 4, 1, 5, 2, 6, 4]
l = 0
r = len(arr) - 1

def MergeSort(arr, l, r):
    if l<r:
        mid = int(l+(r-l)/2)
        # print(mid)
        MergeSort(arr, l, mid)
        MergeSort(arr, mid + 1, r)
        
        return merge(arr, l, mid, r)

def merge(arr,l,m, r):
    i = 0  
    j = 0
    res = arr
    left = arr[l : m+1]
    right = arr[m+1 : r + 1]
    n = len(left)
    mr = len(right)
    k=l
   
    while(i < n and j < mr):
        if left[i] <= right[j]:
            res[k] = left[i]
            i = i + 1
        else:
            res[k] = right[j]
            j = j + 1
        k += 1
    
    if i < n:
        while(i<n):
            res[k] = left[i]
            i = i + 1
            k += 1
            
    if j < mr:
        while(j<mr):
            res[k] = right[j]
            j = j + 1  
            k += 1   
    
    return res       


print(MergeSort(arr, l, r))


# Time: O(nlogn)
# Space: O(n) -> for the extra array that we used in merge.

