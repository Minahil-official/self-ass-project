def divisors():
    num = int(input("enter your number:"))
    for i in range(num):
        current_divisor = i+1
        if num%current_divisor == 0:
            print(f"the divisors of {num} are {current_divisor}")
divisors()