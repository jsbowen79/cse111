"""This program will allow a user to keep a budget and to keep a check register.
Eventually, the program will allow users to save and load their files.  It will 
also allow them to add new accounts to the check register.  Finally, It will 
eventually scan a bank statement and help the user balance their account.  The 
final three functions were not able to be completed in the time that was available
for this project. """

#Import tools needed for the program

import tkinter as tk
from tkinter import Frame, Label, Button, ttk, messagebox
from datetime import datetime
from dateutil import parser

#Create global libraries to store the information for the budget and bank accounts

data = {}
account_data = {}


def get_safe_date(user_input):
    """This function will allow the user to input the date in many formats and will 
    Return a valid formatted date, or raise ValueError if the entry is invalid.
    Arguments: user_input
    Returns: formatted date or error message"""

    user_input = user_input.strip()
    if not user_input:
        return datetime.now().strftime("%Y-%m-%d")  # default today
    try:
        dt = parser.parse(user_input)
        return dt.strftime("%Y-%m-%d")
    except (ValueError, OverflowError) as e:
        messagebox.showerror("Invalid Date", str(e))
        
def validate_float(input):      
    """This function will take input from the user and ensure that it is a valid
    floating point number.  If the input is not a floating point number or cannot
    be converted to one, the function will display a message and end returning 
    "None" which will cause the issuing function to stop running.
    Arguments: input -user input
    Return: floating point number or "None" 
    """
    try:
        amount = float(input)
        return amount
    except ValueError:
        if tk._default_root is not None: 
            messagebox.showerror("Invalid Input", "Amount must be a number.")
        return None
        

def refresh_table(tree, data):
    """This function will clear the Treeview and redraw all rows from the updated data.
    Arguments:  tree-the treeview object created by another function
                data-the dictionary associated with the request
    Return:     The function does not return anything, but updates the treeview object. """
    for row in tree.get_children():
        tree.delete(row)

    total_income = 0
    total_expense = 0
    
    #Separates the budget function from the Register function as their treeview objects are different. 
    #This is necessary to allow the refresh_tables function to be used by both functions. 
    #Budget Function code
    if any(entry_type == "income" for(transaction_id, (validated_date, item, entry_type, amount, trans_num)) in data.items()):

        for i, (transaction_id, (validated_date, item, entry_type, amount, trans_num )) in enumerate(data.items()):
         
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            income_val = f"${amount:,.2f}" if entry_type == "income" else ""
            expense_val = f"${abs(amount):,.2f}" if entry_type == "expense" else ""

            if entry_type == "income":
                total_income += amount
            else:
                total_expense += abs(amount)

            tree.insert("", "end", iid=transaction_id,
                        values=(transaction_id, item, income_val, expense_val, "❌"),
                        tags=(tag, entry_type))

        # Totals rows
        net_total = total_income - total_expense
        tree.insert("", "end", values=("", "Totals:", f"${total_income:,.2f}", f"${total_expense:,.2f}", ""), tags=("total",))
        net_tag = "netpositive" if net_total >= 0 else "netnegative"
        tree.tag_configure("netpositive", foreground="green", font=("Helvetica", 18, "bold"))
        tree.tag_configure("netnegative", foreground="red", font=("Helvetica", 18, "bold"))
        tree.insert("", "end", values=("", "Net Total:", f"${net_total:,.2f}", "", ""), tags=(net_tag,))

    #Register Function code    
    else: 
        total=0
        for i, (transaction_id, (validated_date, item, entry_type, amount, trans_num )) in enumerate(data.items()):
            tag = "evenrow" if i % 2 == 0 else "oddrow"
            debit_val = f"${amount:,.2f}" if entry_type == "debit" else ""
            credit_val = f"${(amount):,.2f}" if entry_type == "credit" else ""
            total += amount
        
            tree.insert("", "end", iid=transaction_id,
                       values=(transaction_id, validated_date, trans_num, item, debit_val, credit_val, total, "❌"),
                       tags=(tag, entry_type))

    tree.update_idletasks()

def on_tree_click(event, tree, data, refresh_table):
    """This function handle when the user clicks in the Treeview object.  The function will delete
     the associated row  if the ❌ in the delete column is clicked.
     Arguments:     event: the event that is detected when a user clicks the treeview object.  
                    tree: the treeview object that was clicked on
                    data: the dictionary associated with the treeview object that was clicked on
                    refresh_table: the refresh_table() function so the treeview object can be redrawn
    Returns:        This function does not return a value.  It deletes the associated information from the 
                    dictionary and redraws the table."""
    
    region = tree.identify("region", event.x, event.y)
    if region != "cell":
        return     
    column = tree.identify_column(event.x)

    #Selects the appropriate column depending on the treeview object clicked
    if any(entry_type == "income" for(transaction_id, (validated_date, item, entry_type, amount, trans_num)) in data.items()):
        if column != "#5":  # the 5th column is "Delete" in the Budget table
            return
    else: 
        if column != "#8": # the 8th column is "Delete" in the Register table
            return

    row_id = tree.identify_row(event.y)
    if not row_id:
        return

    vals = tree.item(row_id, "values")
    if not vals:
        return

    try:
        transaction_id = int(vals[0])
    except ValueError:
        return

    if transaction_id in data:
        del data[transaction_id]
        refresh_table(tree, data)


def main():
    #Create main frame    
    root=tk.Tk()
    root.geometry("2800x1000")
    root.title("BookKeeper")
  
    frm_main=Frame(root, bg="lightblue", padx=6, pady=6)
    frm_main.pack(padx=6, pady=6, fill=tk.BOTH, expand=True)
    budget_tree=setup_budget_app(root)
    budget_tree.refresh_table()
    register_tree=setup_register_app(root)
    register_tree.refresh_table()

    root.mainloop()
    
def setup_budget_app(root):    
    """This function will set up the tkinter frame and the treeview object for the Budget app"""
    def add_entry():
        """This function will collect data from the Tkinter Input boxes for Budget Item and Amount.  
        It will then send the input to the validate_float() function to ensure it is the proper data 
        type.  The function will end if the data is of the wrong type.  The function will continue if 
        the data type is correct.  It will then assign the data to the amount variable as a positive
        or negative number depending on the radio button that is checked (Income or Expense). This will
        happen regardless of whether the amount that was input by the user was positive or negative. 
        The function will then add the entry to the data {} dictionary. This function will also call the 
        refresh_table() function which will refresh the treeview table with the updated data.  This 
        function will then clear the amount entry variables for the next use. 
        """
        transaction_id= len(data) + 1
        input_amount=amount_entry.get() 
        amount=validate_float(input_amount)
        
        if amount is None: 
            return

        item= item_entry.get() or "Unknown Item"
        entry_type = type_var.get() or "expense"
        if entry_type == "expense" and amount > 0: 
            amount=-amount

        data[transaction_id]=[item, "", entry_type, amount, ""]
        budget_tree.refresh_table()
        amount_entry.delete(0, tk.END)
        item_entry.delete(0, tk.END)

    #Setup budget frame to take information about budget items
    budget=tk.Frame(root, borderwidth=2, relief="groove", padx=10, pady=10, width=1000, height=1000)   
    budget.pack_propagate(False)
    budget.pack(side="left", padx=10, pady=10, fill="both")
    title_label= tk.Label(budget, text="Budget App", font=("Helvetica", 20, "bold"))
    title_label.pack(anchor="center", pady=(0,10))
                    
    #Use Tkinter to create a label for the Budget Item input box.  Create the box and put both in the frame. 
    tk.Label(budget, text="Budget Item").pack()
    item_entry=tk.Entry(budget)
    item_entry.pack()

    #Use Tkinter to create a label for the amount input box. Create the amount entry box and put both in the frame.  
    tk.Label(budget, text="Amount").pack()
    amount_entry=tk.Entry(budget)
    amount_entry.pack()   

    # Create Radio Buttons and labels to collect and store results in variable "type-var"
    type_var = tk.StringVar(value="income")  # default
    frame_type = tk.Frame(budget)
    frame_type.pack(pady=4)
    tk.Label(frame_type, text="Type:").pack(side="left")
    tk.Radiobutton(frame_type, text="Income", variable=type_var, value="income").pack(side="left", padx=5)
    tk.Radiobutton(frame_type, text="Expense", variable=type_var, value="expense").pack(side="left", padx=5)

    #Create submit button to save an entry to the dictionary. 
    tk.Button(budget, text="Enter Budget Item", command=add_entry).pack(pady=6)
    tree_frame=Frame(budget)
    tree_frame.pack(fill="both", expand=True, padx=5, pady=5)

    #Create columns in treeview table
    columns = ("Item", "Budget Item", "Income", "Expense", "Delete")
    budget_tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
    budget_tree.pack(side="left", fill="both", expand=True)

    budget_tree.heading("Item", text="Item")
    budget_tree.column("Item", width=50, anchor="e")

    budget_tree.heading("Budget Item", text="Budget Item")
    budget_tree.column("Budget Item", width=250, anchor="w")

    budget_tree.heading("Income", text="Income")
    budget_tree.column("Income", width=180, anchor="e")

    budget_tree.heading("Expense", text="Expense")
    budget_tree.column("Expense", width=180, anchor="e")

    budget_tree.heading("Delete", text="Delete")
    budget_tree.column("Delete", width=50, anchor="e")

    #Style the columns in treeview table. 
    style=ttk.Style()
    style.configure("Treeview",
                    highlightthickness=1,
                    bd=1,
                    relief="solid",
                    rowheight=40,
                    font=("Helvetica", 18))
    style.configure("Treeview.Heading", font=("Helvetica", 20, "bold"))

    budget_tree.tag_configure("oddrow", background="#b4b4b4")
    budget_tree.tag_configure("evenrow", background="white")
    budget_tree.tag_configure("income", foreground="green")
    budget_tree.tag_configure("total", background="#d0d0ff", font=("Helvetica", 20, "bold"))
    budget_tree.tag_configure("expense", foreground="red")
    style.layout("Treeview", [("Treeview.treearea", {"sticky": "nswe"})])
    budget_tree.pack(fill="both", expand=True, padx=6, pady=6)
    refresh_table(budget_tree, data)

    #Create scroll bar and Populate table
    scrollbar=ttk.Scrollbar(tree_frame, orient="vertical", command=budget_tree.yview)
    scrollbar.pack(side="right", fill="y")
    budget_tree.configure(yscrollcommand=scrollbar.set)
    budget_tree.bind("<Button-1>", lambda e: on_tree_click(e, budget_tree, data, refresh_table))
    budget_tree.data=data
    budget_tree.refresh_table=lambda:refresh_table(budget_tree,data)
    return budget_tree

def setup_register_app(root):
    """This function will set up the frame for the Register app.  It will also set up the Treeview object
    that holds the table.  The add_entry function is significantly different from the one in the Budget 
    app; so, it is not combined."""
    
    def add_entry():
      """This function will collect data from the user using Tkinter Input boxes.  It will validate 
      floats with the validate_float function.  It will assign the data to either the 'Debit' or 
      'Credit' column depending on the user's choice.  The function will then add the information to
      the 'account{}' dictionary. """
      transaction_id= len(account_data) + 1
      input_amount=amount_entry.get()
      amount=validate_float(input_amount)
      trans_num=trans.get() or ""   
      validated_date = get_safe_date(date_entry.get())

      if validated_date is None: 
          return

      if amount is None: 
          return
      
      item= item_entry.get() or "Unknown"
      entry_type = type_var.get() or "credit"
      if entry_type == "credit" and amount > 0:
          amount=-amount
          
      account_data[transaction_id]=[validated_date, item, entry_type, amount, trans_num]
      register_tree.refresh_table()
      amount_entry.delete(0, tk.END)
      item_entry.delete(0, tk.END)

    #Setup budget frame to take information about budget items
    account=tk.Frame(root, borderwidth=2, relief="groove", padx=10, pady=10)   
    account.pack(side="right", padx=10, pady=10, fill="both", expand=True)

    #Create a label for the account register
    title_label= tk.Label(account, text="Account Register", font=("Helvetica", 20, "bold"))
    title_label.pack(anchor="center", pady=(0,10))

    
    #Create a label and input box for the Date
    tk.Label(account, text="Date: ").pack()
    date_entry=tk.Entry(account)
    date_entry.pack()
    date_entry.insert (0, datetime.now().strftime("%Y-%m-%d"))

    #Create a label and input box for transaction number
    tk.Label(account, text="Transaction Number: ").pack()
    trans=tk.Entry(account)
    trans.pack()
                    
    #Use Tkinter to create a label for the Budget Item input box.  Create the box and put both in the frame. 
    tk.Label(account, text="Description: ").pack()
    item_entry=tk.Entry(account)
    item_entry.pack()

    #Use Tkinter to create a label for the amount input box. Create the amount entry box and put both in the frame.  
    tk.Label(account, text="Amount: ").pack()
    amount_entry=tk.Entry(account)
    amount_entry.pack()   

    # Create Radio Buttons and labels to collect and store results in variable "type-var"
    type_var = tk.StringVar(value="debit")  # default
    frame_type = tk.Frame(account)
    frame_type.pack(pady=4)
    tk.Label(frame_type, text="Transaction Type:").pack(side="left")
    tk.Radiobutton(frame_type, text="Debit", variable=type_var, value="debit").pack(side="left", padx=5)
    tk.Radiobutton(frame_type, text="Credit", variable=type_var, value="credit").pack(side="left", padx=5)

    #Create submit button to save an entry to the dictionary. 
    tk.Button(account, text="Enter Item", command=add_entry).pack(pady=6)
    tree_frame = Frame(account)
    tree_frame.pack(fill="both", expand=True, padx=6, pady=6)

    #Create columns in treeview table
    columns = ("ID", "trans_num", "date", "trans", "debit", "credit", "total", "delete")
    register_tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
    register_tree.pack(side="left", fill="both", expand=True)
    
    register_tree.heading("ID", text="ID")
    register_tree.column("ID", width=60, anchor="w")

    register_tree.heading("trans_num", text="Transaction ID")
    register_tree.column("trans_num", width=300, anchor="w")

    register_tree.heading("date", text="Date")
    register_tree.column("date", width=50, anchor="w")

    register_tree.heading("trans", text="Name")
    register_tree.column("trans", width=240, anchor="e")

    register_tree.heading("debit", text="Debit")
    register_tree.column("debit", width=220, anchor="e")

    register_tree.heading("credit", text="Credit")
    register_tree.column("credit", width=220, anchor="e")

    register_tree.heading("total", text="Balance")
    register_tree.column("total", width=220, anchor="e")

    register_tree.heading("delete", text="Delete")
    register_tree.column("delete", width=50, anchor="e")

    #Style the columns in treeview table. 
    style=ttk.Style()
    style.configure("Treeview",
                    highlightthickness=1,
                    bd=1,
                    relief="solid",
                    rowheight=40,
                    font=("Helvetica", 18))
    style.configure("Treeview.Heading", font=("Helvetica", 20, "bold"))
    register_tree.tag_configure("oddrow", background="#b4b4b4")
    register_tree.tag_configure("evenrow", background="white")
    style.layout("Treeview", [("Treeview.treearea", {"sticky": "nswe"})])
    register_tree.pack(fill="both", expand=True, padx=6, pady=6)
    refresh_table(register_tree, account_data)

    #Create scroll bar and Populate table
    scrollbar=ttk.Scrollbar(tree_frame, orient="vertical", command=register_tree.yview)
    scrollbar.pack(side="right", fill="y")
    register_tree.configure(yscrollcommand=scrollbar.set)
    register_tree.bind("<Button-1>", lambda e: on_tree_click(e, register_tree, account_data, refresh_table))
    register_tree.data=account_data
    register_tree.refresh_table=lambda:refresh_table(register_tree,account_data)

    return register_tree

if __name__=="__main__": 
    main()