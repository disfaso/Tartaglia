import numpy as np

def calculate_line(before:list):
    coeff: list
    t = 0
    while t < len(before)+1:
        coeff[t] = 0
    # coeff[0] = 1
    # coeff[before.size+1] = 1

    for i in coeff:
        if i == 0 or i == len(before)+1:
            coeff[i] = 1

        elif i == 1 or i == len(before):
            coeff[i] = 1 + before[i]

        else:
            coeff[i] = before[i-1] + before[i]

    return coeff

print('Input the number of line of the Tartaglia triangle')

line = int(input())


# initializing variables
coefficient = [1]
c = 0


while c < line:
    coefficient = calculate_line(coefficient)
    c += 1




print(coefficient)
