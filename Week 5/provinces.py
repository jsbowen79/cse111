"""This program will import values from a csv file into a list and then modify some of 
the elements in the list. It will then count the occurrences of "Alberta" in the list
and print the total number of occurrences."""
#import tools
import csv
import os

def create_list():
    provinces_list = []
    file_dir = os.path.dirname(__file__)
    file_path = os.path.join(file_dir, "provinces.txt")

    with open(file_path, "rt") as file:
        for province in file: 
            clean_province = province.strip()
            provinces_list.append(clean_province) 
    return provinces_list

def remove_first(provinces_list):
    del provinces_list[0] 

def remove_last(provinces_list): 
    last_index= len(provinces_list)-1
    del provinces_list[last_index]

def replace_ab(provinces_list):
    i = 0
    for province in provinces_list:
        if province =="AB": 
            provinces_list[i] = "Alberta"
        i +=1
def count_alberta(provinces_list):
    alberta_count = 0
    for province in provinces_list: 
        if province == "Alberta": 
            alberta_count += 1
    return alberta_count

def main():
    provinces_list = create_list()
    print(provinces_list)
    remove_first(provinces_list)
    print(provinces_list)
    remove_last(provinces_list)
    print(provinces_list)
    replace_ab(provinces_list)
    print(provinces_list)
    alberta_count= count_alberta(provinces_list)
    print(f'The total number of "Alberta" provinces listed in the file is {alberta_count}.')

main()