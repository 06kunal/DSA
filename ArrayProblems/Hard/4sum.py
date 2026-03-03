# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


class Solution:
    
    
    def Brutesum(self, nums, target):
        
        n = len(nums)        
        my_set = set()
        
        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l]== target:
                            temp = [nums[i],nums[j],nums[k], nums[l]]                        
                            temp.sort()     
                            my_set.add(tuple(temp))
                            
        
        return [list(ans) for ans in my_set]
            
        
    
    # fourth = target - (nums[i] + nums[j] + nums[k])
    def bettersum(self, nums, target):
        n = len(nums)
        res = set()
        
        for i in range(0, n):
            for j in range(i+1, n):
                hashset = set()
                for k in range(j+1, n):
                    fourth = target - (nums[i] + nums[j] + nums[k])
                    if fourth in hashset:
                        temp = [nums[i],nums[j],nums[k], fourth]
                        temp.sort()
                        res.add(tuple(temp))
                    hashset.add(nums[k])
         
        return  [list(ans) for ans in res]  
    
    
    
    
    def optimalsum(self, nums, target):
        n = len(nums)
        nums.sort()
        res = []
        
        
        for i in range(0, n):
            if(i>0 and nums[i] == nums[i-1]):
                    continue
            for j in range(i+1, n):
                
                if(j>i+1 and nums[j] == nums[j-1]):
                    continue
                k = j+1
                l = n-1
                
                while(k<l):
                    
                    if nums[i] + nums[j] + nums[k] + nums[l]< target:
                        k+=1
                    elif nums[i] + nums[j] + nums[k] + nums[l]> target:
                        l-=1
                    else:
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                        while(k<l and nums[k] == nums[k-1]):
                            k+=1
                        while(k<l and nums[l] == nums[l+1]):
                            l-=1
                            
        return res            
            
        
        
        
nums = [1,0,-1,0,-2,2] 
target = 0
sol = Solution()

print(sol.Brutesum(nums, target))
print(sol.bettersum(nums, target))
print(sol.optimalsum(nums, target))