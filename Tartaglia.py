import numpy as np

def calculate_line(before:list):
    coeff = []
    coeff.size = before.size+1
    # coeff[0] = 1
    # coeff[before.size+1] = 1

    for i in coeff:
        if i == 0 or i == before.size+1:
            coeff[i] = 1

        elif i == 1 or i == before.size:
            coeff[i] = 1 + before[i]

        else:
            coeff[i] = before[i-1] + before[i]

    return coeff

print('Input the number of line of the Tartaglia triangle')

line = int(input())


# initializing variables
coefficient = []
c = 0


while c < (line+1):
    coefficient[c] = c
    c += 1




print(coefficient.size())
