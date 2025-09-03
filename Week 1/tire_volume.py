"""This program will calculate tire volume using user's input of the tire width, the aspect ratio, and the wheel diameter.  
The program will print the volume to the terminal and will append the date and tire details to the volumes.txt file.  Additionally,
the program uses a user-defined function for validating user input for the various sizes and for error handling if the user inputs
the wrong data type.  The program uses a while loop to allow for a user to choose to continue to look up additional tires.  The 
program also uses an if statement to handle exceptions for the continue question.  Finally, the program asks the user if they would 
like to receive a quote for purchasing tires of the identified size.  The program gives the user options to receive the quote by 
telephone, text, email, or home delivery via mail.  The program records this information in a separate file called quotes.txt which
can be used by employees to generate the quotes and deliver them to the customer in the formats requested. """

# Import modules and initiate needed variables
from datetime import datetime
import math
pi = math.pi

# Create function to validate integers.  
def validate_integer (prompt):
    valid = False
    while not valid:
        try:
             user_input = int(input(prompt))
             valid = True
             return user_input
        except ValueError: 
            print ("Please enter a valid integer!")

# Create function to validate Yes/No answers
def validate_yn(prompt):
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
    
# Open files
with open("volumes.txt", "a") as volumes,  open("quotes.txt", "a") as quotes: 
        quotes.write("Quotes to be written within 24 hours:\n\n")
        again = True
# Initiate loop to ensure a valid selection
        while again:
            now = datetime.now()
            date = datetime.date(now)
# Get required input from users

            print("This program will determine the volume of your tire utilizing measurements gathered from you.")

            width = validate_integer ("Enter the width of the tire in mm (ex 205):")
            aspect =  validate_integer("Enter the aspect ratio of the tire (ex 60):")
            diam = validate_integer("Enter the diameter of the wheel in inches (ex 15):")

# Calculate the volume of the tire, print the volume to the terminal and print the required information to the volumes.txt file. 
            volume = round(((pi * (width * width) * aspect) * ((width * aspect) + (2540*diam)))/10000000000, 2)

            print(f"The approximate volume is {volume} liters")

            volumes.write(
                f"{date}, {width}, {aspect}, {diam}, {volume}\n")
            
# Ask the user if they would like a quote.  Determine the type of quote and collect relevant information.            
            purchase = validate_yn("Would you like to receive a quote to purchase tires of this size?")
            if purchase: 
                contact_phone = None
                email = None
                text = None
                by_phone = None
                digital = None
                paper = False
                name = input("Please enter your full name:")
                address = input("Please enter your mailing address:")
                
                while True: 
                    by_phone = validate_yn("Would you like to receive the quote over the phone?")
                    if by_phone: 
                        contact_phone = input("Please enter your phone number:")
                        text = validate_yn("Would you like to receive a copy of your quote by text?")


                    digital = validate_yn("Would you like us to send the quote by email?")
                    if digital: 
                        email = input ("Please enter your email address:") 

                    if not by_phone and not digital:
                        paper = validate_yn("Would you like us to send a paper copy to your home?")
                        if paper:
                            break
                    if not by_phone and not digital and not paper:
                        print("We are sorry, this is currently all of the available options.  Please choose an option.")
                    else: 
                        break
# Write the gathered information to the quotes file in a format appropriate to help employees provide the requested quotes.
                quotes.write(
                    f"Time requested: {now}\n"
                    f"Customer Name: {name}\n"
                    f"By Phone/By Text ({by_phone}/{text}): {contact_phone}\n"
                    f"Email ({digital}): {email}\n"
                    f"Home address ({paper}): {address}\n"
                    f"Tire Size Requested - {width}-{aspect}-R{diam}\n\n"
                )

                print("You will receive your quote within 24 hours.  Thank you for shopping with us!")
# Give the customer the opportunity to check another tire or close the loop.  
            again = validate_yn("Would you like to check another tire?")

#Close the open files.          
quotes.close()                
volumes.close()
