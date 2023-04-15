def calculate_line(before:list):
    coeff: list = [0] * (len(before)+1+0)


    for i in range(len(coeff)):
        if i == 0:
            coeff[i] = 1

        elif i == len(before):
            coeff[i] = 1

        else:
            coeff[i] = before[i-1] + before[i]

    return coeff

print('Input the number of line of the Tartaglia triangle')

line = int(input())



# initializing variables
coefficient : list = [1]
c = 0

# iterate from 0 to line, calculating the coefficients from the one before
while c < line:
    coefficient = calculate_line(coefficient)
    c += 1



print(coefficient)

