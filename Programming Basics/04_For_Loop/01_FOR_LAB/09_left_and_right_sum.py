count = int(input())

left_sum = 0
right_sum = 0

for left in range(count):
    left_sum += int(input())

for right in range(count):
    right_sum += int(input())

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')

else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')

# range_numbers = int(input())

#left_sum = 0
#right_sum = 0

'''
0 1 2 3
'''
#for number in range(range_numbers*2):
  #  number_to_add = int(input())
 #   if number < range_numbers:
 #       left_sum += number_to_add
#    elif number >= range_numbers:
#        right_sum += number_to_add

# for left in range(range_numbers):
#     left_sum += int(input())
#
# for right in range(range_numbers):
#     right_sum += int(input())


#if left_sum == right_sum:
  #  print(f"Yes, sum = {left_sum}")
#else:
  #  diff = abs(left_sum - right_sum)
 #   print(f"No, diff = {diff}")