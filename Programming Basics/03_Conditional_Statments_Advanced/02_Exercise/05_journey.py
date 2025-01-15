PRICE_SUMMER_BULGARIA_PERC = 0.3
PRICE_WINTER_BULGARIA_PERC = 0.7

PRICE_SUMMER_BALKANS_PERC = 0.4
PRICE_WINTER_BALKANS_PERC = 0.8

PRICE_SUMMER_EUROPE_PERC = 0.9
PRICE_WINTER_EUROPE_PERC = 0.9

budget = float(input())
season = input()

money_spent = 0
destination = ''
stay = ''

#seaseon summer
if season == 'summer':
    #price for Bulgaria
    if budget <= 100:
        money_spent = budget * PRICE_SUMMER_BULGARIA_PERC
        destination = 'Bulgaria'
        stay = 'Camp'
    # Price for BALKANS
    elif budget <= 1000:
        money_spent = budget * PRICE_SUMMER_BALKANS_PERC
        destination = 'Balkans'
        stay = 'Camp'
    #Price for Europe
    else:
        money_spent = budget * PRICE_SUMMER_EUROPE_PERC
        destination = 'Europe'
        stay = 'Hotel'

#season winter
elif season == 'winter':
    #price for Bulgaria
    if budget <= 100:
        money_spent = budget * PRICE_WINTER_BULGARIA_PERC
        destination = 'Bulgaria'
        stay = 'Hotel'
    #price for BALKANS
    elif budget <= 1000:
        money_spent = budget * PRICE_WINTER_BALKANS_PERC
        destination = 'Balkans'
        stay = 'Hotel'
    #price for Europe
    else:
        money_spent = budget * PRICE_WINTER_EUROPE_PERC
        destination = 'Europe'
        stay = 'Hotel'



print(f'Somewhere in {destination}')
print(f'{stay} - {money_spent:.2f}')