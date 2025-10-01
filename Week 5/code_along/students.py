"""This program will open the students.csv file and use it to create a dictionary.  It will 
then get an id number from the user and search the dictionary for the students name.  It
will print the student's name.  The program will print "No such student" if id number 
does not match an id in the dictionary."""
#Import tools
import os
import csv

def create_dict():
    """This function opens the students.csv file and uses it to create a dictionary variable.
    Parameters: none
    Return: dictionary
    """

    filepath = os.path.dirname(__file__)
    file = os.path.join(filepath, "students.csv")
    students_dict = {}
    key_index = 0
    name_index = 1

    with open(file, "rt") as csv_file:
        reader=csv.reader(csv_file)
        next(reader)
        for line in reader:
           id=int(line[key_index])
           name=line[name_index]
           students_dict[id]=name
    return students_dict

def get_student_id():
    while True:
        user_input = input("Please enter an ID number: ")
        if "-" in user_input:
           user_input=user_input.replace("-", "")
        if len(user_input)>9: 
            print("Invalid ID Number: too many digits\n")
        if len(user_input)<9:
            print("Invalid ID Number: too few digits\n")
        try: 
            id_number = int(user_input)
            return id_number

        except ValueError: 
            print(f'\n{user_input} is not a number.  Please enter a number!\n')
        
def search_id(student_id, students_dict):
    while True: 
        try: 
            name = students_dict[student_id]
            return name
        
        except KeyError: 
            print(f"No such student.  The id {student_id} does not exist in the database. ")
            print("Please try another ID.")
            student_id=get_student_id()
        
def main(): 
    students_dict=create_dict()
    print (students_dict)
    student_id= get_student_id()
    name=search_id(student_id, students_dict)
    print(f"The student is {name}.")
main() 