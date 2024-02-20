# 1.Given number is prime number or not
def is_primenumber(num: int):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# 2.Generate a list of prime numbers within a given range
def primenumbers_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_primenumber(num):
            primes.append(num)
    return primes


# 3.Generate the first N prime numbers (count)
def primenumbers_upto(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_primenumber(num):
            primes.append(num)
        num += 1
    return primes


# 1. finding given number is prime or not
number = 13
if is_primenumber(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# 2.finding the prime numbers between given range
start_range = 10
end_range = 50
result = primenumbers_in_range(start_range, end_range)
print(f"Prime numbers between {start_range} and {end_range}: {result}")

# 3. finding first N the prime numbers
N = 15
result = primenumbers_upto(N)
print(f"The first {N} prime numbers are: {result}")
