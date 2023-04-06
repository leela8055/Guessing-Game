# Module to compare input value and give comments accordingly

import List  # Module created to generate a list of numbers of a given range
import cheering


def conditions(p):  # conditions for comparing the values and giving hint

    newlist = List.List(1, 100)  # creating a list of numbers to find the range of the remaining guesses for hint

    # initiating a and b
    a, b = 0, 101

    for i in range(1, 100):  # loop for repeating the user input and comparing to the generated number

        # taking user input
        q = int(input("Please enter a value to guess the generated number or press ""'0'"" to exit : """))

        assert q >= 0, 'Please enter a value in between 1 and 100 or "0" to exit.'  # error input
        assert q <= 100, 'Please enter a value in between 1 and 100 or "0" to exit.'  # error input

        if q == 0:  # option to exit the game
            quit()

        elif q <= a or q >= b:  # checking if the guesses are following the logical elimination pattern
            print('Hint: Now the number lies between %d and' % a, '%d\n' % b)
            print('Check the hint to decrease your guesses ;)\n')

        else:
            # storing the first value of the list
            v = newlist[0]

            if q < p:
                del newlist[:q-v]  # editing the list to delete the logically eliminated values

                # output information
                print('Number of guesses is %d\nEntered value is "Lesser" than the generated value' % i)

                # storing the new list limiting values
                a = newlist[0]
                b = newlist[-1]

                # output information
                print('Hint: Now the number lies between %d and' % a, '%d\n' % b)

            elif q > p:
                del newlist[q-v+1:]  # editing the list to delete the logically eliminated values

                # output information
                print('Number of guesses is %d\nEntered value is "greater" than the generated value' % i)

                # storing the new list limiting values
                a = newlist[0]
                b = newlist[-1]

                # output information
                print('Hint: Now the number lies between %d and' % a, '%d\n' % b)

            elif q == p:
                print('Congratulations!!!\nYou have guessed it "correctly"\nYou have taken %d guesses\nThe generated and the entered values match\n' % i)
                cheering.success()  # sounds
                break
