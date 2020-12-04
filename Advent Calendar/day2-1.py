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

df['outcome'] = '' # create an empty column in the dataframe which will be filled with the outcome (if password is good or not)
for ind in df.index:  # loop through the rows
    c = df['password'][ind].count(df['letter'][ind]) # for each row count how many times the letter appears in the password
    if c < int(df['min'][ind]) or c > int(df['max'][ind]): # check if the condition is not satisfied & update outcome column 
        df['outcome'][ind] = 'bad' 
    else:
        df['outcome'][ind] = 'good'

print(df['outcome'].value_counts()) # print how many good and bad outcomes there are

# print(df.head())