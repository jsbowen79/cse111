"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

# By Joseph Bowen
print(f"This program will calculate the optimum heart-rate range to strengthen your heart during exercise.")
age = int(input("To start, please enter your current age?"))
max = 220 - age 
lowest = round(max * .65)
highest = round(max * .85)

print("When you exercise to strengthen your heart, you should\n"
      f"keep your heart rate between {lowest} and {highest} beats per minute.")


