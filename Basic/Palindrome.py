
n = 121
num = n
rem = 0
reverse = 0


while(n>0):
    rem = n%10 
    n = int(n//10) 
    reverse = reverse*10 + rem

if reverse == num:
    print("True")
else:
    print(False)
    


'''
Time: O(log10(n))
Space: O(1)
'''


    




