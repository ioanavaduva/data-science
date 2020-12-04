# How many passwords are valid according to their policies?

import pandas as pd 

web = open("input-day2.txt") # open data from .txt file

df = pd.DataFrame(web, columns=['init']) # transform web data to dataframe

mima = df['init'].str.split().str[0] # create new column with data before first space
letter = df['init'].str.split().str[1].str.rstrip(':') # create new column with data between first and second spaces
password = df["init"].str.split().str[2] # create new column with data between second and third spaces
df['minmax'] = mima # make a column with min-max values
df[['min', 'max']] = df.minmax.str.split('-', expand = True,) # make two separate columns, one for min, one for max values by splitting min-max column
df['letter'] = letter # make column for letter
df['password'] = password # make column for password
df = df.drop(labels = ['init', 'minmax'], axis=1) # drop first two columns as they are not needed and include too much information

# create empty columns in the dataframe which will be filled with yes/no if the letter is in position min/max and good/bad in the outcome (if password is good or not)
df['pos-min'] = ''
df['pos-max'] = ''
df['outcome'] = '' 
for ind in df.index:  # loop through the rows
    if df['password'][ind][int(df['min'][ind])-1] == df['letter'][ind]: # check if the letter is in position min
        df['pos-min'][ind] = 'yes'
    else:
        df['pos-min'][ind] = 'no'
    if df['password'][ind][int(df['max'][ind])-1] == df['letter'][ind]: # check if the letter is in position max
        df['pos-max'][ind] = 'yes'
    else:
        df['pos-max'][ind] = 'no'
    if (df['pos-min'][ind] == 'yes' and df['pos-max'][ind] == 'yes') or (df['pos-min'][ind] == 'no' and df['pos-max'][ind] == 'no'): # check if the condition is not satisfied & update outcome column
        df['outcome'][ind] = 'bad'
    else:
        df['outcome'][ind] = 'good'

print(df['outcome'].value_counts()) # print how many good and bad outcomes there are

# print(df.head())