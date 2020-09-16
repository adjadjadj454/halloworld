print('waring:you cannot input chinese')
a = input()
for i in range(len(a)):    
    print("ascii of " + a[i] + " is: " + ascii(ord(a[i])))