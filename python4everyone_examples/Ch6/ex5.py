# Take the following Python code that stores a string: 'str =
# 'X-DSPAM-Confidence: 0.8475'. Use find and string slicing to extract the
# portion of the string after the colon character and then use the float
# function to convert the extracted string into a floating point number.

string = 'X-DSPAM-Confidence: 0.8475'
loc = string.find(' ')
num = string[loc+1:]
num_float = float(num)
print(num_float)