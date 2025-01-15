day = str(input())
#Monday	Tuesday	Wednesday	Thursday	Friday	Saturday	Sunday
#12	        12	    14	        14	        12	    16	      16

ticket_12 = ['Monday', 'Tuesday', 'Friday']
ticket_14 = ['Wednesday', 'Thursday']
ticket_16 = ['Saturday', 'Sunday']

if day in ticket_12:
    print('12')
elif day in ticket_14:
    print('14')
elif day in ticket_16:
    print('16')
    