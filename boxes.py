"""In our modern world economy, many items are manufactured in large factories, then packed in boxes and shipped to distribution 
centers and retail stores. A common question for employees who pack items is “How many boxes do we need?”"""
import math

print ("This program will ask the User for the number of items and the number of items packed in each"
"\nbox.  The program will return the number of boxes needed to pack all of the items.")

total_items = int(input("Enter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))
boxes = math.ceil(total_items/items_per_box)
print (f"For {total_items} items, packing {items_per_box} items in each box, you will need {boxes} boxes.")