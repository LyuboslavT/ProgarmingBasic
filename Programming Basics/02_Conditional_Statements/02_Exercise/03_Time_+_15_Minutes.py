hours = int(input())
minutes = int(input())

hours_in_minutes = hours * 60
all_minutes = hours_in_minutes + minutes + 15
hours1 = all_minutes // 60
minutes1 = all_minutes % 60

if hours1 == 24:
    hours1 = 0

if minutes1 < 10:
    print(f'{hours1}:0{minutes1}')
else:
    print(f'{hours1}:{minutes1}')


MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
TIME_ADD = 15

hour = int(input())
minutes = int(input()) + TIME_ADD

if minutes >= 60:
    minutes -= MINUTES_IN_HOUR
    hours += 1

if minutes < 10:
    print(f'{hour}:{minutes:02d}')
else:
    print(f'{hour}:{minutes}')
