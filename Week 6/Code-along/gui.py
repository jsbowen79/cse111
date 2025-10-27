import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import random


def main(): 
    root=tk.Tk()
    root.option_add("*Font", "Helvetica 16")
    frm_main=Frame(root)
    frm_main.master.title("Dice")
    frm_main.pack(padx=3,pady=3, fill=tk.BOTH,expand=True)
    setup_main(frm_main)
    frm_main.mainloop()

def setup_main(frm): 
    lbl_sides=Label(frm, text="Enter the number of sides on the Dice (2-20)")
    lbl_sides.grid (row=0, column=0, padx=5, pady=5)
    ent_sides=IntEntry(frm,lower_bound=2, upper_bound=20, width=4)
    ent_sides.grid(row=0, column=1)
    
    
    
    lbl_count=Label(frm, text="How many dice do you want to roll(1-10)")
    lbl_count.grid (row=2, column=0, padx=5, pady=5)
    ent_count=IntEntry(frm, lower_bound=1, upper_bound=10, width=5)
    ent_count.grid(row=2, column=1)

    btn_roll=Button(frm, text="Roll the Dice")
    btn_roll.grid(row=4, column=0)
    lbl_roll=Label(frm, text="")
    lbl_roll.grid(row=5, column=0, padx=5, pady=5)

    def roll_dice(sides,count):
        sum=0
        roll_text=""
        for roll in range(count):
            die_roll=random.randint(1, sides)
            sum+=die_roll
            roll_text+=f"{die_roll} "
        roll_text+=f"Total {sum}"
        return roll_text


    def roll_action(): 
        try: 
            sides=ent_sides.get()
        except ValueError:
            lbl_roll.config(text="You must enter a valid number of sides")
            return
        try: 
            count=ent_count.get()
        except ValueError: 
            lbl_roll.config(text="You must enter a valid number of dice")
            return
        textlbl=roll_dice(sides,count)
        lbl_roll.config(text=textlbl)

    btn_roll.config(command=roll_action)

if __name__=="__main__":
    main()




    