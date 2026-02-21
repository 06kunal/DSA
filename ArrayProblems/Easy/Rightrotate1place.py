nums = [5,-2,3,9,0,6,10,7]

class Solution:
    
    def rotatebyoneS(self, nums):
        n = len(nums)
        nums[:] = [nums[-1]] + nums[0:n-1]
          
    #Another Method:
    def rotatebyone(self, nums):
        
        n = len(nums)
        last = nums[-1]
             
        for i in range(n-1,0,-1):
            print(i)
            nums[i] = nums[i-1]
        nums[0]=last
           
sol = Solution()
print(sol.rotatebyone(nums), nums)