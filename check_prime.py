num = int(input("Enter integer to be checked for primeness: "))

divisor = 1
divisor_count = 0

while divisor < num and num != 0:
    if (num % divisor) == 0:
        divisor_count += 1
        divisor += 1
    else:
        divisor += 1

if divisor_count > 2:
    print(f"{num} is not a prime number.")
else:
    print(f"{num} is a prime number.")
