import tkinter as tk

def generate_fee_voucher():
    student_name = entry_name.get()
    course_fee = entry_course_fee.get()

    # Validate input
    if not student_name or not course_fee.isdigit():
        result_label.config(text="Invalid input. Please enter valid data.")
        return

    total_fee = int(course_fee)

    # Create fee voucher text
    voucher_text = f"Student Name: {student_name}\nCourse Fee: {course_fee} Rs.\nTotal Fee: {total_fee} Rs."

    # Display the voucher
    result_label.config(text=voucher_text)

# Create the main window
root = tk.Tk()
root.title("Fee Voucher Generator")

# Create and place widgets
label_name = tk.Label(root, text="Student Name:")
label_name.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_course_fee = tk.Label(root, text="Course Fee:")
label_course_fee.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

entry_course_fee = tk.Entry(root)
entry_course_fee.grid(row=1, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Voucher", command=generate_fee_voucher)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()