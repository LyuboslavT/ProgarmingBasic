import math
WATER_RESISTANCE_15_M = 12.5

record = float(input())
distance = float(input())
time_in_seconds_for_1_m = float(input())

time_distance = distance * time_in_seconds_for_1_m

slow_count = distance // 15
slow = slow_count * WATER_RESISTANCE_15_M
time = time_distance + slow

if time < record:
    print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')
else:
    need = time - record
    print(f'No, he failed! He was {need:.2f} seconds slower.')