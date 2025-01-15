import math
show_name = str(input())
episode_duration = int(input())
break_duration = int(input())

LUNCH = 0.125
REST = 0.25

lunch_time = break_duration * LUNCH
rest_time = break_duration * REST
break_remaining = break_duration - (lunch_time + rest_time)

if break_remaining >= episode_duration:
    time_left = break_remaining - episode_duration
    print(f'You have enough time to watch {show_name} and left with {math.ceil(time_left)} minutes free time.')
else:
    time_need = episode_duration - break_remaining
    print(f"You don't have enough time to watch {show_name}, you need {math.ceil(time_need)} more minutes.")
