def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    n = int(input("Enter a positive integer (n): "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        print(f"Prime numbers up to {n}:")
        for number in range(2, n + 1):
            if is_prime(number):
                print(number, end=" ")
        print()  # Print a newline after the list of prime numbers
except ValueError:
    print("Invalid input. Please enter a positive integer.")
