#nums = [2,7,11,15], target = 9
# return the index. One solution will always exist.
# only one solution exists.
# Only use element once.


class Solution:
    
    def twosum(self, nums, target):
        res = []
        dict = {}
        n = len(nums)
        
        for i in range(0, n):
            left = target - nums[i]
            if left in dict:
                return [dict[left], i]

            dict[nums[i]] = i
    
nums = [2,7,11,15]
target = 18
sol = Solution()
print(sol.twosum(nums, target))




