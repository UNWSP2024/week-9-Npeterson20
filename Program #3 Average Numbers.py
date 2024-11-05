# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.
    # Add your code here #

    def calculate_total_and_average():
    try:
        with open("numbers.txt", "r") as file:
            numbers = file.readlines()
            total = 0
            count = 0
            for line in numbers:
                try:
                    number = int(line.strip())
                    total += number
                    count += 1
                except ValueError:
                    print(f"Non-integer value encountered and skipped: {line.strip()}")
            if count > 0:
                average = total / count
                print(f"The total is: {total}")
                print(f"The average is: {average}")
            else:
                print("No valid integers found in the file.")
    except IOError:
        print("An error occurred while trying to read the file.")

calculate_total_and_average()


# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()
