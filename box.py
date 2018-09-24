# Ask user for width and height of box. Print box using one * character per unit length of box, and fill inside of box with empty space

BAD_INPUT = True # set flag for asking for user input
ERROR_MESSAGE = "Bad user input." # message if bad input received

while BAD_INPUT: # continue to ask for input until is is int
    try: # prompt user for size of square
        width = int(input("Width? "))
        BAD_INPUT = False # good input received, change flag, except loop
    except: 
        print(ERROR_MESSAGE) # inform user of bad input

BAD_INPUT = True

while BAD_INPUT: # continue to ask for input until is is int
    try: # prompt user for size of square
        height = int(input("Height? "))
        BAD_INPUT = False # good input received, change flag, except loop
    except: 
        print(ERROR_MESSAGE) # inform user of bad input

# max_height = height
# max_width = width
# while height > 0: # until all rows printed
#     new_width = width
#     while new_width > 0: # until all cols printed
#         if height == max_height or height == 1: # if first row or last row
#             print('*', end='') # just print all * chars
#         else:
#             if new_width == max_width or new_width == 1: # if first col or last col
#                 print('*', end='') # just print one *
#             else: # middle cols
#                 print(' ', end='') # print one empty space
#         new_width -= 1 # decrement cols counter
#     print() # start new line
#     height -= 1 # decrement rows counter

row_counter = 1 # start on row 1
while row_counter <= height: # until all rows printed
    col_counter = 1 # start on col 1    
    while col_counter <= width: # until all cols printed
        if row_counter == 1 or row_counter == height or col_counter == 1 or col_counter == width: # if first row or last row or first col or last col
            print('*', end='') # just print all * chars
        else:
            # if col_counter == 1 or col_counter == width: # if first col or last col
            #     print('*', end='') # just print one *
            #else: # middle cols
            print(' ', end='') # print one empty space
        col_counter += 1 # decrement cols counter
    print() # start new line
    row_counter += 1 # decrement rows counter