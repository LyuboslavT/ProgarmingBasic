hour = int(input())
day = str(input())

days_open = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
hours_open = [10, 11, 12, 13, 14, 15, 16, 17, 18]

if day in days_open and hour in hours_open:
    print('open')
else:
    print('closed')