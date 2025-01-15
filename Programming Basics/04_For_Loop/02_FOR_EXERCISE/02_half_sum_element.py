import math

number = int(input())

max_element = float("-inf")
sum_elements = 0

for _ in range(number):
    current_number = int(input())

    if current_number > max_element:
        max_element = current_number

    sum_elements += current_number

half_sum = sum_elements - max_element

if half_sum == max_element:
    print(f'Yes\nSum = {max_element}')

else:
    diff = abs(max_element - half_sum)
    print(f'No\nDiff = {diff}')




