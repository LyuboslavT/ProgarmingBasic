# Входни данни
weight = float(input())
service_type = input()
distance = int(input())

# Цена на километър според теглото
if weight < 1:
    price_per_km = 0.03
elif weight < 10:
    price_per_km = 0.05
elif weight < 40:
    price_per_km = 0.10
elif weight < 90:
    price_per_km = 0.15
else:
    price_per_km = 0.20

# Базова цена
base_cost = distance * price_per_km

# Допълнителна надценка за express услуга
if service_type == "express":
    if weight < 1:
        markup_rate = 0.8
    elif weight < 10:
        markup_rate = 0.4
    elif weight < 40:
        markup_rate = 0.05
    elif weight < 90:
        markup_rate = 0.02
    else:
        markup_rate = 0.01

    # Изчисляване на надценката
    additional_cost_per_km = weight * price_per_km * markup_rate
    additional_cost = distance * additional_cost_per_km
else:
    additional_cost = 0

# Обща цена
total_cost = base_cost + additional_cost

# Изход
print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total_cost:.2f} lv.")
