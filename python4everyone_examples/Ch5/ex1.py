# Write a program which repeatedly reads numbers until the user enters 'done'.
# Once 'done' is entered, print out the total, count, and average of the
# numbers. If the user enters anything other than a number, detect their mistake
# using try and except and print an error message and skip tot the next number.

it = 0
tot = 0

inp = None
while inp != 'done':
    inp = input('Enter a number:')  
    try:
        inp_val = float(inp)
        tot = tot + inp_val
        it = it + 1
    except:
        print('Invalid input')
avg = tot/it   
print(tot, it, avg)
