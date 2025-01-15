book = input()
counter = 0
current_book = ''

while current_book != 'No More Books':
    current_book = input()

    if current_book == book:
        print(f'You checked {counter} books and found it.')
        break

    counter += 1

else:
    counter -= 1
    print(f'The book you search is not here!\nYou checked {counter} books.')
