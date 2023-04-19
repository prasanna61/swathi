n=int(input('enter how many nums do u want in series:'))
if n>2:
    a=0
    b=1
    print(a,end=' ')
    print(b,end=' ')
    while n-2>0:
        k=a+b
        a=b
        b=k
        print(k,end=' ')
        n-=1
else:
    print('enter a valid num')
