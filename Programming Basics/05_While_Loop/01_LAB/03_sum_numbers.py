number = int(input())

total_sum = 0

while total_sum <= number:
    current_number = int(input())
    total_sum += current_number

    if total_sum >= number:
        print(total_sum)
        break
