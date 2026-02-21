# Move zeros to the end with the order maintained with inplace

# Before -> nums = [1,0,2,4,3,0,0,3,5,1]
# After -> nums = [1,2,4,3,3,5,1,0,0,0]


class Solution:
    
    def movezeros(self, nums):
        n = len(nums)
        
        i = -1
        
        for j in range(0, n):
            if nums[j] != 0:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        if i != n-1:
            while(i<n-1):
                i+=1               
                nums[i] = 0
                  

        
        
        
                
nums = [1,0,2,4,3,0,0,3,5,1]

sol = Solution()
sol.movezeros(nums)
print(nums)
                   
                   