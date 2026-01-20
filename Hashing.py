'''
Frequency Map/ Dictionary

How to store frequency in Dictionary


nums = [5, 5, 7, 7, 1, 1, 1, 5, 4, 4, 4, 4, 6]

Now I want the frequency of every number.
key : n-value

Two methods:
Method 1: using normal code. 

create empty dictionary. 
start with 1st element check if its already present. 
If yes then +1 its value and if no then add the key with value 1.


This is called frequency Map

Syntax:

freq_map = dict() or {}


searching, updating and adding in dictionary is O(1).
'''

nums = [5, 5, 7, 7, 1, 1, 1, 5, 4, 4, 4, 4, 6]
x = 1

freq_map = dict()

for i in range (0, len(nums)):
    if nums[i] in freq_map:
        freq_map[nums[i]] += 1

    else:
        freq_map[nums[i]] = 1

print(freq_map[x])

'''
Time: O(n)
Space: O(n)
'''

#Method 2: using hashmap.get(key, 0). 
# This ,.get will return the value for the corresponding key. 
# If it is not present then it will return 0.

nums_list = [5, 5, 7, 7, 1, 1, 1, 5, 4, 4, 4, 4, 6]


Hash_Map = {}
n = len(nums_list)

for i in range(0, n):
    Hash_Map[nums_list[i]] = Hash_Map.get(nums_list[i], 0) + 1

print(Hash_Map[x])

'''
Time: O(n)
Space: O(n)
'''



#Hashing Concept. 
'''
Same concept for every language.
Prestoring values into same data structure like list/dictoinary and then fetching it.

Prestoring means that we will store the values for our use
before solving the question.

'''
#Q1: given two lists, check the number of occurence of an element
# in the another list.


#Brute force approach
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

freq = dict()

for i in m:
    count = 0
    for j in n:
        if i == j:
            count += 1
    freq[i] = count

print(freq)


'''
Time: O(n*m)
space: O(n);
'''


