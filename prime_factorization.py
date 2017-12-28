"""Find the prime factorization of any number."""

import time
import prime_functions as pf

while True:
    # Store the input in a variable.
    number = input("Enter a number or 'exit' to quit: ")
    # Check if the user wants to exit.
    if number.lower() == 'exit':
        break
    # Otherwise convert the input into an int.
    else:
        number = int(number)
    print("Calculating...")
    start = time.time()
    # Find the prime factors and store them in a list.
    prime_factors = pf.find_pfs(number)
    end = time.time()
    duration = round(end - start, 2)
    print("Calculation complete.\nPrime factorization: ")
    print("\t", end='')
    # Print the prime factorization of the number.
    if len(prime_factors) == 1:
        print(str(number) + " is prime.")
        break
    else:
        for factor in prime_factors[:(len(prime_factors) - 1)]:
            print(str(factor), end=" * ")
        print(prime_factors[len(prime_factors) - 1])
    print("Largest prime factor: " + str(max(prime_factors)) +
          "\nThe calculation took " + str(duration) + " seconds.\n")
    continue
