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
    play_game = "Yes"
    while play_game == "Yes":
        try:
            user_number = int(input("Enter a number: "))
        except:
            print("Please enter a number")
        else:
            if user_number % 2 == 0:
                print("That is an even number!")
                play_game = input("Continue? Yes/No: ")
            else:
                print("That is an odd number!")
                play_game = input("Continue? Yes/No: ")
    if play_game == "No":
        print("Ok, bye bye!")


def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    count = 1
    while count <= 100:
        if count % 10 == 0:
            print(count)
        else:
            print(count, end = " ")
        count += 1


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    inputs_list = []
    while True:
        user_input = input("Type number: ")
        if user_input == "done":
            return sum(inputs_list)/len(inputs_list)
        inputs_list.append(int(user_input))


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
