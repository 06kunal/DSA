
'''
start with min_index = 0
compare min index with the array and keep on updating the min_index
After completion swap the min_index with starting of outer loop.


'''

nums = [5, 7, 8, 4, 1, 6, 9, 2, 8]


def swap(a, b, arr):
    x = arr[a]
    arr[a] = arr[b]
    arr[b]=x


for i in range(0, len(nums)):
    min_index = i 
    for j in range(i+1, len(nums)):
        if(nums[j] < nums[min_index] ):
            min_index = j
            print(min_index)
    
    swap(min_index, i, nums) 
    
print(nums)       


'''
Time: O(n^2)
Space: O(1)
'''