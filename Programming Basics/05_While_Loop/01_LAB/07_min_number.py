from sys import maxsize

max_size = maxsize

while True:
    user_input = input()

    if user_input == 'Stop':
        break

    number = int(user_input)

    if number < max_size:
        max_size = number

print(max_size)