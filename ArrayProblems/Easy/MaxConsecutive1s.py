
class Solution:
    
    def maxconsecutive(self, nums):
        count = 0
        res = 0
        
        for i in nums:
            if i == 1:
                count += 1
            else:
                
                res = max(res, count)
                count = 0
        return res
        



nums = [1,0,1,1,0,1,1,1,1,0,0,0,0,1,1,0,1,1,1,0,0,0,1,0]
sol = Solution()
print(sol.maxconsecutive(nums))