#!/usr/bin/env python3
# HW05_ex00_logics.py


##############################################################################
def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    try:
        user_input = int(input("Enter an integer : "))
        if user_input % 2 == 0:
            print("{} is even!".format(user_input))
        else:
            print("{} is odd!".format(user_input))
    except:
        print("That's not a valid integer")


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    cell_value = 1
    for row in range(0, 10):
        for column in range(0, 10):
            print(cell_value, end=" ")
            cell_value += 1
        print("\n")


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    number_list = []
    print("Enter the numbers you want to find the average of. "
          "When you want to stop, enter done")
    while True:
        try:
            user_input = input("Enter number : ")
            if user_input.lower() == "done":
                if len(number_list) > 0:
                    return sum(number_list)/len(number_list)
                else:
                    return "Nothing to average!"
            else:
                number_list.append(float(user_input))
        except:
            print("That's not a valid number, try again!")


##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    print(find_average())


if __name__ == '__main__':
    main()
