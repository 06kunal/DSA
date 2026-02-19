arr = [1, 8, 7, 56, 90]

class Solution:
    
    def largest(self, arr):
        
        largest = 0
        for i in arr:
            if i > largest:
                largest = i
        return largest
    
    

ans = Solution().largest(arr)
print(ans)
