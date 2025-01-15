fat_percentage = int(input())
protein_percentage = int(input())
carbs_percentage = int(input())
total_calories = int(input())
water_percentage = int(input())

# Изчисляване на грамовете за всеки макроелемент
fat_grams = (fat_percentage / 100) * total_calories / 9
protein_grams = (protein_percentage / 100) * total_calories / 4
carbs_grams = (carbs_percentage / 100) * total_calories / 4

# Общо тегло на храната (без вода)
total_food_weight = fat_grams + protein_grams + carbs_grams

# Тегло на храната след изваждане на водата
food_weight_without_water = total_food_weight * (1 - water_percentage / 100)

# Калории на грам храна
calories_per_gram = total_calories / food_weight_without_water

# Изход
print(f"{calories_per_gram:.4f}")