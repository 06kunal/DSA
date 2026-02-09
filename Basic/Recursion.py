# Recursion - when a function calls itfelf.

# question print kunal 4 times.
# Head Recursion: first we will do the job then call the function.

def func(count):
    if count == 4:
        print("ending head recursion")
        return 
    
    print(count, ": Kunal")
    count += 1
    func(count)

func(0)


# Tail Recursion: first we will call the function and then we'll do the job.

def fun(count):
    if count == 4:
        print("ending tail recursion")
        return 
    
    count += 1
    fun(count)
    print(count, ": Kunal")

fun(0)


'''
Time: O(n+1) -> O(n)
Space: O(n+1) -> O(n)
'''



