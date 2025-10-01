"""This program will print a receipt for a customer utilizing information
gathered from a csv file containing order details and another csv file 
product information. For my improvements, I opened both files using the same
read_dictionary method.  In the exception block for the file-not found error, 
I gave the user the opportunity to input the name of the file. For the permission
error, the program will wait while the user contacts the administrator to get 
access to the file.  The user can then press enter to continue the program.  I 
added the return date to the bottom of the receipt.  """

#Import tools
import csv
import os
from datetime import datetime, date, timedelta


# Prepare explicit file path names for guaranteed file handling despite 
# where the program is run. 
path=os.path.dirname(__file__)
request_path=os.path.join(path, "request.csv")
products_path=os.path.join(path, "products.csv")

def read_dictionary(filename, key_column_index):
    """This function reads a csv file and returns a dictionary variable 
    containing the information contained in the csv file"""

    dictionary = {}
    while True: 
        try: 
            file = open(filename, "rt") 
            break

        except FileNotFoundError:
            print(f"File not found. The file {filename}  does not exist")
            category = os.path.splitext(os.path.basename(filename))[0]
            user_input = input(f"Please enter the name for the file located in the program directory which holds the {category} information.")
            path=os.path.dirname(__file__)
            filename=os.path.join(path, user_input)
        except PermissionError: 
            print(f"You do not have permissions to the file {filename}. Please speak to an administrator.")
            again = input("Press Enter to try again")            

    reader=csv.reader(file)
    next(reader)
    for line in reader: 
        try: 
            key=line[key_column_index]
            dictionary[key]=line
        except KeyError: 
            print(f"The dictionary does not contain an entry for {key}.")
    
    file.close()

    return dictionary

def create_receipt(products_dict, request_dict):
    print ("\n\n              Razor's Edge Groceries\n\n")
    subtotal = 0
    total_items = 0
    print(f"{'Item':<20}{'Qty':<13}{'Price':<12}") 
    for request in request_dict.values(): 
        common_key = request[0] 
        qty = int(request[1])
        try: 
           product_dict = products_dict[common_key]
        except KeyError:
           print(f'\n\nError: unknown product ID "{common_key}" in the request.csv file.  \nPlease recheck your order.\n\n')
        item = product_dict[1]
        price = float(product_dict[2])
        line_cost = round(price * qty, 2)
        subtotal += line_cost
        total_items += qty
        print (f"{item:<20}  {qty:<10} ${price:<10,.2f}")
    return total_items, subtotal

def main():

    # Create products dictionary
    filename=products_path
    key_column_index = 0
    products_dict =read_dictionary(filename, key_column_index)

    # Create request dictionary
    filename=request_path
    request_dict=read_dictionary(filename, key_column_index)

    total_items, subtotal = create_receipt(products_dict, request_dict)
    taxes= total_items * .06
    total= subtotal + taxes
    now = datetime.now()
    return_window= timedelta(days=30)
    return_date = now + return_window
    return_date = return_date.replace (hour=21, minute=0, second=0)
    print(f"{'Total Items Purchased: ':>30}{' ':>3}{total_items:<10}")
    print(f"{'Subtotal: ':>30}{'$':>3}{subtotal:<10,.2f}")
    print(f"{'Sales Tax: ':>30}{'$':>3}{taxes:<10,.2f}")
    print(f"{'Total: ':>30}{'$':>3}{total:<10,.2f}")
    print("Thank you for shopping with Razor's Edge!")
    print(f"We are happy to accept your qualified\n returns until {return_date.strftime("%m/%d/%Y %I%M")}\n\n")
    print(f"{now.strftime("%m/%d/%Y %I:%M:%S %p"):>42}")
    print("\n\n")

if __name__=="__main__":
    main()