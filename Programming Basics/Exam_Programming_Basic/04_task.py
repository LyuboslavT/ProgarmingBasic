# stundets_count = int(input())
#
# counter_5 = 0
# counter_4_5 = 0
# counter_3_4 = 0
# counter_2_3 = 0
#
# for _ in range(2, 7):
#     stident_grade = float(input())
#
#     if grade >= 5.00:
#         counter_5 += 1
#

# Вход
n = int(input())
grades = [float(input()) for _ in range(n)]

# Инициализиране на броячите за различните групи
top_students = 0
between_4_and_4_99 = 0
between_3_and_3_99 = 0
fail = 0
total_sum = 0

# Обработка на оценките
for grade in grades:
    total_sum += grade
    if grade >= 5.00:
        top_students += 1
    elif 4.00 <= grade <= 4.99:
        between_4_and_4_99 += 1
    elif 3.00 <= grade <= 3.99:
        between_3_and_3_99 += 1
    else:
        fail += 1

# Пресмятане на процентите
top_students_percentage = (top_students / n) * 100
between_4_and_4_99_percentage = (between_4_and_4_99 / n) * 100
between_3_and_3_99_percentage = (between_3_and_3_99 / n) * 100
fail_percentage = (fail / n) * 100

# Пресмятане на средния успех
average_grade = total_sum / n

# Изход
print(f"Top students: {top_students_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {between_4_and_4_99_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {between_3_and_3_99_percentage:.2f}%")
print(f"Fail: {fail_percentage:.2f}%")
print(f"Average: {average_grade:.2f}")
