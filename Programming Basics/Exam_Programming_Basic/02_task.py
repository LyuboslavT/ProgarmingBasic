# Входни данни
daily_allowance = float(input())  # Джобните на Тереза на ден
daily_income = float(input())    # Печалбата от продажби на ден
total_expenses = float(input())  # Разходите за целия период
gift_price = float(input())      # Цената на подаръка

# Броят на дните
days = 5

# Изчисляване на общите спестени пари
savings_from_allowance = daily_allowance * days
earnings_from_sales = daily_income * days
total_savings = savings_from_allowance + earnings_from_sales - total_expenses

# Проверка дали парите са достатъчни
if total_savings >= gift_price:
    print(f"Profit: {total_savings:.2f} BGN, the gift has been purchased.")
else:
    deficit = gift_price - total_savings
    print(f"Insufficient money: {deficit:.2f} BGN.")
