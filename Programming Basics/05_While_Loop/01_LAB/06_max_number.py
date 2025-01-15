from sys import maxsize

min_size = -maxsize


while True:
    user_input = input()

    if user_input == 'Stop':
        break

    number = int(user_input)

    if number > min_size:
        min_size = number

print(min_size)

