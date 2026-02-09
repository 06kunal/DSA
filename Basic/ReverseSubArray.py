arr= [1, 2, 3, 4, 5, 6, 7]

l = 1
r = 3

def reverse(l, r):
    if l == r or l > r:
        return

    x = arr[l]
    arr[l] = arr[r]
    arr[r] = x
    return reverse(l+1, r-1)

reverse(l, r)
print(arr)

