import pandas as pd
import re

pd.set_option('display.max_colwidth', None)

df = pd.read_csv('jeopardy.csv')

# examine the dataframe
print(df.head())
# rename the columns so they're easier to access
df.rename(columns = {'Show Number': 'show_number', ' Air Date': 'air_date', ' Round': 'round', ' Category':'category', ' Value':'value', ' Question':'question', ' Answer':'answer'}, inplace=True)

# get column names to check they've changed
print(df.columns)

# Write a function that filters the dataset for questions that contains all of
# the words in a list of words. For example, when the list ["King", "England"]
# was passed to our function, the function returned a DataFrame of 152 rows.
# Every row had the strings "King" and "England" somewhere in its " Question".

def list_words(data, words):
  filter = lambda x: all(word.lower() in x.lower() for word in words)
  return data.loc[data['question'].apply(filter)]

new_df = list_words(df, ['King', 'England'])
# print(new_df['question'])

# We may want to eventually compute aggregate statistics, like .mean() on the "
# Value" column. But right now, the values in that column are strings. Convert
# the " Value" column to floats. If you’d like to, you can create a new column
# with the float values.

df['value'] = df['value'].str.replace(r'$', '', regex=True)
df['value'] = df['value'].str.replace(r',', '')

df['value_float'] = df.value.apply(lambda x: float(x) if x!='None' else 0.0)

# print(df['value_float'].head())


# Now that you can filter the dataset of question, use your new column that
# contains the float values of each question to find the “difficulty” of certain
# topics. For example, what is the average value of questions that contain the
# word "King"?

print('Overall mean value is: ' + str(df['value_float'].mean()))

df_filter = list_words(df, ['King'])
print('Mean value of questions that contain King: ' + str(df_filter.value_float.mean()))

# Write a function that returns the count of the unique answers to all of the
# questions in a dataset. For example, after filtering the entire dataset to
# only questions containing the word "King", we could then find all of the
# unique answers to those questions. The answer “Henry VIII” appeared 3 times
# and was the most common answer.

def count_unique(data, words):
  filtered = list_words(data, words)
  return filtered['answer'].value_counts()
  # unique = filtered.groupby('answer').value.count().reset_index()
  # return unique.sort_values(by=['value'], ascending=False)

# Tests the unique answer formula 
df_unique = count_unique(df, ['King'])
print(df_unique.head())