BASIS = 5364
GOAL = 8848

current_height = BASIS
day_counter = 1

while True:
    command = input()
    if command == 'END':
        print(f'Failled!\n{current_height}')
        break

    if command == "Yes":
        day_counter += 1
        if day_counter > 5:
            print(f'Failled!\n{current_height}')
            break

    achieved_meters = int(input())
    current_height += achieved_meters

    if current_height >= GOAL:
        print(f'Goal reached for {day_counter} days!')
        break
