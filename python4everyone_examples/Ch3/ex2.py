# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.

hrs = input('Enter Hours:')
rt = input('Enter rate:')
pay_extra = 0
try: 
    if float(hrs) > 40:
        rt_extra = 0.5*float(rt) # only want 0.5 because we add it on to the other pay
        extra = float(hrs) - 40
        pay_extra = extra*rt_extra
    pay = float(hrs)*float(rt) + pay_extra
    print('Pay:', pay)
except:
    print('Error, please enter numeric input')
