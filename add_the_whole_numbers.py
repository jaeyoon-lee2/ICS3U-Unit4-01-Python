#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Oct 2019
# This program uses a while loop


def main():
    # this function uses a while loop
    loop_counter = 0
    result = 0

    # input
    positive_integer = int(input("Enter the number you want to add from 1: "))
    print("")

    # process & output
    while loop_counter <= positive_integer:
        result = loop_counter + result
        loop_counter = loop_counter + 1
    print("Sum of 1 to {0} is {1}".format(positive_integer, result))

if __name__ == "__main__":
    main()
