def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(start, end):
    """Find all prime numbers in a given range."""
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

# Example usage
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
print(f"Prime numbers between {start} and {end}: {find_primes(start, end)}")
