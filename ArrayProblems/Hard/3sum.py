# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.


class Solution:
    
    
    # Time: O(n3), Space: O(number of triplets)
    def brutesum(self, nums):
        
        my_set = set()
        n = len(nums)
        
        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i],nums[j],nums[k]]                        
                        temp.sort()     # -> its time will be almost negligible because only sorting three elements.
                        my_set.add(tuple(temp))  # -> we cannot add List in a set. So we add a list.
        
        return [list(ans) for ans in my_set]
    
    
    
    # so basically we'll try to eliminate the third loop.
    # Time: O(n2), Space: O(n + number of triplets)
    def Bettersum(self, nums):
        
        n = len(nums)       
        result = set()
        
        for i in range(0, n):
            my_set = set()            
            for j in range(i+1, n):
                if -(nums[i] + nums[j]) in my_set:
                    temp = [nums[i], nums[j], -(nums[i] + nums[j])]
                    temp.sort()
                    result.add(tuple(temp))
                my_set.add(nums[j])
                
        return [list(ans) for ans in result]
    
    
    
    # Basically we will fix one pointer and then use two pointers inside the loop.
    # Time: -> O(n2) + O(nlogn), space: O(1)
    def Optimalsum(self, nums):
        
        n = len(nums)
        res = []
        nums.sort()
        
        for i in range(0, n):
            
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            j = i+1
            k = n-1
            while(j<k):
                if nums[i] + nums[j] + nums[k] < 0:
                    j+=1
                elif nums[i] + nums[j] + nums[k] > 0:   
                    k -=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k -= 1
                        
        return res
    
    # Below is not an optimal solution due to the overhead of converting list in to tuple and then tuple into list. also the set used will considered as an extra space. Space: O(number of triplets)
        
        # n = len(nums)
        # res = set()
        # nums.sort()
        
        # for i in range(0, n):
            
        #     if i != 0 and nums[i] == nums[i-1]:
        #         continue
            
        #     j = i+1
        #     k = n-1
        #     while(j<k):
        #         if nums[i] + nums[j] + nums[k] < 0:
        #             j+=1
        #         elif nums[i] + nums[j] + nums[k] > 0:   
        #             k -=1
        #         else:
        #             res.add(tuple([nums[i], nums[j], nums[k]]))
        #             j+=1
        #             k-=1
        # return [list(ans) for ans in res]
        
        
                      
                    
nums = [1,2,0,1,0,0,0,0]
# [0,0,0,0,0,1,1,2]
sol = Solution()

print(sol.brutesum(nums))
print(sol.Bettersum(nums))
print(sol.Optimalsum(nums))
