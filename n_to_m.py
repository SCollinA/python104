# ask user for start number
# ask user for end number
# print out numbers from start to end on separate lines

BAD_INPUT = True
ERROR_MESSAGE = "Bad user input."

# continue to ask for user input until good input recieved
while BAD_INPUT:
    try: # ask for user input and catch exception if it is not int
        start_input = int(input("Start from: "))
        BAD_INPUT = False # this line reached if input is good, change flag and exit loop
    except:
        print(ERROR_MESSAGE)

# Reset input flag to ask for end number
BAD_INPUT = True
while BAD_INPUT: # ask until an int is received
    try: # catch expection if non-int received
        end_input = int(input("End on: "))
        if start_input < end_input: # if start is less than end
            BAD_INPUT = False # change flag, exit loop
        else: # if start is not less than end
            print(ERROR_MESSAGE)
    except:
        print(ERROR_MESSAGE)


while start_input <= end_input:
    print(start_input)
    start_input += 1