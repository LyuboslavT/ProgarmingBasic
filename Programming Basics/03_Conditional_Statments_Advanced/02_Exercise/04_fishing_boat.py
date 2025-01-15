RENT_BOAT_SPRING = 3000
RENT_BOAT_AUTUMN_SUMMER = 4200
RENT_BOAT_WINTER = 2600

GROUP_OF_6_DISC = 0.1
GROUP_BETWEEN_7_AND_11_INCL_DISC = 0.15
GROUP_MORE_THAN_12 = 0.25
GROUP_COUNT_EVEN_DISC = 0.05

budget = int(input())
season = input()
people_count = int(input())

price = 0

# Определяме базовата цена според сезона
if season == 'Winter':
    price = RENT_BOAT_WINTER

elif season == 'Autumn' or season == 'Summer':
    price = RENT_BOAT_AUTUMN_SUMMER

elif season == 'Spring':
    price = RENT_BOAT_SPRING

# Приложение на групови отстъпки
if people_count <= 6:
    price -= price * GROUP_OF_6_DISC

elif 7 <= people_count <= 11:
    price -= price * GROUP_BETWEEN_7_AND_11_INCL_DISC

else:
    price -= price * GROUP_MORE_THAN_12

# Приложение на отстъпка за четен брой хора (без есента)
if people_count % 2 == 0 and season != 'Autumn':
    price -= price * GROUP_COUNT_EVEN_DISC

# Проверка дали бюджетът е достатъчен
if budget >= price:
    money_left = budget - price
    print(f'Yes! You have {money_left:.2f} leva left.')

else:
    money_needed = price - budget
    print(f'Not enough money! You need {money_needed:.2f} leva.')
