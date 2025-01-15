number = int(input())

x1 = 0
x2 = 0
x3 = 0
combination_counter = 0

for x1 in range(number + 1):
    for x2 in range(number + 1):
        for x3 in range(number + 1):
            product = x1 + x2 + x3

            if product == number:
                combination_counter += 1

print(combination_counter)
                