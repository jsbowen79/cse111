import tkinter as tk
from tkinter import messagebox, ttk 
from checkbook_balancer import validate_float, refresh_table, get_safe_date
import pytest
from pytest import approx
from datetime import datetime
from unittest.mock import patch

@patch("tkinter.messagebox.showerror")   # ⬅️ this line replaces the real messagebox

def test_validate_float(mock_showerror):
    """Test the validate_float function to ensure it returns either a valid float or 
    a "None" value.  A valid float will allow the add_entry function to continue.  A
    "None" value will exit the add_entry function without an error and allow the 
    user to try again."""
    root = tk.Tk()
    root.withdraw()

    assert validate_float(25) == approx (25.0)
    assert validate_float(13.1) == approx (13.1)
    assert validate_float("abs") == None
    assert validate_float (-13.1) == approx(-13.1)
    assert validate_float (-5) == approx (-5.0)
    assert validate_float ("13K") == None
    assert validate_float ("12@#$") == None
    assert mock_showerror.call_count == 3

def test_refresh_table_income_mode():
    root = tk.Tk()
    root.withdraw()
    tree= ttk.Treeview(root, columns=("ID", "Item", "income", "expense", "Delete"))

    data = {
    1: ("2025-10-14", "Salary", "income", 1000, "T1"),
    2: ("2025-10-14", "Rent", "expense", 400, "T2"),
    3: ("2025-10-14", "Electricity", "expense", 500, "T3"),
    4: ("2025-10-14", "Bonus", "income", 500, "T4")
}


    refresh_table(tree, data)

    root.update_idletasks()

    rows = tree.get_children()
    assert len(rows) == 6

    first =tree.item(rows[0])["values"]
    assert first [1] == "Salary"
    assert first [2] == "$1,000.00"
    assert first [3] == ""

    first =tree.item(rows[1])["values"]
    assert first [1] == "Rent"
    assert first [3] == "$400.00"
    assert first [2] == ""
    

    totals_row = tree.item(rows[4])["values"]
    assert totals_row[1] == "Totals:"
    assert totals_row[2] == "$1,500.00"
    assert totals_row[3] == "$900.00"

    root.destroy()

def test_refresh_table_credit_mode():
    root = tk.Tk()
    root.withdraw()
    tree = ttk.Treeview(root, columns=("ID", "Date", "Trans Num", "Item", "Debit", "Credit", "Balance", "Delete"))  

    data = {
    1: ("2025-10-14", "Deposit", "debit", 500, "T1"),
    2: ("2025-10-14", "Groceries", "credit", -200, "T2"),
    3: ("2025-10-14", "Car Parts", "credit", -250, "T3"),
    4: ("2025-10-14", "Bonus", "debit", 200, "T4")
}


    refresh_table(tree, data)

    root.update_idletasks()

    rows = tree.get_children()
    assert len(rows) == 4 

    first = tree.item(rows[0])["values"]
    assert first[3] == "Deposit" 
    assert first[4] =="$500.00"
    assert first[5] == ""
    assert first[6] == 500.00

    last = tree.item(rows[2])["values"]
    assert last[3] == "Car Parts" 
    assert last[5] =="$-250.00"
    assert last[4] == ""
    assert last[6] == 50.00

    root.destroy()


def test_get_safe_date():
    assert get_safe_date("") == approx(datetime.now().strftime("%Y-%m-%d"))
    assert get_safe_date("12-15-12")=="2012-12-15"
    assert get_safe_date("1/2/3")=="2003-01-02"
    assert get_safe_date("5-6-2024")=="2024-05-06"



pytest.main(["-v", "--tb=line", "-rN", __file__])

