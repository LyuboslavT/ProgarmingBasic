# · Брой пилешки менюта – цяло число в интервала [0 … 99]
#
# · Брой менюта с риба – цяло число в интервала [0 … 99]
#
# · Брой вегетариански менюта – цяло число в интервала [0 … 99]
import math
chicken_count = int(input())
fish_count = int(input())
vegan_count = int(input())
delivery = 2.50


# • Пилешко меню – 10.35 лв.
#
# • Меню с риба – 12.40 лв.
#
# • Вегетарианско меню – 8.15 лв.

sub_sum = chicken_count * 10.35 + fish_count * 12.40 + vegan_count * 8.15

dessert = sub_sum * 0.2

total_sum = (sub_sum + dessert + delivery)



# Да се отпечата на конзолата един ред: "{цена на поръчката}"

print(f'{round(total_sum, 2)}')
