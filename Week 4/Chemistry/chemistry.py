"""This program will ask the user for a chemical formula and a sample size in 
grams.  It will then calculate and display the molar mass and the number of 
moles in the sample.  I made several improvements to the program.  First, I
placed the program in a loop that will continue running until the user says
to stop.  The program will give the user a parting message at that time. 
Second, I added formula format validation which allows the user to continue 
in the program if they enter an invalid formula.  Third, I made the formula 
case insensitive.  The user can enter the formula in any case and as long as 
their letters are correct, the formula will be formatted to utilize the 
dictionary appropriately."""

# Import csv for managing the csv file.  Import os for ensuring debugging 
# will work.  Import required parse_formula function from formula program. 
import csv
from formula import parse_formula
import os
import re

def format_formula(periodic_table_dict, formula: str)->str:
    invalid = True
    while invalid: 
        parts = re.findall(r"[A-Za-z]+|\d+",formula)
        result = ""
        all_valid=True

        for part in parts:
            if part.isalpha():
                part=part.capitalize()
                result += part.capitalize()
                if part in periodic_table_dict:
                    continue
                else: 
                    print(f"{part} is not an element in the Periodic Table.\n\n")
                    formula = input("Please enter the chemical formula for the compound:  ")
                    all_valid=False
                    break                  
            else: 
                result += part
        if all_valid:
            invalid = False
    return result
    

def validate_yn(prompt):
    """This function will validate yes and no responses.
    parameters: prompt -the prompt question to ask the user
    return boolean
    """

    valid = False
    while not valid:
        user_input = input(prompt).strip().lower()
        if user_input in ["y", "yes"]:
            valid = True
            return True
        elif user_input in ("n", "no"): 
            Valid = True
            return False
        else: 
            print("Invalid response!  Please enter 'y' or 'n'.")

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """This function computes the molar mass of the molecule identified
    by the user and returns that mass
    parameters: symbol_quantity_list
                periodic_table_dict
    return: total_mass
    """
    total_mass = 0

    for item in symbol_quantity_list: 
       element = item[0]
       element_list= (periodic_table_dict[element])
       atomic_weight=float(element_list[1])
       quantity = int(item[1])
       weight = atomic_weight * quantity
       total_mass += weight 
    return total_mass

def make_periodic_table():
    """This function utilizes a csv file containing all of the elements
    in the periodic table along with their atomic weights and symbols
    to build a dictionary in memory.  The dictionary will have a key 
    equal to the symbol for the element and will contain a list with 
    the element name and the atomic weight of the element as its value. 
    The function will return the completed dictionary. 
    parameters: none
    return periodic_table_dict
    """
    periodic_table_dict = {}
    
    script_dir = os.path.dirname(__file__)
    file_path= os.path.join(script_dir, "periodic-table.csv")

    with open(file_path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)

        for row in reader:
            key = row[0].strip(" ,")
            value1= row[1].strip(" ,")
            value2= float(row[2])

            periodic_table_dict [key] = [value1, value2]
    return periodic_table_dict
    
def main():
    """The main function will ask the user for the chemical formula
    and the sample size.  It will call the function to create the 
    periodic table dictionary.  It will call the parse_formula 
    function to get a list of elements in the function.  It will 
    then call the compute_molar_mass function to calculate the 
    molar mass.  It will then calculate the number of moles
    in the sample. Finally, it will display the molar mass 
    and the number of moles for the user."""

    # Create the periodic table dictionary. 
    periodic_table_dict = make_periodic_table()
    
    # Introduce program and et information from the user

    print("This program will calculate the molar mass and the number of moles " \
    "present in a sample as identified by the user. \n\n")
    again= True
    while again: 
        formula=format_formula(periodic_table_dict, input("Please enter the chemical formula for the compound:  "))
        sample_size=float(input("Please enter the size of your sample in grams:  "))

        symbol_quantity_list=parse_formula(formula, periodic_table_dict)
        molar_mass=compute_molar_mass(symbol_quantity_list, periodic_table_dict)
        total_moles=round(sample_size/molar_mass,5)

        print(f"Your sample has a molar mass of {molar_mass} and contains a total of {total_moles} moles.\n")
        again = validate_yn("Would you like to calculate another sample?")
    print("\n\nThank you for using our program.  Have a nice day!\n\n")    


if __name__ == "__main__":
    main()