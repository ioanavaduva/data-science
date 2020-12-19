# For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?

from collections import Counter

day6 = open('input-day6.txt')

group_info = day6.read().split('\n\n') # remove all extra empty rows

nice_group_info = []

for line in group_info:    
    nice_line = line.replace('\n', '')
    nice_group_info.append(nice_line) # every element of the list is a string corresponding to each group
counts_vec = []

for line in nice_group_info:
    cnt = Counter(line) # for each group, cnt stores a dict with how many members of the group answered a question with yes
    counts_vec.append(len(cnt)) # counts_vec contains a vector where each entry represents how many questions were answered altogether with yes by a group

print('Sum of number of questions to which anyone answered yes is ', str(sum(counts_vec)))

