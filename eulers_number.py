# Script for calculating and displaying Euler's Number a set amount of
#decimal places which is specified by the user

import math

def calculate(input_val):

    #math.e function only rounds to a maximum of 15 decimal places
    e = round(math.e, input_val)
    return e

def main():

    while True:

        #try, except statement to catch error if user inputs non-integer value
        try:
            #converting user's string input into integer and calling calculate function
            input_val = calculate(int(input('Please enter the number of decimal places you want e to be to: ')))
            print (str(input_val))
            break

        except ValueError:
            print('\nPlease enter a valid number')
            print('\n')

if __name__ == '__main__':
    main()
