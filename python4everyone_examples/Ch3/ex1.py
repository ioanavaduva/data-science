# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours. 

hrs = input('Enter Hours:')
rt = input('Enter rate:')
pay_extra = 0
if float(hrs) > 40:
    rt_extra = 0.5*float(rt) # only want 0.5 because we add it on to the other pay
    extra = float(hrs) - 40
    pay_extra = extra*rt_extra
pay = float(hrs)*float(rt) + pay_extra
print('Pay:', pay)