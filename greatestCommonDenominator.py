num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

max_divisor = num2

if num1 < num2:
    max_divisor = num1

for divisor in range (max_divisor, 0, -1):
    if num1 % divisor == 0 and num2 % divisor == 0:
        print(f"{divisor} is the greatest common divisor for {num1} and {num2}")
        break


# can import 'math' lib which has a gcd method that take 2 inputs and returns the GCD
# ans = math.gcd(num1, num2)

