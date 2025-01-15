trip_needed_money = float(input())
current_amount_money = float(input())

number_days = 0
number_spending_days = 0
result = ''

while number_spending_days < 5:
    command = input()
    money = float(input())
    number_days += 1

    if command == 'spend':
        number_spending_days += 1
        current_amount_money = current_amount_money - money if current_amount_money > money else 0

    elif command == 'save':
        number_spending_days = 0
        current_amount_money += money

        if current_amount_money >= trip_needed_money:
            result = f'You saved the money for {number_days} days.'
            break

else:
    result = f"You can't save the money.\n{number_days}"

print(result)