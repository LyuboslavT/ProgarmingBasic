# 1. Депозирана сума – реално число в интервала [100.00 … 10000.00]
#
# 2. Срок на депозита (в месеци) – цяло число в интервала [1…12]
#
# 3. Годишен лихвен процент – реално число в интервала [0.00 …100.00]
import math

depositAmount = float(input())
duration = int(input())
GPR = float(input()) / 100


# 1. Изчисляваме натрупаната лихва: 200 * 0.057 (5.7%) = 11.40 лв.
# 2. Изчисляваме лихвата за 1 месец: 11.40 лв. / 12 месеца = 0.95 лв.
# 3. Общата сума е: 200 лв. + 3 * 0.95 лв. = 202.85 лв.

interest = depositAmount * GPR
interestOneMonth = interest / 12
total_amount = depositAmount + duration * interestOneMonth

print(total_amount)

