# 5 20 3 
# 7 -10 9 
# 1 -52 6 


nums = [[5,20,3], [7,-10,9], [1,-52, 6]]

rows = len(nums)
columns = len(nums[0])
print(rows, columns)


for i in range (0, rows):
    for j in range(0, columns):
        print(nums[i][j], end=" ")
    print()
    
print()
#print the upper triangle
# Output:
# 5 20 3 
# * -10 9 
# *  *  6 
print("Upper triangle")  
for i in range(0, rows):
    for j in range(0, columns):
        if j>= i:
            print(nums[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
    

print()
#print the lower triangle
# Output:
# 5  *  3 
# * -10 * 
# 1  *  6 

print("Lower triangle")  
for i in range(0, rows):
    for j in range(0, columns):
        if j<= i:
            print(nums[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
    
    
print()

#print the diagonal
# Output:
# 5 20 3 
# * -10 9 
# *  *  6 

print("Diagonal")  
for i in range(0, rows):
    for j in range(0, columns):
        if j == i:
            print(nums[i][j], end=" ")
        else:
            print("*", end=" ")
    print()
    
    
#creating an empty list with rows and columns

result = [[0]*columns for _ in range(rows)]
print(result)