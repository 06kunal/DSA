nums = [3,0,-2,-5,0,-4]


class Solution:
    
    def rearrange(self, nums):
        
        n = len(nums)
        positive = 0
        negative = 1
        res = [0]*n
        for i in nums:
            if i >= 0:
                res[positive] = i
                positive += 2
            else:
                res[negative] = i
                negative+=2                
        return res
    
sol = Solution()
print(sol.rearrange(nums))               
        
            
            
                