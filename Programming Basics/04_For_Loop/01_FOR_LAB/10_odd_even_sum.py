count = int(input())

total_sum = 0
diff = 0
odd_sum = 0
even_sum = 0

for i in range(count):
    current_num = int(input())

    if i % 2 == 0:
        even_sum += current_num

    else:
        odd_sum += current_num

if even_sum == odd_sum:
    print(f'Yes\nSum = {odd_sum}')

else:
    diff = abs(even_sum - odd_sum)
    print(f'No\nDiff = {diff}')