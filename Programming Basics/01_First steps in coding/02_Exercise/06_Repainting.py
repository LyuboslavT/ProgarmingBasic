# 1. Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
#
# 2. Необходимо количество боя (в литри) - цяло число в интервала [1…100]
#
# 3. Количество разредител (в литри) - цяло число в интервала [1…30]
#
# 4. Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]

naylon = int(input())
paint = int(input())
razreditel = int(input())
hours = int(input())
bags = 0.40

# · Предпазен найлон - 1.50 лв. за кв. метър
#
# · Боя - 14.50 лв. за литър
#
# · Разредител за боя - 5.00 лв. за литър

naylon_bonus = (naylon + 2) * 1.50
paint_bonus = (paint + paint * 0.1) * 14.50
razreditel_sum = razreditel * 5.00

products_total = naylon_bonus + paint_bonus + bags + razreditel_sum

worker_salary = products_total * 0.3 * hours

total_sum = products_total + worker_salary


# Да се отпечата на конзолата един ред:

# · "{сумата на всички разходи}"

print(f'{total_sum}')
