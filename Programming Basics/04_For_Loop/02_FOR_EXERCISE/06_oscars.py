import math

actor_name = input()
academy_given_points = float(input())
judge_count = int(input())

judge_name = ''
judge_given_points = 0
total_points = 0 + academy_given_points
points_earned = 0

for _ in range(judge_count):
    judge_name = input()
    judge_given_points = float(input())
    points_earned = (len(judge_name) * judge_given_points / 2)

    total_points += points_earned

    if total_points >= 1250.5:

        print(f'Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!')
        break

else:
    points_need = 1250.5 - total_points
    print(f'Sorry, {actor_name} you need {points_need:.1f} more!')