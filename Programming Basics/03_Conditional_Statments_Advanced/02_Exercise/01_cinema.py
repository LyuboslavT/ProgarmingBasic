PREMIERE = 12
NORMAL = 7.50
DISCOUNT = 5.00

movie_type = input()
rows = int(input())
columns = int(input())

capacity = rows * columns
sum_total = 0

if movie_type == 'Premiere':
    sum_total = capacity * PREMIERE

elif movie_type == 'Normal':
    sum_total = capacity * NORMAL

elif movie_type == 'Discount':
    sum_total = capacity * DISCOUNT

print(f'{sum_total:.2f} leva')