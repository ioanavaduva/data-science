# For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

from collections import Counter

day6 = open('input-day6.txt')

group_info = day6.read().split('\n\n') # remove all extra empty rows

nice_group_info = []

for line in group_info:    
    nice_line = line.replace('\n', '')
    nice_group_info.append(nice_line) # every element of the list is a string corresponding to each group

nice_group_info2 = []

for line in group_info:    
    nice_line2 = line.replace('\n', ' ')
    nice_group_info2.append(nice_line2) # replace \n with a space to separate between the answers of individuals in a group


lol_string = [] 

for string in nice_group_info2:
    indiv_string = string.split(' ')
    lol_string.append(indiv_string) # (lol =) list of lists of strings; each string corresponds to the answers of a member in a group

group_numbers = [] 

for string in lol_string:
    group_numbers.append(len(string)) # vector with how many members are in each group
counts_vec = []

def list_to_dict(ent): # function to transform from list of lists of strings to list of lists of dictionaries
    d = {}
    d = dict(ent)
    return d

list_dict = []

for line in nice_group_info:
    cnt = Counter(line) # for each group, cnt stores a dict with how many members of the group answered a question with yes
    list_dict.append(list_to_dict(cnt)) # get a list on dictionaries where each dictionary contains how many people in the group responded with yes to each question

res = [] 

for i in range(len(list_dict)): # counter to access elements of two different lists (group_numbers and list_dict)

    j = 0

    for key, value in list_dict[i].items(): # need the values from the dictonary to equal the number of people in a group 
        
        if value == group_numbers[i]: # compare if all members (access how many with group_numbers[i]) of the group responded to the same questions (by comparing the value corresponding to each key(each key is a letter for one group))
            j = j+1 # add 1 for each question answered with yes by each member
        else:
            continue

    res.append(j) # each entry of res will be equal to the number of questions all people in the group answered with 'yes'

print('Sum of number of questions to which everyone (from each group) answered yes is ', str(sum(res)))