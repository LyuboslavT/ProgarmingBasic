FACEBOOK_FINE = 150
INSTAGRAM_FINE = 100
REDDIT_FINE = 50

count = int(input())
salary = int(input())

fine = 0
fine_total = 0
tab = ''

for _ in range(count):
    tab = input()
    if tab == "Facebook":
        fine += FACEBOOK_FINE

    elif tab == 'Instagram':
        fine += INSTAGRAM_FINE

    elif tab == 'Reddit':
        fine += REDDIT_FINE

    if fine >= salary:
        print('You have lost your salary.')
        break
else:
    print(salary - fine)



