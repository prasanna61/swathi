num=int(input('Enter a num:'))
temp=x=num
sum=0
digits=0
while num>0:
    num=num//10
    digits+=1
while x>0:
    rem=x%10
    sum=sum+rem**digits
    x=x//10
if temp==sum:
    print('armstrong')
else:
    print('Not armstrong')
