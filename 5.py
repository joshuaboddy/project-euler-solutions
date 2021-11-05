import math       

def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes

i = 20
primes = primes_sieve(i)
primes_and_powers = {}

for n in range(2,i+1):
    for prime in primes:
        if n % prime == 0:
            power = 1
            while n / (prime ** (power + 1)) >= 1:
                power = power + 1
            if prime in primes_and_powers.keys():
                primes_and_powers[prime] = max(primes_and_powers[prime], power)
            else:
                primes_and_powers[prime] = power
     
print(math.prod([key**power for key, power in primes_and_powers.items()]))