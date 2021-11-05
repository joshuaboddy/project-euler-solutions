import math

def is_prime(n):

    if n <= 1:
        return False
    elif n==2:
        return False
    elif n % 2 == 0:
        return False
    else:
        for i in range(2, math.floor(math.sqrt(n))+1):
            if n % i == 0:
                return False
                break
            
        return True
      

x = 600851475143  
y = 2

while True:
    if x % y == 0:
        if is_prime(int(x/y)):
            break
        else:
            x = x / y
    else:
        y = y+1
    
print(x/y)
