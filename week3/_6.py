def prime_numbers():
    numbers = input("Enter numbers: ").split()
    numbers = [int(num) for num in numbers]
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_nums = [num for num in numbers if is_prime(num)]
    print("Prime numbers:", prime_nums)

prime_numbers()