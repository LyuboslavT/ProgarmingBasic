PUZZLE = 2.6
DOLL = 3
TEDDY_BEAR = 4.1
MINION = 8.2
TRUCK = 2
LOAN_PECENT = 0.1


price_for_holiday = float(input())
puzzle_count = int(input())
doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

toys_count = puzzle_count + doll_count + teddy_bear_count + minion_count + truck_count

toys_price_sum = puzzle_count * PUZZLE + doll_count * DOLL \
                 + teddy_bear_count * TEDDY_BEAR \
                 + minion_count * MINION \
                 + truck_count * TRUCK




if toys_count >= 50:
    toys_price_sum -= toys_price_sum * 0.25

loan = toys_price_sum * LOAN_PECENT
income = toys_price_sum - loan

if income >= price_for_holiday:
    rest = income - price_for_holiday
    print(f'Yes! {rest:.2f} lv left.')
else:
    need = price_for_holiday - income
    print(f'Not enough money! {need:.2f} lv needed.')