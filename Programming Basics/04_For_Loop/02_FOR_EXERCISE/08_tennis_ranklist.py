# 	W - ако е победител получава 2000 точки
# 	F - ако е финалист получава 1200 точки
# 	SF - ако е полуфиналист получава 720 точки

# constants
WIN = 2000
FINAL = 1200
SEMI_FINAL = 720

# get input
tour_count = int(input())
starting_points = int(input())

result = ''
win_counter = 0
points_earned = 0

# starting for loop, iterating all of the tours
for _ in range(tour_count):
    step_won = input()

    # checking what step on which tour is achieved

    if step_won == "W":
        win_counter += 1
        points_earned += WIN

    elif step_won == 'F':
        points_earned += FINAL

    elif step_won == 'SF':
        points_earned += SEMI_FINAL

total_points_won = points_earned + starting_points

print(f'Final points: {total_points_won}')
print(f'Average points: {points_earned // tour_count}')
print(f'{win_counter / tour_count * 100:.2f}%')