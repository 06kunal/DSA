'''
if arr[i+1] > arr[i]
    i++
else:
    put arr[i] at its correct position
    

'''

arr = [5, 7, 8, 4, 1, 6, 9, 2, 8] 


for i in range(0, len(arr) - 1):
    if arr[i+1] < arr[i]:
        key = arr[i+1]
        for j in range(i, -1, -1):
            print(j)
            if arr[j] > key:
                arr[j+1] = arr[j]            
                arr[j] = key
                
                
print(arr)

'''
Time: O(n^2)
Space: O(1)
'''