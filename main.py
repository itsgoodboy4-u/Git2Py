# 1. Fibonacci Sequence
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# 2. Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# 3. Check Prime Number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 4. GCD (Greatest Common Divisor)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 5. LCM (Least Common Multiple)
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# 6. Palindrome Check
def is_palindrome(s):
    return s == s[::-1]

# 7. Sum of Digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# 8. Reverse a String
def reverse_string(s):
    return s[::-1]

# 9. Binary to Decimal
def binary_to_decimal(b):
    return int(b, 2)

# 10. Decimal to Binary
def decimal_to_binary(n):
    return bin(n)[2:]

if __name__ == "__main__":
    print("Fibonacci (10 terms):", fibonacci(10))
    print("Factorial (5):", factorial(5))
    print("Is 17 prime?", is_prime(17))
    print("GCD of 48 and 18:", gcd(48, 18))
    print("LCM of 48 and 18:", lcm(48, 18))
    print("Is 'radar' a palindrome?", is_palindrome("radar"))
    print("Sum of digits in 1234:", sum_of_digits(1234))
    print("Reverse of 'hello':", reverse_string("hello"))
    print("Binary '1010' to decimal:", binary_to_decimal("1010"))
    print("Decimal 10 to binary:", decimal_to_binary(10))
