count = int(input())
washing_machine_price = float(input())
price_toys = int(input())

money_present_even_birthday = 10
stealing = 0
sum_money = 0
total_money = 0
toy_count = 0
toy_savings = 0


for i in range(1, count + 1):

    if i % 2 == 0:
        sum_money += money_present_even_birthday
        money_present_even_birthday += 10
        stealing += 1

    else:
        toy_count += 1
        toy_savings = toy_count * price_toys

    total_money = sum_money + toy_savings - stealing

if total_money >= washing_machine_price:
    money_left = total_money - washing_machine_price
    print(f'Yes! {money_left:.2f}')

else:
    money_need = washing_machine_price - total_money
    print(f'No! {money_need:.2f}')