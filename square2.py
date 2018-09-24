# Ask user for length of square. Print square using one * character per unit length of square.

BAD_INPUT = True # set flag for asking for user input
ERROR_MESSAGE = "Bad user input." # message if bad input received

while BAD_INPUT: # continue to ask for input until is is int
    try: # prompt user for size of square
        square_length = int(input("How big is the square? "))
        BAD_INPUT = False # good input received, change flag, except loop
    except: 
        print(ERROR_MESSAGE) # inform user of bad input

side1 = square_length # first side of square, rows
while side1 > 0: # until all rows printed
    side2 = square_length # second side of square, cols
    while side2 > 0: # until all cols printed
        print('*', end='') # print each * without starting new line
        side2 -= 1 # decrement cols counter
    print() # start new line
    side1 -= 1 # decrement rows counter