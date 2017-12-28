from textwrap import fill
import prime_functions as pf

number = int(input("Find primes up to what number? "))
# Save primes to a list.
primes = pf.list_primes(number)

for prime in primes[0:len(primes)-1]:
    print(prime, end=', ')
print(primes[len(primes)-1])
# Print length of primes.
print(f'Number of primes less than {number}: {len(primes)}')
# Pause before exiting.
input()
