def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fib(n-1) + fib(n-2)
    
cumsum = 0 
i=1

while fib(i) < 4e6:
    cumsum+=fib(i)
    i+=3
    
print(cumsum)