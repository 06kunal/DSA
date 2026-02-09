s = 'aabbaa'

def isPalindrome(s):
    l = 0
    r = len(s) - 1
    
    while l<=r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return False
    return True    


print(isPalindrome(s))


'''
Time: O(n)
Space: O(1)
'''

# using recursion

def isPalindromeRec(s, left, right):
    if left >=right:
        return True
    elif s[left] == s[right]:
        return isPalindromeRec(s, left + 1, right -1)
    else:
        return False
    
print(isPalindromeRec(s, 0, len(s)-1))

'''
Time: O(n/2)-> O(n)
Space: O(n/2)-> O(n)
'''
