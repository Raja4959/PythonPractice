# Decorator to check the input list has valid integers
def check_list(func):
    def wrapper(*args, **kwargs):
        chk = [isinstance(num, int) for num in kwargs['nums']]
        if all(chk):
            return func(kwargs['nums'])
        return "Invalid list items"
    return wrapper


# program to find out prim numbers present in a list
@check_list
def list_primes(nums: list):
    primes = []
    for num in nums:
        is_prime = True
        if num == 1 or num == 2:
            primes.append(num)
            continue
        for i in range(2, (num//2)):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    return primes


input1 = [9, 3, 8, 15, 17, 2, 29, 3]
print(list_primes(nums=input1))
input2 = [9, 3, 8, 15, '17', 2, 29, 3]
print(list_primes(nums=input2))
