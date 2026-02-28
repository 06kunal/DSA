# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

class Solution:
    
    def BruteMaxsum(self, nums):
        
        maxsum = float("-inf")
        n = len(nums)
        for i in range(0, n):
            sum = nums[i]
            for j in range(i+1, n):
                sum = sum + nums[j]
                maxsum = max(sum, maxsum)
        return maxsum
    
    
    #Kaden's Algorithm
    # if total is negative then make total -ve because it will not help in my answer.
    def OptimalMaxSum(self, nums):
        n = len(nums)
        maxi = float("-inf")
        total = 0
        for i in nums:
            total += i
            maxi = max(maxi, total)
            if total <0:
                total = 0
                
        return maxi
        
                

nums = [5,4,-1,7,8]
sol = Solution()

print(sol.BruteMaxsum(nums))
print(sol.OptimalMaxSum(nums))
