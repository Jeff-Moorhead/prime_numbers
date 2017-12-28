import time
import prime_functions as pf

number = int(input("Find primes up to what number? "))
# Save primes to a list.
start = time.time()
primes = pf.list_primes(number)
end = time.time()

for prime in primes[0:len(primes)-1]:
    print(prime, end=', ')
print(primes[len(primes)-1])
# Print length of primes.
print(f'Number of primes less than {number}: {len(primes)}')
# Display total time of calculation.
print(f'The calculation took {end-start} seconds.')
# Pause before exiting.
input()
