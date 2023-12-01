import tkinter as tk
from tkinter import messagebox

def generate_voucher():
    student_name = entry_name.get()
    student_roll = entry_roll.get()
    fee_amount = entry_fee.get()

    if not student_name or not student_roll or not fee_amount:
        messagebox.showerror("Error", "Please fill in all fields.")
    else:
        voucher_text = f"Fee Voucher\n\nStudent Name: {student_name}\nRoll Number: {student_roll}\nFee Amount: {fee_amount}"
        voucher_label.config(text=voucher_text)

# Create the main window
root = tk.Tk()
root.title("Fee Voucher Generator")

# Create and place widgets
label_name = tk.Label(root, text="Student Name:")
label_name.grid(row=0, column=0, sticky="e", padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_roll = tk.Label(root, text="Roll Number:")
label_roll.grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_roll = tk.Entry(root)
entry_roll.grid(row=1, column=1, padx=10, pady=5)

label_fee = tk.Label(root, text="Fee Amount:")
label_fee.grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_fee = tk.Entry(root)
entry_fee.grid(row=2, column=1, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Voucher", command=generate_voucher)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

voucher_label = tk.Label(root, text="", font=("Arial", 12))
voucher_label.grid(row=4, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
