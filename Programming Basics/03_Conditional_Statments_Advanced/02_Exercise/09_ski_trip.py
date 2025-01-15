ROOM_FOR_ONE_PERSON = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35

days = (int(input()) - 1)
room_type = input()
rating = input()


price = 0
discount = 0

if room_type == 'room for one person':
    price = days * ROOM_FOR_ONE_PERSON
elif room_type == 'apartment':
    if days >= 15:
        discount = APARTMENT * days * 0.5
        price = (days * APARTMENT) - discount
    elif 10 <= days <= 15:
        discount = APARTMENT * days * 0.35
        price = APARTMENT * days - discount
    elif days < 10:
        discount = APARTMENT * days * 0.3
        price = (APARTMENT * days) - discount
elif room_type == 'president apartment':
    if days >= 15:
        discount = PRESIDENT_APARTMENT * days * 0.2
        price = (days * PRESIDENT_APARTMENT) - discount
    elif 10 <= days <= 15:
        discount = PRESIDENT_APARTMENT * days * 0.15
        price = (PRESIDENT_APARTMENT * days) - discount
    elif days < 10:
        discount = PRESIDENT_APARTMENT * days * 0.1
        price = (PRESIDENT_APARTMENT * days) - discount

if rating == 'positive':
    price += price * 0.25
else:
    price -= price * 0.1

print(f'{price:.2f}')
