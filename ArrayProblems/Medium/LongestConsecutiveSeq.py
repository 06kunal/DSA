# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution:
    
    def Brutesequence(self, nums):
        
        n = len(nums)
        max_count = 0
       
        for i in range(0, n):
            count = 1
            num = nums[i]
            
            while num + 1 in nums:
                count += 1
                num += 1
                
            max_count = max(max_count, count)
        return max_count
        
    # Using Sorting
    def Bettersequence(self, nums):
        
        last_smaller = float("-inf")
        count = 0
        longest = 0
        n = len(nums)
        nums.sort()
        print(nums)
        for i in range (0, n):
            if nums[i] - last_smaller == 1:
                count += 1 
                last_smaller = nums[i]
                  
            elif last_smaller != nums[i]:
                count = 1
                last_smaller = nums[i]
            longest = max(count, longest)            
            
        return longest
    
    
    def Optimalsequence(self, nums):
        
        my_set = set()
        n = len(nums)
        
        for i in range(0, n):
            my_set.add(nums[i])
         
        longest = 0
        
        for num in my_set:
            if num-1 not in my_set:
                count = 1
                while num + 1 in my_set:
                    count += 1
                    num += 1
                longest = max(count, longest)
                
        return longest
        
nums = [0,0]
sol = Solution()
print(sol.Brutesequence(nums))
print(sol.Bettersequence(nums))
print(sol.Optimalsequence(nums))   #-> Time: O(n + n + n) because while loop will only run when there will be a sequence. So at an average it will take O(n) time. 
            



