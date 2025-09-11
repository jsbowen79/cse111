"""This program calculates the storage efficiency of 12 common steel can sizes and then prints those sizes to the terminal"""
#Import math module for pi
import math

def compute_storage_efficiency (radius, height): 
    """This function computes the storage efficiency of the can with the radius and height given as parameters.  
    In this particular program, this function did not save any space because the way I wrote it originally, I 
    only had to enter the formulas once.  The same is true for the compute_cost_efficiency function below"""
    volume = math.pi * radius**2 * height
    surf_area = 2 * math.pi * radius * (radius + height) 
    storage_efficiency = volume/surf_area
    return storage_efficiency

def compute_cost_efficiency(radius, height, cost):
    """This function computes the cost efficiency of a can with the dimensions and cost passed in as parameters"""
    volume = math.pi * radius**2 * height
    cost_efficiency = volume / cost
    return cost_efficiency

def main():
    #Create global variables to store highest cost and storage efficiency statistics. 
    most_storage_efficient = None
    most_cost_efficient = None
    highest_storage_efficiency = 0
    highest_cost_efficiency= 0

    # Create Dictionary of cans and sizes.  
    can_dict = {
        1:{"can_name": "#1 Picnic", "radius": 6.83, "height": 10.16, "cost_per_can": 0.28, "storage_efficiency" : None, "cost_efficiency" : None},
        2:{"can_name":"#1 Tall", "radius": 7.78, "height": 11.91, "cost_per_can": 0.43, "storage_efficiency" : None, "cost_efficiency" : None},
        3:{"can_name":"#2", "radius": 8.73, "height": 11.59, "cost_per_can": 0.45, "storage_efficiency" : None, "cost_efficiency" : None},
        4:{"can_name":"#2.5", "radius": 10.32, "height": 11.91, "cost_per_can": 0.61, "storage_efficiency" : None, "cost_efficiency" : None},
        5:{"can_name":"#3 Cylinder", "radius": 10.79, "height": 17.78, "cost_per_can": 0.86, "storage_efficiency" : None, "cost_efficiency" : None},
        6:{"can_name":"#5", "radius": 13.02, "height": 14.29, "cost_per_can": 0.83, "storage_efficiency" : None, "cost_efficiency" : None},
        7:{"can_name":"#6Z", "radius": 5.40, "height": 8.89, "cost_per_can": 0.22, "storage_efficiency" : None, "cost_efficiency" : None},
        8:{"can_name":"#8Z short", "radius": 6.83, "height": 7.62, "cost_per_can": 0.26, "storage_efficiency" : None, "cost_efficiency" : None},
        9:{"can_name":"10", "radius": 15.72, "height": 17.78, "cost_per_can": 1.53, "storage_efficiency" : None, "cost_efficiency" : None},
        10:{"can_name":"211", "radius": 6.83, "height": 12.38, "cost_per_can": 0.34, "storage_efficiency" : None, "cost_efficiency" : None},
        11:{"can_name":"#300", "radius": 7.62, "height": 11.27, "cost_per_can": 0.38, "storage_efficiency" : None, "cost_efficiency" : None},
        12:{"can_name":"#303", "radius": 8.10, "height": 11.11, "cost_per_can": 0.42, "storage_efficiency" : None, "cost_efficiency" : None}
    }

    # Loop through cans
    for can_id, attributes in can_dict.items():

        """Calculate storage_efficiency and enter it into the dictionary for the appropriate can. If the storage_efficiency is 
        higher than the previous efficiency, store the can name and the storage_efficiency as a variable"""
        
        storage_efficiency = compute_storage_efficiency(attributes["radius"], attributes["height"])
        attributes["storage_efficiency"] = round(storage_efficiency,2)
        if storage_efficiency > highest_storage_efficiency: 
            highest_storage_efficiency = storage_efficiency
            most_storage_efficient = attributes["can_name"]
        

        """Calculate cost_efficiency and enter it into the dictionary for the appropriate can. If the cost_efficiency is higher
        that the previous efficiency, store the can name and the cost_efficiency as a variable.  Print the cost and storage
        efficiency ratings for each can while still inside the loop."""

        cost_efficiency = compute_cost_efficiency(attributes["radius"], attributes["height"], attributes["cost_per_can"])
        attributes["cost_efficiency"]=cost_efficiency 
        if cost_efficiency > highest_cost_efficiency:
            highest_cost_efficiency = cost_efficiency
            most_cost_efficient = attributes["can_name"]
        print (f"The {attributes["can_name"]} can has a storage efficiency of {storage_efficiency:.2f} and a cost efficiency of {cost_efficiency:.2f}.")      

    """Print the highest cost and storage efficient cans"""

    print (f"\n\nThe {most_cost_efficient} can is the most cost efficient with a cost efficiency rating of {highest_cost_efficiency:.2f}!")
    print (f"The {most_storage_efficient} can is the most storage efficient with a storage efficiency rating of {highest_storage_efficiency:.2f}!")
       # print(f"{can_name}: Volume={volume:.2f}, Storage Efficiency : {storage_efficiency:.2f}")

"""run the program"""
main()














