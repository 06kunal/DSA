#Optimised Approach

'''
constraints: 1 <= n[i] <= 10
'''

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]


hash_list = [0]*11


for i in n:
    hash_list[i] += 1

for i in m:
    if i < 1 or i >10:
        print(0)
    else:
        print(hash_list[i])

print(hash_list)

'''
Time: O(n + m)
space: O(10)
'''




#Using Disctionary
# we don't need constraint

freq_dict = dict()

for i in n:
    freq_dict[i] = freq_dict.get(i, 0) + 1

for i in m:
    if i in freq_dict:
        print(freq_dict[i])
    else:
        print(0)
 
print(freq_dict)






