group_cunt = int(input())

count_musala = 0
count_monblan = 0
count_kilimanjaro = 0
count_k2 = 0
count_everest = 0

for _ in range(group_cunt):
    people_in_group = int(input())

    if 1 <= people_in_group <= 5:
        count_musala += people_in_group

    elif 6 <= people_in_group <= 12:
        count_monblan += people_in_group

    elif 13 <= people_in_group <= 25:
        count_kilimanjaro += people_in_group

    elif 26 <= people_in_group <= 40:
        count_k2 += people_in_group

    elif people_in_group > 40:
        count_everest += people_in_group

total_people = count_musala + count_monblan + count_kilimanjaro + count_k2 + count_everest

print(f'{count_musala / total_people * 100:.2f}%')
print(f'{count_monblan / total_people * 100:.2f}%')
print(f'{count_kilimanjaro / total_people * 100:.2f}%')
print(f'{count_k2 / total_people * 100:.2f}%')
print(f'{count_everest / total_people * 100:.2f}%')