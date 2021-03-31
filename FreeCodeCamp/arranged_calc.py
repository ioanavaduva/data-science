def arithmetic_arranger(problems, show_res = False):

    if len(problems) > 5: # there are too many problems supplied to the function. The limit is five, anything more will return: Error: Too many problems.
        return 'Error: Too many problems.'
    else:
        pass
    
    sep_problems = [] # split the strings into individual entries
    for prob in problems:
        pb = prob.split(' ')
        sep_problems.append(pb)

    for problem in sep_problems:
        if len(problem[0]) > 4 or len(problem[2]) > 4 : # Each operand (aka number on each side of the operator) has a max of four digits in width.
            return 'Error: Numbers cannot be more than four digits.'
        else:
            pass

        if problem[1] == "+" or problem[1] == "-": # The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. 
            pass
        else:
            return "Error: Operator must be '+' or '-'."
        
        try: #Each number (operand) should only contain digits. 
            int(problem[0]) and int(problem[2])
        except:
            return 'Error: Numbers must only contain digits.'

    row1 = ''
    row2 = ''
    row3 = ''
    row4 = ''

    for index, problem in enumerate(sep_problems, start=1):
        
        n = max(len(problem[0]), len(problem[2])) # find longest number
        m = n + 2 # number of spaces for each column
        
        if index == len(sep_problems):
            w = ''
        else:
            w = 4*' '

        row1_entry = (m-len(problem[0]))*' ' + problem[0] + w
        row1 = row1 + row1_entry

        row2_entry = problem[1] + (m-1-len(problem[2]))*' ' + problem[2] + w
        row2 = row2 + row2_entry

        row3_entry = m * '-' + w
        row3 = row3 + row3_entry

        result = eval(problems[index-1])
        row4_entry = (m - len(str(result)))*' ' + str(result) + w
        row4 = row4 + row4_entry

    if show_res:
        arranged_problems = row1 + '\n' + row2 + '\n' + row3 + '\n' + row4
    else:
        arranged_problems = row1 + '\n' + row2 + '\n' + row3
    
    return arranged_problems

b = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"], True)
print(b)