# 1. Брой страници в текущата книга – цяло число в интервала [1…1000]
#
# 2. Страници, които прочита за 1 час – цяло число в интервала [1…1000]
#
# 3. Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]

book_pages = int(input())
pages_per_h = int(input())
day_count = int(input())

h_count = book_pages // pages_per_h
h_per_day = h_count // day_count

print(h_per_day)



