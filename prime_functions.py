"""Functions to find the largest prime factor of 600851475143"""

def is_factor(num, fact):
    """Check whether fact is a factor of num"""
    if num % fact == 0:
        return True
    else:
        return False


def is_prime(number):
    """Check whether number is prime or composite."""
    for i in range(2, number):
        # Check whether number has any factors besides 1 and itself
        if is_factor(number, i):
            return False
        else:
            continue
    # Return True if no factors are found
    return True


def find_pfs(number):
    """Find the prime factors of a number and store them in a list."""
    prime_factors = []
    i = 2
    while number != 1:
        # Check whether i is a factor of number and whether i is prime.
        if is_factor(number, i) and is_prime(i):
            # Add prime factors to the list.
            prime_factors.append(i)
            # Factor out the most recent prime factor.
            number /= i
            continue
        else:
            # Check the next number.
            i += 1
            continue
    return prime_factors


def list_primes(num):
    """List all the prime numbers less than num."""
    if num < 2:
        raise ValueError("Number must be greater than or"
                         "equal to 2.")
    # Initiate primes with the first prime number.
    primes = [2]
    for i in range(3, num):
        if is_prime(i):
            primes.append(i)
            # Skip to the next odd number.
            i += 2
    return primes


if __name__ == '__main__':
    number = int(input("Enter a number to test primeness: "))
    if is_prime(number):
        print(f'{number} is prime.')
    else:
        print(f'{number} is composite.')
