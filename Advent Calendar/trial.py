import pandas as pd
df = pd.DataFrame({'num1': ['2', 3, 4, 6], 'num2': ['4', 5, 6, 7]})

df['difference'] = df['num1']+df['num2']
print(df)