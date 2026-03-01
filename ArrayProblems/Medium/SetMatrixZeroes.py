

class Solution:
    
    def setzero(self, matrix):
        
        r = len(matrix)
        c = len(matrix[0])
        print(c)
        
        res = [[0]*c for _ in range(r)]
        for i in range(0, r):
            for j in range(0, c):             
                res[i][j] = matrix[i][j]
                        
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == 0:
                    for k in range(0, c):
                        res[i][k] = 0
                    for k in range(0, r):
                        res[k][j] = 0
                    
        for i in range(0, r):
            for j in range(0, c):             
                matrix[i][j] = res[i][j]
                
                
    # Not using another array
    def matrixzero(self, matrix):
        
        r = len(matrix)
        c = len(matrix[0])
        
                        
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == 0:
                    for k in range(0, c):
                        if matrix[i][k] != 0:
                            matrix[i][k] = float("inf")
                    for k in range(0, r):
                        if matrix[k][j] != 0:
                            matrix[k][j] = float("inf")
                            
    
    # Optimal Approach
    def optimalset(self, matrix):
        
        r = len(matrix)
        c = len(matrix[0])
        
        coltrack = [0]*c
        rowtrack = [0]*r
        
                        
        for i in range(0, r):
            for j in range(0, c):
                if matrix[i][j] == 0:
                    coltrack[j] = -1
                    rowtrack[i] = -1
                    
        for i in range(0, r):
            for j in range(0, c):
                if rowtrack[i] == -1 or coltrack[j] == -1:
                    matrix[i][j] = 0
        
        

                            
        

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix3 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

sol = Solution()

sol.setzero(matrix)
sol.matrixzero(matrix2)
sol.optimalset(matrix3)
print(matrix)
print(matrix2)
print(matrix3)