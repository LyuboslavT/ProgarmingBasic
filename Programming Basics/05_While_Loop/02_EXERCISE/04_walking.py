GOAL = 10_000

steps_sum = 0
command = ''
result = ''

while steps_sum < GOAL:
    command = input()

    if command == 'Going home':
        steps_to_home = int(input())
        steps_sum += steps_to_home
        break

    steps_sum += int(command)

if steps_sum >= GOAL:
    diff = steps_sum - GOAL
    print(f'Goal reached! Good job!\n{diff} steps over the goal!')

else:
    diff = GOAL - steps_sum
    print(f'{diff} more steps to reach goal.')