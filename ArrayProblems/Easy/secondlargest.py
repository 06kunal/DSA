arr = [1,2,3,4,5,6,7,8,9,10]

class Solution:
    
    def SecondLargest(self, arr):
        
        largest = -float("inf")
        secondlargest = -float("inf")
        smallest = float("inf")
        secondsmallest = float("inf")
        ans = []
        
        for i in arr:
            if i > largest:               
                secondlargest = largest
                largest = i
                
            elif i > secondlargest and i != largest:
                secondlargest = i
                
                
        ans.append(secondlargest)        
        for i in arr:
            if i < smallest:               
                secondsmallest = smallest
                smallest = i
            elif i < secondsmallest and i != smallest:
                secondsmallest = i    
        ans.append(secondsmallest)        
        return ans
    

sol = Solution()
print(sol.SecondLargest(arr))
