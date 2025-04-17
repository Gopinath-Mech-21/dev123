def prime(a):
    n = []  # List to store prime numbers
    for j in range(2, a):  # Loop through numbers from 2 to a-1
        is_prime = True  # Assume j is prime
        for k in range(2, int(j**0.5) + 1):  # Check for factors up to the square root of j
            if j % k == 0:  # If j is divisible by k, it's not prime
                is_prime = False
                break  # No need to check further
        if is_prime:  # If j is still considered prime
            n.append(j)  # Add it to the list of primes
    return n  # Return the list of prime numbers

# Get user input
n = int(input("Enter the number: "))
b = prime(n)
print(b)
