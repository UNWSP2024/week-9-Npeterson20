# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.


def count_names_in_file():
    try:
        with open("names.txt", "r") as file:
            names = file.readlines()
            name_count = len(names)
            print(f"The number of names in the file is: {name_count}")
    except IOError:
        print("An error occurred while trying to read the file.")

count_names_in_file()



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()
