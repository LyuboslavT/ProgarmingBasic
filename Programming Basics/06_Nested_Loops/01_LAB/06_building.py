floors = int(input())
rooms = int(input())

floor_counter = 1
room_type = ''


for i in range(floors, 0, -1):

    for j in range(0, rooms):

        if i == floors:
            room_type = 'L'

        elif i % 2 == 0:
            room_type = 'O'

        else:
            room_type = 'A'

        print(f'{room_type}{i}{j}', end= ' ')

    print()