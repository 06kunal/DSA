# 0 1 1 2 3 5 8 


def fib(n):
    first = 0
    second = 1
    if n <= 1:
        return n
    
    while n>=2:
        third = first + second
        first = second
        second = third
        n -= 1
    return third

print(fib(4))


# Using recursion

def fibRec(n):
    if n <= 1:
        return n
    return fibRec(n-1) + fibRec(n-2)   
print(fibRec(1)) 

'''
Time: O(2^n)
Space: O(2^n)
'''