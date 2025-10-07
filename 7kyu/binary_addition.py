'''Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.'''

'''
1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
'''
#my solution

import re
def add_binary(a,b):
    binary_string = bin(a + b)
    match = re.match(r'(0b)(\d+)', binary_string)
    #string is inside a match object
    #to access match object you have to use .group()
    if match:
        return (match.group(2))

a = 1
b = 1
print(add_binary(a, b))