nums = [5,-2,3,9,0,6,10,7]

class Solution:

    def rotatebyk(self, nums, k):
        n = len(nums)
        for _ in range(0, k):
            last = nums[-1]
        
            for i in range(n-1,0,-1):
                nums[i] = nums[i-1]
            nums[0] = last

    
    #Another Method using slicing
    def rotatebykS(self, nums, k):
        
        n = len(nums)
        r = k%n
        
        nums[:] = nums[n-r:] + nums[:n-r]
        
    


sol = Solution()
#sol.rotatebyk(nums, 3)
sol.rotatebykS(nums, 3)
print(nums)
        