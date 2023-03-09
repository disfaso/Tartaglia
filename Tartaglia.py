import numpy as np


print('Input the number of line of the Tartaglia triangle')

line : int = input()

coefficient = []
c = 0
while c < line+1:
    coefficient[c] = c
    c += 1
    


print(coefficient.size())
