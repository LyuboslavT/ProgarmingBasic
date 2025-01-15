DECOR_PERCENT = 0.1
DISCOUNT_MORE_150_STATIST = 0.1

budget = float(input())
statist_count = int(input())
price_for_one_sute = float(input())

decor = budget * DECOR_PERCENT

suite_for_all_statist = statist_count * price_for_one_sute

if statist_count > 150:
    suite_for_all_statist -= suite_for_all_statist * DISCOUNT_MORE_150_STATIST

total_sum = decor + suite_for_all_statist

if total_sum > budget:
    need = total_sum - budget
    print(f'Not enough money!')
    print(f'Wingard needs {need:.2f} leva more.')
else:
    rest = budget - total_sum
    print(f'Action!')
    print(f'Wingard starts filming with {rest:.2f} leva left.')