import tkinter as tk

def file_new():
  


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



def file_open():
    

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


def file_save():
    

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


def edit_cut():
    print("Cut")

def edit_copy():
    print("Copy")

def edit_paste():
    print("Paste")

# Create the main window
root = tk.Tk()
root.title("Tkinter Menu Example")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Admition Voucher", command=file_new)
file_menu.add_command(label="Semester voucher", command=file_open)
file_menu.add_command(label="Rapeat Course Voucher", command=file_save)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Create Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=edit_cut)
edit_menu.add_command(label="Copy", command=edit_copy)
edit_menu.add_command(label="Paste", command=edit_paste)

# Run the main loop
root.mainloop()
