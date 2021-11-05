import math

def is_prime(n):

    if n <= 1:
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
y = math.floor(math.sqrt(x)) + 1  

while True:
    if x % y == 0 and is_prime(y):
        break
    else:
        y = y-1
    
print(y)