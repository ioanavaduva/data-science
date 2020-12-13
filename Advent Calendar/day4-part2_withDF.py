import pandas as pd
import re

day4 = open("input-day4.txt") # open data from .txt file

pass_info = day4.read().split('\n\n') # remove all extra empty rows

nice_pass_info = []

for line in pass_info:    
    nice_line = line.replace('\n', ' ')
    nice_pass_info.append(nice_line) # replace all \n (as characters in string) with a space

pass_list = []

for line in nice_pass_info:
    li = line.split(' ')
    pass_list.append(li) # obtain a list of lists of strings (where each string is a 'key:value' pair)

res = []
res2 = []

def list_to_dict(ent): # function to transform from list of lists of strings to list of lists of dictionaries
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
    res3.append(d1)  # res3 is a list of dictionaries, where each dictionary corresponds to a passport

# transform res3 (list of dictionaries) into dataframe and perform validation with the dataframe

df = pd.DataFrame(res3)
df = df.drop(labels = ['cid'], axis=1)  # drop cid column as not required

df = df.dropna(axis=0, how='any') # drop all rows which have at least one NaN entry
print('Number of valid passports (before validation) is ', len(df))

def check_byr(cell): # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    return len(str(cell)) == 4 and int(cell) >= 1920 and int(cell) <= 2002

def check_iyr(cell): # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    return len(cell) == 4 and int(cell) >= 2010 and int(cell) <= 2020    

def check_eyr(cell): # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    return len(cell) == 4 and int(cell) >= 2020 and int(cell) <= 2030

def check_hgt(cell): # hgt (Height) - a number followed by either cm or in: If cm, the number must be at least 150 and at most 193. If in, the number must be at least 59 and at most 76.
    if cell[-2:] == 'in' and int(cell[:-2]) >= 59 and int(cell[:-2]) <= 76:
        return True
    elif cell[-2:] == 'cm' and int(cell[:-2]) >= 150 and int(cell[:-2]) <= 193:
        return True
    else:
        return False            

def check_hcl(cell): # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    return bool(re.match(r'^#[0-9a-f]{6}', cell))

def check_ecl(cell): # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    eye_col = ['amb', 'blu', 'gry', 'grn', 'hzl', 'oth', 'brn']
    return cell in eye_col

def check_pid(cell): # pid (Passport ID) - a nine-digit number, including leading zeroes.
    return bool(re.match(r'[0-9]{9}', cell)) and len(cell) == 9

df['outcome'] = '' # create new column and add 'yes' if all conditions are satisfied; otherwise add 'no'.
for ind in df.index:
    if check_byr(df['byr'][ind]) and check_iyr(df['iyr'][ind]) and check_eyr(df['eyr'][ind]) and check_hgt(df['hgt'][ind]) and check_hcl(df['hcl'][ind]) and check_ecl(df['ecl'][ind]) and check_pid(df['pid'][ind]):
        df['outcome'][ind] = 'yes'
    else:
        df['outcome'][ind] = 'no'

# print(df.head(250))
print(df['outcome'].value_counts())
