# ------------------------------------------------- #
# Title: Assignment 7- Pickling and Structured Error Handling
# Description: Demonstrates pickling data and exception handling in python
# ChangeLog: (Who, When, What)
# NDaharia, 06-01-2022, Created
# NDaharia, 06-02-2022, Completed Assignment07
# ------------------------------------------------- #

# Data
dataList = []  # list
objFile = "age.dat"  # file where data will be stored
strChoice = ""  # empty string that will save user input
strEnd = ""  # empty string that will store whether the user wants to exit

import pickle
from datetime import date


def read_file(file_name):
    '''
    Function unpickles and loads data from file_name.
    :param file_name: name of file to be read
    :return: file data
    '''
    try:
        file = open(file_name, "rb")
        file_data = pickle.load(file)
        file.close()
        print(file_data)
    except:
        print("File not found.")


def write_file(file_name, some_list):
    '''
    Function writes pickled data in some_list to the file file_name.
    :param file_name: name of file that data is written to
    :param some_list: list of data that will be written to file
    :return: nothing is returned
    '''
    try:
        file = open(file_name, "wb")
        pickle.dump(some_list, file)
        file.close()
        return 'Success!'
    except Exception as e:
        print("Error.")
        print(e)


def input_age():
    '''
    Asks for user input for their age.
    :return: returns the integer that have been inputted by the user
    '''
    try:
        age = int(input("Enter your age in years: "))
        if (age <= 0 or age > 100):
            raise Exception("Please choose an age in between 0 and 100!")

        return age
    except ValueError as e:
        print("Please choose an integer!")
        print(e)
    except TypeError as e:
        print("Please choose an integer!")
        print(e)


def yearOfBirth(age):
    '''
    Returns the year of birth for given age.
    :param age: age in years.
    :return: the year of birth.
    '''

    # creating the date object of today's date
    todays_date = date.today()
    return todays_date.year - age


def add_to_list(data, list_name):
    '''
      Appends data to a list
      :param data: Some integer values
      :param list_name: List that lists integer values
      :return: updated list after the data has been appended
      '''
    list_name.append(data)
    return list_name


while True:  # main script
    print(
        """
        1 = Enter your age to list in memory
        2 = Save data to disk
        3 = Load data from disk
        4 = Exit
        """
    )
    strChoice = input("Which choice would you like to do from the menu? ")

    if strChoice == "1":
        try:
            age = input_age()
        except Exception as e:
            # there was an error getting the age,
            print(e)
            continue  # return to beginning of while loop.

        # add the age to the list
        add_to_list(age, dataList)

        # compute the year of birth from the entered age
        year = yearOfBirth(age)

        # add the year to the list
        add_to_list(year, dataList)

        print(f"You added {age} and {year} to the list in memory {dataList}")
        continue  # return to the beginning of the while loop

    if strChoice == "2":
        write_file(objFile, dataList)
        print("Data Saved!")
        continue

    if strChoice == "3":
        read_file(objFile)
        continue

    if strChoice == "4":
        strEnd = input("Do you wish to continue? Answer 'y' or 'n'")
        if strEnd.lower() == 'y':
            print("Unsaved data will be lost, exiting!")
            break  # break out of the while loop and end the program
        else:
            continue

    else:
        print("Please Choose one of the 4 integer choices from the menu.")
