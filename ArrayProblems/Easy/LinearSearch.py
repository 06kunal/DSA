

class Solution:
    
    def search(self, nums, x):
        n = len(nums)
        for i in range(0, n):
            if nums[i] == x:
                return i
        return -1


nums =  [1, 2, 3, 4]
x = 4
sol = Solution()
print(sol.search(nums, x))