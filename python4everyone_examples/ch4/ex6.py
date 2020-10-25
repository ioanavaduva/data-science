# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate)

hrs = input('Enter Hours:')
rt = input('Enter rate:')

def computepay(hours, rate):
    pay_extra = 0
    if float(hours) > 40:
        rt_extra = 0.5*float(rate) # only want 0.5 because we add it on to the other pay
        extra = float(hours) - 40
        pay_extra = extra*rt_extra
    xp = float(hours)*float(rate) + pay_extra
    return xp
    

pay = computepay(hrs, rt)
print('Pay:', pay)