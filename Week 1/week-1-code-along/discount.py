"""You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store’s 
slowest sales days. On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, the store will 
discount the customer’s subtotal by 10%.""" 

# Import needed modules
from datetime import datetime

#Initialize subtotal variable at 0
subtotal = 0

# Retrieve the day of the week from the system clock using datetime module
today = datetime.now()
day = str(today.strftime("%A"))

print("This program will collect the subtotal from a user and determine the discount per store policy.")
# Start main loop
loop = True
while loop: 
    qty = int(input("Please enter the quantity you wish to purchase:"))
        
    while not qty == 0:
        cost = round (float(input("Please enter the cost of the item you wish to purchase:")),2)
        subtotal = float(subtotal + (cost * qty))
        print (f"Your subtotal so far is ${subtotal:.2f}.")
        qty = int(input("Please enter the quantity you wish to purchase:"))
        

    if day in ("Tuesday", "Wednesday"): 
        discount = True
    else: 
        discount = False

    if discount == True:
        if subtotal >= 50:
            dscnt = subtotal * .1
            total = subtotal - dscnt
            tax = total * .06
            grandtotal = total + tax
        
            print(f"Your {day} discount is ${dscnt:.2f}.")
            print(f"Your sales tax is ${tax:.2f}.")  
            print(f"The total amount due is ${grandtotal:.2f}.")  
            print ("Thankyou for shopping with us!")
            loop = False
        else: 
            invalid = True
            while invalid: 
                shortage = 50-subtotal
                shop = input(f"You will qualify for the {day} discount if you spend ${shortage:.2f} more!"
                            "  Would you like to continue shopping?")
                if shop in ("Yes", "Y", "yes", "y"): 
                    invalid = False
                    loop = True
                    print("Please return when you have finished shopping.")
                    continue
                elif shop in ("No", "N", "no", "n"):
                    invalid = False
                    loop = False
                    tax = subtotal * .06
                    grandtotal = subtotal + tax
                    print(f"Your  did not qualify for the {day} discount.")
                    print(f"Your sales tax is ${tax:.2f}.")  
                    print(f"The total amount due is ${grandtotal:.2f}.")  
                    print ("Thankyou for shopping with us!")
                    loop = False
                    continue
                   
                else: 
                    invalid = True
                print("Please enter yes or no!") 
    else: 
        tax = subtotal * .06
        grandtotal = subtotal + tax
        print(f"Your sales tax is ${tax}:.2f.")  
        print(f"The total amount due is ${grandtotal}:.2f.")  
        print ("Thankyou for shopping with us!")
        loop = False
