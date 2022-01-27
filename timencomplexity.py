def fun(n):
    if n==1:
        return 1
    else:
        return fun(n-1) + fun(n-1) 
print(fun(5))
