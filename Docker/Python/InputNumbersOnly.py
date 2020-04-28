#The below 'only_numbers' method is to check and make the user to enter a valid number per the instruction given to them.
def only_numbers(list):
    # The below if code is used when a user has to enter a number from a given range.
    if len(list) == 3:
        pre_number = 0
        # list[0] is the instruction for the user to enter a number from a given range.
        # list[1] is the minimum number the user can enter.
        # list[2] is the maximum number the user can enter.
        while not list[1] <= pre_number <= list[2]:
            try:
                pre_number = int(input(list[0]))
                if not list[1] <= pre_number <= list[2]:
                    print("You didn't enter a number from " + str(list[1]) + " to " + str(list[2]) + ".")
            except ValueError:
                print("You didn't enter a valid number.")
                pre_number = 0
        return pre_number

    #The below elif code is used when a user has to enter a number unlimited to a range.
    elif len(list) == 1:
        # list[0] is the instruction for the user to enter a number.
        pre_number = "0"
        while type(pre_number) is not float:
            try:
                pre_number = float(input(list[0]))
            except ValueError:
                print("You didn't enter a valid number.")
        return pre_number
