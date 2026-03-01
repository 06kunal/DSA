

class Solution:
          
    # Brute force
    def bruterotate(self, matrix):
        
        r = len(matrix)
        c = len(matrix[0])
        res = [[0]*c for _ in range(r)]
        
        rc = c-1               
        for i in range(0, r):
            rr = 0            
            for j in range(0, c):                
                res[rr][rc] = matrix[i][j]
                rr +=1
            rc -= 1
        
        for i in range(0, r):
            for j in range(0, c):             
                matrix[i][j] = res[i][j]
                
                            
    
    # Optimal Approach
    def optimalrotate(self, matrix):
        
        r = len(matrix)
        c = len(matrix[0])
        
                        
        for i in range(0, r):
            for j in range(i, c):                
                x = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = x
        
        for i in range(0, r):
            for j in range(0, c//2):                
                x = matrix[i][j]
                matrix[i][j] = matrix[i][c-1-j]
                matrix[i][c-1-j] = x

                            
        

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,2,3],[4,5,6],[7,8,9]]


sol = Solution()

sol.bruterotate(matrix)
sol.optimalrotate(matrix2)
print(matrix)
print(matrix2)



