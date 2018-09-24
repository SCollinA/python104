# Ask user for number. Print factors of users number.

BAD_INPUT = True # set flag for asking for user input
ERROR_MESSAGE = "Bad user input." # message if bad input received

while BAD_INPUT: # continue to ask for input until is is int
    try: # prompt user for size of square
        number = int(input("Give me a number, any number. "))
        BAD_INPUT = False # good input received, change flag, except loop
    except: 
        print(ERROR_MESSAGE) # inform user of bad input

factor = 1
other_factor = 2

while factor < other_factor: # check all numbers up to half of given number
    if number % factor == 0:
        other_factor = int(number / factor)
        print("%d, %d" % (factor, other_factor))
    factor += 1