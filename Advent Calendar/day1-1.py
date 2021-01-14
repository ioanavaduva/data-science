# Find the two/three (for second challenge) entries that sum to 2020 and then multiply those two/three numbers together.
data = open('input-day1.txt')

d = list(data)
print(d[0])

for num in d:
    for num2 in d:
        for num3 in d:
            if int(num) + int(num2) + int(num3) == 2020:
                print('The product of the three numbers that add to 2020 is: ' + str(int(num)*int(num2)*int(num3)))
                break
            else:
                continue
            break
   

