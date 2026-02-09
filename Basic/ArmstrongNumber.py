'''

Armstrong number: whent the sum of its digit's power to the number of the digits is same as the number.
153 = 1^3 + 5^3 + 3^3
    = 1 + 125 + 27
    = 153

'''

from math import *

num = 153
n = num
sum = 0

#length = len(str(num))

length = int(log10(num)) + 1
print(length)

while(n>0):
    last_digit = n %10
    n = n//10
    sum = sum + last_digit**length
    print(sum)

if num == sum:
    print(True)
else:
    print(False)

'''
Time: O(log10(n))
Space: O(1)
'''