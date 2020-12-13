# Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

day4 = open("input-day4.txt") # open data from .txt file

pass_info = day4.read().split('\n\n')

# pass_info = pass_info[0]
nice_pass_info = []

for line in pass_info:    
    nice_line = line.replace('\n', ' ')
    nice_pass_info.append(nice_line)

pass_list = []

for line in nice_pass_info:
    li = line.split(' ')
    pass_list.append(li)

# print(pass_list[:5])

pref_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
res = []

def validate_line(line, prefs):
    for word in prefs:
        if any(word in s for s in line):
            continue
        else:
            return False
    return True


for line in pass_list:
    if validate_line(line, pref_list):
        res.append('yes')
    else:
        res.append('no')

print(res.count('yes'))


