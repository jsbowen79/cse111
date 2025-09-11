"""This program will check passwords for complexity requirements and give the password a complexity score.  It will 
also check passwords to see if they are contained in a list of common passwords or dictionary words.  I added several 
extra features to my program.  I imported OS and used it to change the file handling to explicit to avoid any errors 
running the program as long as the appropriate files are located in the same directory as the .py file.  This also solved
a problem with the file running perfectly in the python window, but failing to find the files in the debugger.  I also 
added logic at the end to give one message if the password scored less than a 5 and another message if the password scored 
a 5.  I also repeated the password that was checked so the user was sure they typed it correctly.  To save processing time, 
I stopped all loops as soon as a match was found.  """

import os


# Define character sets for password complexity. 

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]
character_list = UPPER + LOWER + DIGITS + SPECIAL

def word_in_file(word, filename, case_sensitive=False): 
    """This function will compare the password parameter to the words in the list of common dictionary words.  If the word 
    matches any word in the word list, the function will return a boolean value of True.  If there is no match, the function
    will return a boolean value of False. The function has a default value of false for case_sensitive"""
    script_dir = os.path.dirname(__file__)  
    file_path = os.path.join(script_dir, filename)
    
    with open(file_path, "r", encoding="utf-8") as wordfile:
        for x in wordfile:
            if case_sensitive == False: 
                if x.strip().lower() == word.strip().lower(): 
                    return True
            else: 
                if x.strip() == word.strip():
                    return True
            
        return False
        

def word_has_character(word, character_list):
    """This function will search the characters in the password and compare them to the supplied character list.  It will
    return True if the character is contained in the supplied list and False if it is not"""
    for i in word: 
        if i in character_list: 
            return True
    return False

def word_complexity (word):
    """This function will determine a numeric complexity value between 0 and 4 for each password based on the types of characters 
    the password contains."""
    password_complexity = 1
    lower = word_has_character(word, LOWER)
    upper = word_has_character(word, UPPER)
    digits = word_has_character(word, DIGITS)
    special = word_has_character(word, SPECIAL)
    if lower: 
        password_complexity +=1
    if upper: 
        password_complexity +=1
    if digits: 
        password_complexity +=1
    if special:
        password_complexity +=1
    return password_complexity

def password_strength (password, min_length=10, strong_length=16):
    in_dict = word_in_file(password, "./wordlist.txt", False)
    if in_dict: 
        print(f'The password "{password}" is a dictionary word and is not secure.')
        return 0
    top_pass_list = word_in_file(password, "toppasswords.txt", True)
    if top_pass_list: 
        print(f'The password "{password}" is a commonly used password and is not secure.')
        return 0
    if len(password) < min_length:
        print(f'The password "{password}" is too short and is not secure.  Passwords should be at least {min_length} characters.')
        return 1
    if len(password)> strong_length:
        print(f'The password "{password}" is long. Length trumps complexity. This is a good password.')
        return 5
    else: 
        strength = int(word_complexity(password))
        print(f'The password "{password}" scored a {strength}.')
        return (strength)
        
    
def main():
    # Define initial password as none-type to allow for looping.  Begin loop. 
    password = None    
    while password not in ("Q", "q"): 
        password = input("Please enter the password you would like to check.  Press Q to Quit.")
        if password not in ("Q", "q"):
            strength = password_strength(password)
            if strength < 5: 
                print("Your password is weak! Never use dictionary words or common passwords.  Try longer passwords with different character types.")
            else: 
                print("Excellent job! Your password is strong! Strong passwords protect everyone!")
        else: 
            print("Thankyou for using the password checker to improve your password strength.  Good passwords protect everyone!")
          

if __name__ == "__main__":
    main()
