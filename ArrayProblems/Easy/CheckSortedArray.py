arr = [1,3,2,4,5]

class Solution:
    
    def checkSortedArray(self, arr):
        for i in range(0, len(arr)-1):
            if arr[i+1] < arr[i]:
                return False
        return True
                
sol = Solution()
print(sol.checkSortedArray(arr))