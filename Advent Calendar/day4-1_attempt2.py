# Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?

import pandas as pd
day4 = open("input-day4.txt") # open data from .txt file

pass_info = day4.read().split('\n\n')

nice_pass_info = []

for line in pass_info:    
    nice_line = line.replace('\n', ' ')
    nice_pass_info.append(nice_line)

pass_list = []

for line in nice_pass_info:
    li = line.split(' ')
    pass_list.append(li)

res = []
res2 = []

def list_to_dict(ent): # function to transform from list of strings to list of dictionaries
    d = {}
    i = entries.split(':')
    d[i[0]] = i[1]
    res.append(d)
    return res

for line in pass_list:
    res = []
    for entries in line:
        list_to_dict(entries)
    res2.append(res) # res2 is a list of lists of dictionaries where each inner list corresponds to a passport

res3 = []

for li in res2:
    d1 = {}
    for i in li:
        d1.update(i)
    res3.append(d1)      
# res3 is a list of dictionaries, where each dictionary corresponds to a passport

pref_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def validate_line(line, prefs):
    for key in prefs:
        if any(key in s for s in line):
            continue
        else:
            return False
    return True

res4 = []

for line in res3:
    if validate_line(line, pref_list):
        res4.append('yes')
    else:
        res4.append('no')

print(res4.count('yes')) # res4 contains yes and no for passports that are valid or not based on the given criteria (that they have all required fields)

# transform res3 (list of dictionaries) into dataframe

df = pd.DataFrame(res3)

print(df.head())

