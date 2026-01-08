import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# DB Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="restaurant_db"
)
cursor = conn.cursor()

# Check item availability
def check_and_order():
    item = entry_item.get().strip().title()
    name = entry_name.get().strip().title()
    table = entry_table.get().strip()

    if not item or not name or not table:
        messagebox.showerror("Missing Info", "Please fill all fields.")
        return

    cursor.execute("SELECT item_name, category, price FROM menu WHERE item_name = %s", (item,))
    result = cursor.fetchone()

    if result:
        item_name, category, price = result
        cursor.execute("""
            INSERT INTO customer_orders (customer_name, table_number, item_name, category, price)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, table, item_name, category, price))
        conn.commit()
        messagebox.showinfo("Success", f"{item_name} ordered successfully!")
        load_orders()
    else:
        messagebox.showwarning("Not Found", f"{item} is not available in menu.")

# Load all orders into the table
def load_orders():
    for row in order_table.get_children():
        order_table.delete(row)
    cursor.execute("SELECT order_id, customer_name, table_number, item_name, category, price FROM customer_orders")
    for order in cursor.fetchall():
        order_table.insert("", tk.END, values=order)

# GUI
root = tk.Tk()
root.title("Restaurant Order System")
root.geometry("800x500")

# Input Fields
tk.Label(root, text="Customer Name").grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10)

tk.Label(root, text="Table Number").grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_table = tk.Entry(root)
entry_table.grid(row=1, column=1, padx=10)

tk.Label(root, text="Item to Order").grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_item = tk.Entry(root)
entry_item.grid(row=2, column=1, padx=10)

tk.Button(root, text="Place Order", command=check_and_order).grid(row=3, column=1, pady=10)

# Orders Table
columns = ("Order ID", "Customer", "Table", "Item", "Category", "Price")
order_table = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    order_table.heading(col, text=col)
    order_table.column(col, anchor="center", width=100)

order_table.grid(row=4, column=0, columnspan=3, padx=10, pady=20)
load_orders()

root.mainloop()
