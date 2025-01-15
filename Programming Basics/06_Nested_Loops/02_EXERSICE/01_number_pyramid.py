number = int(input())
current = 1
is_current_bigger = False

for n in range(1, number + 1):
    for m in range(1, n +1):

        if current > number:
            is_current_bigger = True
            break
        print(str(current) + ' ', end= '')
        current += 1
    if is_current_bigger:
        break

    print()