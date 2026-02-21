# Find the missing number from the array


class Solution:
    
    def missing(self, nums):
        n = len(nums)
        freq = {}
        
        for i in range(0,n+1):
            freq[i] = 0
        
        for i in nums:
            freq[i] = 1
        
        for k, v in freq.items():
            if v == 0:
                return k
            
            
    # Optimal solution
    def missingOptimal(self, nums):
        n = int(len(nums))
        n_sum = n*(n+1)//2
        sum = 0
        for i in nums:
            sum = sum + i
        
        return n_sum - sum
                      


nums = [9,6,4,2,3,5,7,0,1]
sol = Solution()
print(sol.missing(nums))
print(sol.missingOptimal(nums))