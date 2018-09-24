# Print a 5x5 square of * characters

row_counter = 5 # number of rows

while row_counter > 0: # loop through all rows
    col_counter = 5 # number of columns
    while col_counter > 0: # loop through all cols
        print('*', end='') # print one * per col without starting new line
        col_counter -= 1 # decrement cols remaining
    print() # move to new line
    row_counter -= 1 # decrement rows remaining
