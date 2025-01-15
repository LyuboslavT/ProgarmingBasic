import math

exam_hh = int(input())
exam_mm = int(input())
arrive_hh = int(input())
arrive_mm = int(input())

exam_in_mm = exam_hh * 60 + exam_mm
arrive_in_mm = arrive_hh * 60 + arrive_mm
difference = exam_in_mm - arrive_in_mm


if abs(difference) < 0:
    print('Late')
    if abs(difference) >= 60:
        hh_late = abs(difference) // 60
        mm_late = abs(difference) % 60
        print(f'{hh_late}:{mm_late} hours after the start')
    else:
        print(f'{abs(difference)} minutes after the start')

elif abs(difference) == 0 or abs(difference) <= 30:
    print('on time')
    if difference <= 30:
        print(f'{abs(difference)} minutes before the start')

else:
    print('Early')
    if difference >= 60:
        hh = abs(difference) // 60
        mm = abs(difference) % 60
        if mm < 10:
            print(f'{hh}:0{mm} hours before the start')
        elif hh > 0:
            print(f'{hh}:{mm} hours before the start')
    else:
        print(f'{abs(difference)} minutes before the start')
