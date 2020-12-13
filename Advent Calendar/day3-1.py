# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees (#) would you encounter?

map = open('input-day3.txt')

dat = map.read().split('\n')

def slope(dat, step, col):
    cts = []
    pos_col=0
    
    for row_num in range(0, len(dat)-1, step):
        row = str(dat[row_num])

        if row[pos_col] == '#': 
            cts.append('X')
        else:
            cts.append('O')

        pos_col = (pos_col + col) % len(row)    

    return cts.count('X')

print('Number of trees: ', slope(dat, 1, 3))
print('Number of trees: ', slope(dat, 1, 1)*slope(dat, 1, 3)*slope(dat, 1, 5)*slope(dat, 1, 7)*slope(dat, 2, 1))