'''
It works one adjacent swaps
swap with the adjacent. Keep pushing the largest to the right.


'''

arr = [5, 7, 8, 4, 1, 6, 9, 2, 8]

n = len(arr)

while(n>0):
    is_swap = False
    for i in range(0, n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            is_swap = True
    n-=1
    
    if is_swap == False:
        print("Array is sorted.")
        break 

print(arr)

'''
Time:O(n^2)
Space: O(1)
'''