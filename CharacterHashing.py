s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]

hash_list = [0]*26

for ch in s:
    ascii_value = ord(ch)
    index = ascii_value - 97
    hash_list[index] += 1

print(hash_list)

for ch in q:
    index = ord(ch) - 97
    print(hash_list[index])

'''
Time: O(n+m)
space: O(26) -> O(1)
'''