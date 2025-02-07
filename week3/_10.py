def prime_numbers():
    numbers = map(int, input("Enter numbers: ").split())
    
    def filter_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0: return False
        return True
    print("Prime numbers:", [num for num in numbers if filter_prime(num)])

prime_numbers()