interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

combination_counter = 0
is_equal = False

for i in range(interval_start, interval_end + 1):
    for y in range(interval_start, interval_end + 1):
        combination_counter += 1
        product = i + y

        if product == magic_number:
            is_equal = True
            print(f'Combination N:{combination_counter} ({i} + {y} = {magic_number})')
            break

    if is_equal:
        break
else:
    print(f'{combination_counter} combinations - neither equals {magic_number}')