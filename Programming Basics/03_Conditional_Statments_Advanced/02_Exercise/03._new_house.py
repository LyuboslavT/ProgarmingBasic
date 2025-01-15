ROSES = 5
DAHLIAS = 3.8
TULIPS = 2.8
NARCISSUS = 3
GALDIOLUS = 2.5

ROSES_MORE_THAN_80_DISC = 0.1
DAHLIAS_MORE_THAN_90_DISC = 0.15
TULIPS_MORE_THAN_80_DISC = 0.15
NARCISSUS_LESS_THAN_120_INCRS = 0.15
GALDIOLUS_LESS_THAN_80_INCRS = 0.2


flower_type = input()
flower_count = int(input())
budget = int(input())

total = 0
discount = 0
increase = 0

if flower_type == 'Roses':
    total = flower_count * ROSES

    if flower_count > 80:
        discount = total * ROSES_MORE_THAN_80_DISC
        total -= discount

elif flower_type == 'Dahlias':
    total = flower_count * DAHLIAS

    if flower_count > 90:
        discount = total * DAHLIAS_MORE_THAN_90_DISC
        total -= discount

elif flower_type == 'Tulips':
    total = flower_count * TULIPS

    if flower_count > 80:
        discount = total * TULIPS_MORE_THAN_80_DISC
        total -= discount

elif flower_type == 'Narcissus':
    total = flower_count * NARCISSUS

    if flower_count < 120:
        increase = total * NARCISSUS_LESS_THAN_120_INCRS
        total += increase

elif flower_type == 'Gladiolus':
    total = flower_count * GALDIOLUS

    if flower_count < 80:
        increase = total * GALDIOLUS_LESS_THAN_80_INCRS
        total += increase


if budget >= total:
    money_left = budget - total
    print(f'Hey, you have a great garden with {flower_count} {flower_type} and {money_left:.2f} leva left.')

else:
    money_left = total - budget
    print(f'Not enough money, you need {money_left:.2f} leva more.')
