n=int(input('enter the no :'))
fact=1
for i in range(n,1,-1):
    fact=fact*i
print(fact)


def fact(n):
    if n==0:
        print('factorial')
    elif n<0:
        print('negative no')
    else:
        
