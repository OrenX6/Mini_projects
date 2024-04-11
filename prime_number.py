
# Using a for...else statement
def prime_checker(number):
    if number % 2 == 0 or number < 2:
        print("It's not a prime number.")
    else:
        for i in range(2, number // 2):
            if number % i == 0:
                print("It's not a prime number.")
                return
        else:
            print("It's a prime number.")


# Using is_prime variable
def prime_checker2(number):
    is_prime = True
    if number % 2 == 0 or number < 2:
        is_prime = False
    else:
        for i in range(2, number // 2):
            if number % i == 0:
                is_prime = False
                return

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
prime_checker2(number=n)
