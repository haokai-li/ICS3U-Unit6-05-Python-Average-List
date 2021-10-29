#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program calculate average and list


def calculated_average(calculate_user_number):
    # This function calculate average and list
    total_number = 0

    # process
    for list_number in calculate_user_number:
        total_number += list_number
    total_number = total_number / len(calculate_user_number)

    # process
    number_float = total_number + 0.5
    total_number = int(number_float)

    return total_number


def main():
    # This function calculate average
    average_list = []
    user_number = None

    # output
    print("Please enter 1 mark at a time. Enter -1 to end.")
    print("")

    while user_number != -1:
        # input
        user_string = input("What is your mark? (as %): ")

        try:
            user_number = int(user_string)
            average_list.append(user_number)

        except Exception:
            # output
            print("You didn't enter an integer.")

    # remove -1
    average_list.pop()

    # call functions
    average_number = calculated_average(average_list)

    # output
    print("")
    print("The average is: {}%".format(average_number))


if __name__ == "__main__":
    main()
