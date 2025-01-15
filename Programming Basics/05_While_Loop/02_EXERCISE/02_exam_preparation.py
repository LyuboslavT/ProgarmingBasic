not_successful_notes = int(input())

failed_times = 0
solved_task_counter = 0
grades_sum = 0
last_problem = ''
has_failed = True

while failed_times < not_successful_notes:
    task_name = input()

    if task_name == 'Enough':
        has_failed = False
        break

    grade = int(input())

    if grade <= 4:
        failed_times += 1

    grades_sum += grade
    solved_task_counter += 1
    last_problem = task_name

if has_failed:
    print(f'You need a break, {not_successful_notes} poor grades.')

else:
    average_grade = grades_sum / solved_task_counter
    print(f'Average score: {average_grade:.2f}\nNumber of problems: {solved_task_counter}\nLast problem: {last_problem}')
