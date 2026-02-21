
class Solution:
    
    def merge(self, a, b):
        
        res = []
        i = 0
        j = 0
        k = 0
        n1 = len(a)
        n2 = len(b)
        
        while i<n1 and j<n2:
            if a[i] <= b[j]:
                if len(res) == 0 or res[-1] != a[i]:
                    res.append(a[i])
                i +=1
            else:
                if len(res) == 0 or res[-1] != b[j]:
                    res.append(b[j])
                j +=1
        
        if i<n1:
            while(i<n1):
                if len(res) == 0 or res[-1] != a[i]:
                    res.append(a[i])
                i += 1
                
    
        if j<n2:
            while(j<n2):
                if len(res) == 0 or res[-1] != b[j]:
                    res.append(b[j])
                j += 1
        return res
                    

nums1 = [2, 2, 4, 6, 6, 8]
nums2 = [4,4,6]

sol = Solution()
print(sol.merge(nums1,nums2))