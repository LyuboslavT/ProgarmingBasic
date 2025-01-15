number = int(input())

third_digit = number % 10
second_digit = (number // 10) % 10
first_digit = number // 100

if first_digit == 0 or second_digit == 0 or third_digit == 0:
    print("no digit should be 0")
elif first_digit < 0 or second_digit < 0 or third_digit < 0:
    print("no digit should be < 0")


for i in range(1, third_digit + 1):
    for j in range(1, second_digit + 1):
        for k in range(1, first_digit + 1):
            result = i * j * k
            print(f'{i} * {j} * {k} = {result};')
