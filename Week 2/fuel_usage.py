def validate_float(user_input):
    try:
        valid_float=float(user_input); 
    except:
        print ("You must enter a valid float (ex. 12.3).  Please try again.");
        valid=False;
        valid_float = 0;
        return(valid_float, valid)
    
    if valid_float >=0:
        valid = True;
    else:
        print("Please enter a positive number!");
        valid_float = 0;
        valid = False;  
    return (valid_float, valid);
        
def validate_pos_dif (start_milage, end_milage):
    if (end_milage > start_milage):
       return True; 
    else: 
       print("Your ending odometer reading must be higher than your beginning odometer reading!  Please try again.")
       return False; 
  

def main():
  # Get an odometer value in U.S. miles from the user.
    valid = False; 
    while not valid:
       user_input = input("Enter the first odometer reading (miles):");
       (start_miles, valid) = validate_float(user_input); 
    
  # Get another odometer value in U.S. miles from the user.
    valid = False; 
    while not valid:
       user_input = input("Enter the second odometer reading (miles):")
       (end_miles, valid) = validate_float(user_input);
       if valid:
          valid = validate_pos_dif(start_miles, end_miles);

  # Get a fuel amount in U.S. gallons from the user.
    valid = False; 
    while not valid:
       user_input = input("Enter the amount of fuel used (gallons):");
       (amount_gallons, valid) = validate_float(user_input);

  # Call the miles_per_gallon function and store
  # the result in a variable named mpg.
    mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

  # Call the lp100k_from_mpg function to convert the
  # miles per gallon to liters per 100 kilometers and
  # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)
  # Display the results for the user to see.
    print(f"{mpg} miles per gallon");
    print(f"{lp100k} liters per 100 kilometers")
#  pass
def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.
    Parameters
    start_miles: An odometer value in miles.
    end_miles: Another odometer value in miles.
    amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    mpg= (end_miles-start_miles)/amount_gallons;
    return mpg;

def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.
    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp100k = 235.215/mpg; 
    return lp100k;

# Call the main function so that
# this program will start executing.
main()