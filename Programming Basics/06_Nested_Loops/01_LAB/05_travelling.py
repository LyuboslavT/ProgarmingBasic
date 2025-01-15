while True:
    destination = input()
    if destination == 'End':
        break

    minimum_budget = float(input())
    sum_savings = 0

    while sum_savings < minimum_budget:
        savings = float(input())
        sum_savings += savings

    print(f'Going to {destination}!')
