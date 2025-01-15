degrees = int(input())
time_of_day = input()

shoes = ''
outfit = ''

if time_of_day == 'Morning':

    if 10 <= degrees <= 18:
        shoes = 'Sneakers'
        outfit = 'Sweatshirt'

    elif 18 <= degrees <= 24:
        shoes = 'Moccasins'
        outfit = 'Shirt'

    elif degrees >= 25:
        shoes = 'Sandals'
        outfit = 'T-Shirt'

elif time_of_day == 'Afternoon':

    if 10 <= degrees <= 18:
        shoes = 'Moccasins'
        outfit = 'Shirt'

    elif 18 <= degrees <= 24:
        shoes = 'Sandals'
        outfit = 'T-Shirt'

    elif degrees >= 25:
        shoes = 'Barefoot'
        outfit = 'Swim Suit'

elif time_of_day == 'Evening':

    if 10 <= degrees <= 18:
        shoes = 'Moccasins'
        outfit = 'Shirt'

    elif 18 <= degrees <= 24:
        shoes = 'Moccasins'
        outfit = 'Shirt'

    elif degrees >= 25:
        shoes = 'Moccasins'
        outfit = 'Shirt'

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")