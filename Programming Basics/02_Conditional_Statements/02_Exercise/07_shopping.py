GPU = 250
CPU = 0.35
RAM = 0.1
DISCOUNT = 0.15

budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

gpu_price = gpu_count * GPU
cpu_price = cpu_count * (gpu_price * CPU)
ram_price = ram_count * (gpu_price * RAM)

total_sum = gpu_price + cpu_price + ram_price

if gpu_count > cpu_count:
    total_sum -= total_sum * DISCOUNT

if budget >= total_sum:
    rest = budget - total_sum
    print(f'You have {rest:.2f} leva left!')
else:
    need = total_sum - budget
    print(f'Not enough money! You need {need:.2f} leva more!')