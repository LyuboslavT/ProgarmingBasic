# MAY_OCTOBER_STUDIO_PRICE = 50
# MAY_OCTOBER_APT_PRICE = 65
#
# JUNE_SEPTEMBER_STUDIO_PRICE = 75.20
# JUNE_SEPTEMBER_APT_PRICE = 68.70
#
# JULY_AUGUST_STUDIO_PRICE = 76
# JULY_AUGUST_APT_PRICE = 77
#
# STUDIO_MAY_OCTOBER_DISC_7 = 0.05
# STUDIO_MAY_OCTOBER_DISC_14 = 0.3
# STUDIO_JUNE_SEPTEMBER_DISC_14 = 0.2
# APT_DISC = 0.1
#
# month = input()
# overnight_stay_count = int(input())
# price = 0
# discount = 0
# money_spent_studio = 0
# money_spent_apt = 0
#
# room_type = ''
#
#
# if month == 'May' or month == 'October':
#
#     if 7 > overnight_stay_count < 14 and (month == 'May' or month == 'October'):
#         price = overnight_stay_count * MAY_OCTOBER_STUDIO_PRICE
#         discount = price * STUDIO_MAY_OCTOBER_DISC_7
#         money_spent_studio = price - discount
#
#     elif overnight_stay_count > 14 and (month == 'May' or month == 'October'):
#         price = overnight_stay_count * MAY_OCTOBER_STUDIO_PRICE
#         discount = price * STUDIO_MAY_OCTOBER_DISC_14
#         money_spent_studio = price - discount
#
#     if overnight_stay_count < 14 and (month == 'May' or month == 'October'):
#         money_spent_apt = overnight_stay_count * MAY_OCTOBER_APT_PRICE
#
#     elif overnight_stay_count > 14 and (month == 'May' or month == 'October'):
#         price = overnight_stay_count * MAY_OCTOBER_APT_PRICE
#         discount = price * APT_DISC
#         money_spent_apt = price - discount
#
#
# if month == 'June' or month == 'September':
#
#     if overnight_stay_count < 14 and (month == 'June' or month == 'September'):
#         money_spent_studio = overnight_stay_count * JUNE_SEPTEMBER_STUDIO_PRICE
#
#     elif overnight_stay_count >= 14 and (month == 'June' or month == 'September'):
#         price = overnight_stay_count * JUNE_SEPTEMBER_STUDIO_PRICE
#         discount = price * STUDIO_JUNE_SEPTEMBER_DISC_14
#         money_spent_studio = price - discount
#
#     if overnight_stay_count < 14 and (month == 'June' or month == 'September'):
#         money_spent_apt = overnight_stay_count * JUNE_SEPTEMBER_APT_PRICE
#
#     elif overnight_stay_count >= 14 and (month == 'June' or month == 'September'):
#         price = overnight_stay_count * JUNE_SEPTEMBER_APT_PRICE
#         discount = price * APT_DISC
#         money_spent_apt = price - discount
#
#
# if month == 'July' or month == 'August':
#     money_spent_studio = overnight_stay_count * JULY_AUGUST_STUDIO_PRICE
#
#     if overnight_stay_count < 14 and (month == 'July' or month == 'August'):
#         money_spent_apt = overnight_stay_count * JULY_AUGUST_APT_PRICE
#
#     elif overnight_stay_count > 14 and (month == 'July' or month == 'August'):
#         price = overnight_stay_count * JULY_AUGUST_APT_PRICE
#         discount = price * APT_DISC
#         money_spent_apt = price - discount
#
#
# print(f'Apartment: {money_spent_apt:.2f} lv.')
# print(f'Studio: {money_spent_studio:.2f} lv.')

# constants
# basis prices
MAY_OCTOBER_STUDIO = 50
MAY_OCTOBER_APT = 65

JUNE_SEPT_STUDIO = 75.2
JUNE_SEPT_APT = 68.7

JULY_AUGUST_STUDIO = 76
JULY_AUGUST_APT = 77

# discounts studio
MAY_OCTOBER_STUDIO_MORE_THAN_7 = 0.05
MAY_OCTOBER_STUDIO_MORE_THAN_14 = 0.3
JUNE_SEPT_STUDIO_MORE_THAN_14 = 0.2

# discounts apt
APT_DISCOUNT_MORE_THAN_14 = 0.1

# define user input variables
month = input()
nights_count = int(input())

price_studio = 0
price_apt = 0
discount = 0
money_spent_for_studio = 0
money_spent_for_apt = 0

# May and October logic
if month == 'May' or month == 'October':
    price_studio = MAY_OCTOBER_STUDIO * nights_count
    price_apt = MAY_OCTOBER_APT * nights_count

    # Studio discounts for May/October
    if 7 < nights_count <= 14:
        discount = price_studio * MAY_OCTOBER_STUDIO_MORE_THAN_7
    elif 1 < nights_count > 14:
        discount = price_studio * MAY_OCTOBER_STUDIO_MORE_THAN_14

    money_spent_for_studio = price_studio - discount

    # Apartment discount for May/October
    if 1 < nights_count > 14:
        discount = price_apt * APT_DISCOUNT_MORE_THAN_14
    money_spent_for_apt = price_apt - discount

# June and September logic
if month == 'June' or month == 'September':
    price_studio = JUNE_SEPT_STUDIO * nights_count
    price_apt = JUNE_SEPT_APT * nights_count

    # Studio discount for June/September
    if 1 < nights_count > 14:
        discount = price_studio * JUNE_SEPT_STUDIO_MORE_THAN_14
    money_spent_for_studio = price_studio - discount

    # Apartment discount for June/September
    discount_apt = 0  # separate discount for apartment
    if 1 < nights_count > 14:
        discount_apt = price_apt * APT_DISCOUNT_MORE_THAN_14
    money_spent_for_apt = price_apt - discount_apt

# July and August logic
if month == 'July' or month == 'August':
    price_studio = JULY_AUGUST_STUDIO * nights_count
    price_apt = JULY_AUGUST_APT * nights_count

    # Apartment discount for July/August
    discount = 0  # no discount for studio in July/August
    if 1 < nights_count > 14:
        discount = price_apt * APT_DISCOUNT_MORE_THAN_14
    money_spent_for_apt = price_apt - discount
    money_spent_for_studio = price_studio

# Output the final amounts
print(f'Apartment: {money_spent_for_apt:.2f} lv.\nStudio: {money_spent_for_studio:.2f} lv.')
