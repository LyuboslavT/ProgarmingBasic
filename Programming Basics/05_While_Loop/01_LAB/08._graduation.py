student_name = input()

total_grade = 0
counter = 0
failed_years = 0


while counter < 12:
    grade = float(input())

    if grade < 4:
        failed_years += 1

        if failed_years > 1:
            failed_years = counter + 1
            print(f'{student_name} has been excluded at {failed_years} grade')
            break

        continue

    counter += 1
    total_grade += grade

else:
    average_grade = total_grade / counter
    print(f'{student_name} graduated. Average grade: {average_grade:.2f}')