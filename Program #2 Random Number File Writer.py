# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).



import random

def write_random_numbers_to_file():
    try:
        count = int(input("How many random numbers would you like to generate (up to 1000)? "))
        if 1 <= count <= 1000:
            with open("random_numbers.txt", "w") as file:
                for _ in range(count):
                    number = random.randint(1, 500)
                    file.write(f"{number}\n")
            print(f"{count} random numbers have been written to 'random_numbers.txt'.")
        else:
            print("Please enter a number between 1 and 1000.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

write_random_numbers_to_file()
