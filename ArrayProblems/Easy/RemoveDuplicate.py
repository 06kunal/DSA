# In dictionary, elements are stored uniquely and order is also maintained.


nums = [1,1,1,2,2,2,3,4,4,5,5,6,6]

class Solution:
    
    def removeDuplicate(self, nums):
        
        j = 0
        freq_map = {}
        
        for i in range(0, len(nums)):
            freq_map[nums[i]] = 0
        
        for k in freq_map:
            nums[j] = k
            j += 1
        
        return j


# using two pointers.

    def removeDuplicatetp(self, arr):
        
        i = 0
        
        for j in range(1, len(arr)):
            if arr[i]!= arr[j]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        return i+1
            

sol= Solution()
#print(sol.removeDuplicate(nums), nums)
print(sol.removeDuplicatetp(nums), nums)

        
        
        