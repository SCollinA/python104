# Ask user for string input. Print string with box of asterisks around it.

user_string = input("Text? ")
string_length = len(user_string)
box_length = string_length + 4 # box stretches one space and one asterisk on each side of string
rows = 3 # one row for user string and one row above and below string

row_counter = 0 # keep track of which row loop is on
while row_counter < rows:
    col_counter = 0 # keep track of which col loop is on
    while col_counter < box_length: 
        if row_counter == 0 or row_counter == rows - 1: # if first or last row
            print('*', end='') # print all asterisks
        else: # if middle row
            # if first or last col, just print *
            if col_counter == 0 or col_counter == box_length - 1:
                print('*', end='')
            # else if second or second to last col, print ' '
            elif col_counter == 1 or col_counter == box_length - 2:
                print(' ', end='')
            else: # if not first two cols or last two cols
                print(user_string, end='') # print whole string without starting new line
                # add number of cols in string to col_counter
                col_counter += string_length - 1 # subtract 1, because it will be incremented again below
        col_counter += 1 # move to next col
    print() # move to next line
    row_counter += 1 # move to next row
