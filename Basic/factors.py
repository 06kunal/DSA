#Print all the factors of a number in a list.
#ex: 10 -> {1, 2, 5, 10}



from math import *

# Brute Force:
n = 10
factors = []

for i in range(1, n+1):
    if n%i == 0:
        factors.append(i)
print(factors)

'''
Time: O(n)
Space: O(k), where k = no. of factors.
'''

    
#Optimised approach:

n1 = 10
factors1 = []

for i in range(1, n//2 + 1):
    if n1%i == 0:
        factors1.append(i)
factors1.append(n1)
print(factors1)


'''
Time: O(n/2)
Space: O(k), where k = no. of factors.
'''


#Optimised Solution 2
num = 36

list_f = []

for i in range(1, int(sqrt(num)) + 1):
    if num%i == 0:
        list_f.append(i)
        if num//i != i:
            list_f.append(num//i)

list_f.sort()
print(list_f)

'''
Time: O(sqrt(n)) + O(logn)
Space: O(k), where k = no. of factors.
'''

