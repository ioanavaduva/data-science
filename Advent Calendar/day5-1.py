# What is the highest seat ID on a boarding pass?
import pandas as pd

web = open('input-day5.txt')

list_strings = web.read().split('\n')

vec = list(range(128))
col_num = list(range(8))

def get_row(code):
    vec = list(range(128))
    if code[0] == 'F':
        new_vec1 = vec[:int(len(vec)/2)]
    else:
        new_vec1 = vec[int(len(vec)/2):]
    
    if code[1] == 'F':
        new_vec2 = new_vec1[:int(len(new_vec1)/2)]
    else:
        new_vec2 = new_vec1[int(len(new_vec1)/2):]
    
    if code[2] == 'F':
        new_vec3 = new_vec2[:int(len(new_vec2)/2)]
    else:
        new_vec3 = new_vec2[int(len(new_vec2)/2):]

    if code[3] == 'F':
        new_vec4 = new_vec3[:int(len(new_vec3)/2)]
    else:
        new_vec4 = new_vec3[int(len(new_vec3)/2):]

    if code[4] == 'F':
        new_vec5 = new_vec4[:int(len(new_vec4)/2)]
    else:
        new_vec5 = new_vec4[int(len(new_vec4)/2):]

    if code[5] == 'F':
        new_vec6 = new_vec5[:int(len(new_vec5)/2)]
    else:
        new_vec6 = new_vec5[int(len(new_vec5)/2):]

    if code[6] == 'F':
        new_vec7 = new_vec6[:int(len(new_vec6)/2)]
    else:
        new_vec7 = new_vec6[int(len(new_vec6)/2):]
    
    return new_vec7[0]

def get_column(code):
    if code[7] == 'L':
        new_col_num1 = col_num[:int(len(col_num)/2)]
    else:
        new_col_num1 = col_num[int(len(col_num)/2):]

    if code[8] == 'L':
        new_col_num2 = new_col_num1[:int(len(new_col_num1)/2)]
    else:
        new_col_num2 = new_col_num1[int(len(new_col_num1)/2):]

    if code[9] == 'L':
        new_col_num3 = new_col_num2[:int(len(new_col_num2)/2)]
    else:
        new_col_num3 = new_col_num2[int(len(new_col_num2)/2):]

    return new_col_num3[0]

# print('Row', get_row('FBFBBFFRLR'))
# print('Column', get_column('FBFBBFFRLR'))
# print('id', get_row('FBFBBFFRLR')*8 + get_column('FBFBBFFRLR'))

id_list = []
rows = []
columns = []  

for element in list_strings:
    rows.append(get_row(element))
    columns.append(get_column(element))
    id_list.append(get_row(element)*8 + get_column(element))   

big_list = [rows, columns, id_list]

print('Largest seat ID is ', max(id_list))

df = pd.DataFrame(big_list)
df = df.T

df = df.rename(columns={0: 'Rows', 1:'Columns', 2: 'ID'})
print(df['Rows'].valu_counts())
print(df['Columns'].value_counts())
print(df.head())

