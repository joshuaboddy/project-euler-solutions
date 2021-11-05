import math

def factorise(num):
    
    factors = []
    
    for potential_factor in range(1,math.floor(math.sqrt(num))+1):
        if num % potential_factor == 0:
            factors.append([potential_factor, int(num / potential_factor)])
            
    return factors
        
def has_three_digit_product(num):
    
    for factors in factorise(num):
        if len(str(factors[0])) == len(str(factors[1])) == 3:
            return True
            break
    
    return False

def is_palindrome(num):
    
    return str(num) == str(num)[::-1]
        
i = 999*999
palindrome = False
three_digit_product = True

while not (is_palindrome(i) and has_three_digit_product(i)):
     i = i-1

print(i)
    