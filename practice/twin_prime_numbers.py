def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_twin_prime(num1, num2):
    """Check if two numbers are twin primes."""
    if abs(num1 - num2) == 2:
        return is_prime(num1) and is_prime(num2)
    return False

# Example usage:
num1 = 11
num2 = 13

if is_twin_prime(num1, num2):
    print(f"({num1}, {num2}) are twin primes.")
else:
    print(f"({num1}, {num2}) are NOT twin primes.")