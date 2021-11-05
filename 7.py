import math

def is_prime(n):

    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(2, math.floor(math.sqrt(n))+1):
            if n % i == 0:
                return False
                break
            
        return True
    
cnt = 0
i = 1
while cnt < 10001:
    if is_prime(i):
        cnt = cnt + 1
    i = i+1
    
print (i-1)