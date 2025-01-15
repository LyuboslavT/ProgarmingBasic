city = str(input())
sales_volume = float(input())
interest = 0
error_condition = False

if city == "Sofia":
    if 0 <= sales_volume <= 500:
        interest = sales_volume * 0.05
    elif 500 <= sales_volume <= 1000:
        interest = sales_volume * 0.07
    elif 1000 <= sales_volume <= 10000:
        interest = sales_volume * 0.08
    elif sales_volume > 10000:
        interest = sales_volume * 0.12
    else:
        error_condition = True
elif city == 'Varna':
    if 0 <= sales_volume <= 500:
        interest = sales_volume * 0.045
    elif 500 <= sales_volume <= 1000:
        interest = sales_volume * 0.075
    elif 1000 <= sales_volume <= 10000:
        interest = sales_volume * 0.1
    elif sales_volume > 10000:
        interest = sales_volume * 0.13
    else:
        error_condition = True
elif city == 'Plovdiv':
    if 0 <= sales_volume <= 500:
        interest = sales_volume * 0.055
    elif 500 <= sales_volume <= 1000:
        interest = sales_volume * 0.08
    elif 1000 <= sales_volume <= 10000:
        interest = sales_volume * 0.12
    elif sales_volume > 10000:
        interest = sales_volume * 0.145
    else:
        error_condition = True
else:
    error_condition = True

if error_condition:
    print('error')
else:
    print(f'{interest:.2f}')



