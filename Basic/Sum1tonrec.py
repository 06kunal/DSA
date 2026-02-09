

def fun(sum, n):
    if n == 0:
        return sum
    return fun(sum + n, n - 1)

print(fun(0, 10))


# another method
# 1. create a flow
# 2. write a base condition.

def func(n):
    if n == 1:
        return 1
    return n + func(n-1)

print(func(10))

