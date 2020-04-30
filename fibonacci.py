# Python script for calculating the fibonacci sequence,
# user input specifies the length of sequence


def fib_sequence(n):

    # if user enters value less than or equal to 0, default value of 0 is returned
    if n<=0:
        return 0

    counter = 0
    fib_seq = []

    #while loop calculates fibonacci sequence until counter is greater than n
    while (counter <= n):

        #if, elif statements output sequence if length is 1 or 2 else fibonacci number calculated
         if n == 1:
             fib_seq.append(0)
         elif n == 2:
            fib_seq.append(0)
            fib_seq.append(1)
         else:
             fib_seq.append(fib_seq[-1] + fib_seq[-2])

        # increment counter
         counter +=1

    #convert fibonacci sequence to strings so they can be displayed in a list
    for num in fib_seq:
        fib_seq[num] = str(fib_seq[num])

    return (', '.join(fib_seq))


def main():

    while True:

        #try, except statement to catch error if user inputs non-integer value
        try:
            #converting user's string input into integer and calling fib_sequence function
            fib_input = fib_sequence(int(input('Enter the length of fibonacci sequence')))
            print(fib_input)
            break

        except:
            print('\nPlease enter a valid number')
            print('\n')

if __name__ == '__main__':
    main()
