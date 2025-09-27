"""This program will generate random numbers and append them to a number's list in a library."""

import random

def append_random_numbers(numbers_list, quantity=1):
    i=0
    for i in range (quantity):
        number = round(float((random.uniform(1,100))), 2)
        numbers_list.append(number)

def main():
    numbers_list = []
    append_random_numbers(numbers_list)    
    append_random_numbers(numbers_list,7)
    print(numbers_list)



if __name__ == "__main__":
    main()