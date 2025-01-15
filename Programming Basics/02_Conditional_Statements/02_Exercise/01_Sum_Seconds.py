time_first = int(input())
time_second = int(input())
time_third = int(input())

time_together = time_first \
                + time_second \
                + time_third

time_in_minutes = time_together // 60
time_seconds = time_together % 60

if time_seconds <10:
    print(f'{time_in_minutes}:0{time_seconds}')
else:
    print(f'{time_in_minutes}:{time_seconds}')

