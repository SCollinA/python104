# print a triangle 4 rows high using * chars

ROWS = 4 # number of rows of triangle (height)
COLS = (ROWS * 2) - 1 # number of cols in triangle (width)
row_counter = 0 # variable to loop through rows

while row_counter < ROWS: # while not past last row
    asterisks = 1 + (2 * row_counter) # number of asterisks on row
    spaces = COLS - asterisks # number of spaces on row
    end_spaces = spaces / 2 # half number of spaces
    col_counter = 0 # place on row
    while col_counter < COLS: # while not past last col
        if spaces == end_spaces and asterisks > 0: # if half of spaces have been printed
            print('*', end='') # print asterisks
            asterisks -= 1 # reduce number of remaining asterisks
        else: 
            print(' ', end='') # print spaces
            spaces -= 1 # decrement remaining spaces
        col_counter += 1 # move to next col
    print() # move to next line
    row_counter += 1 # move to next row
