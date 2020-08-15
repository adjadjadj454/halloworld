import random
while True:
    q=random.randint(0,24)
    b=random.randint(0,24)
    c=random.randint(0,24)
    j=random.randint(0,24)
    print(q;b;c;j)
    users=input('please your number')
    if users=='+' or users=='-' and q+users+b+c+j==24:
        print('you win')
        break
    else:
        print('youb lose')
        break