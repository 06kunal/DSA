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
        
        # Time: O(k) + O(n-k) -> O(n)
        # Space: O(1)
        
    
    
    
    
    #Before Rotation: [5,-2,3,9,0,6,10,7]
    #After Rotation: [6,10,7,5,-2,3,9,0]
    #Another method without using slicing -> best approach
    def reverse(self, nums, i, j):
        
        while(i<j):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    
    def rotateWreverse(self, nums, k):
        n = len(nums)
        self.reverse(nums,0,n-1)
        print(nums)
        self.reverse(nums, 0, k)
        self.reverse(nums, k+1, n-1)
    


sol = Solution()
#sol.rotatebyk(nums, 3)
# sol.rotatebykS(nums, 3)
sol.rotateWreverse(nums, 3)
print(nums)
        